#!/usr/bin/env python3
"""Send one text request to a Microsoft Foundry model deployment."""

from __future__ import annotations

import argparse
import os
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path

from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

TOKEN_SCOPE = "https://ai.azure.com/.default"


def load_config(environment: Mapping[str, str]) -> tuple[str, str]:
    """Read and validate the two values required by this sample."""
    endpoint = environment.get("AZURE_OPENAI_ENDPOINT", "").rstrip("/")
    model = environment.get("AZURE_OPENAI_MODEL", "")

    if not endpoint or not model:
        raise ValueError(
            "Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_MODEL before running."
        )
    if not endpoint.startswith("https://"):
        raise ValueError("AZURE_OPENAI_ENDPOINT must be an HTTPS URL.")

    return endpoint, model


def normalize_base_url(endpoint: str) -> str:
    """Convert a resource or Responses endpoint into an OpenAI v1 base URL."""
    endpoint = endpoint.rstrip("/")

    if endpoint.endswith("/openai/v1/responses"):
        return endpoint.removesuffix("responses")
    if endpoint.endswith("/openai/v1"):
        return f"{endpoint}/"
    return f"{endpoint}/openai/v1/"


def create_client(endpoint: str, tenant_id: str | None = None) -> OpenAI:
    """Create an OpenAI client that authenticates with Microsoft Entra ID."""
    credential = DefaultAzureCredential(visual_studio_code_tenant_id=tenant_id)

    # The token provider gets and refreshes Entra tokens for the OpenAI client.
    token_provider = get_bearer_token_provider(credential, TOKEN_SCOPE)

    # The portal may provide either a resource URL or the full Responses URL.
    return OpenAI(
        base_url=normalize_base_url(endpoint),
        api_key=token_provider,
        timeout=30.0,
        max_retries=2,
    )


def ask_model(client: OpenAI, model: str, prompt: str) -> str:
    """Send a prompt and return only the model's text response."""
    response = client.responses.create(model=model, input=prompt)
    return response.output_text


def create_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "prompt",
        nargs="?",
        default="Explain Microsoft Foundry in one sentence.",
        help="Text to send to the model",
    )
    return parser


def main(arguments: Sequence[str] | None = None) -> int:
    """Run the sample and return a process exit code."""
    args = create_parser().parse_args(arguments)

    try:
        # Load configuration kept beside this script, regardless of current folder.
        load_dotenv(Path(__file__).with_name(".env"))
        endpoint, model = load_config(os.environ)
        tenant_id = os.environ.get("AZURE_OPENAI_TENANT_ID")
        answer = ask_model(create_client(endpoint, tenant_id), model, args.prompt)
    except (AzureError, OpenAIError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(answer)
    return 0


if __name__ == "__main__":
    sys.exit(main())