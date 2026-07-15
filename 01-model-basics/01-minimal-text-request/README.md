---
title: Send a Minimal Text Request
description: Call a Microsoft Foundry model from Python with Microsoft Entra ID
ms.date: 2026-07-15
ms.topic: tutorial
---

## What you will learn

This sample sends one prompt to a model deployed in Microsoft Foundry. It uses
Microsoft Entra ID, so no API key is stored in the code.

The sample demonstrates three steps:

1. Read the resource endpoint and model deployment name
2. Create an OpenAI-compatible client with an Entra token provider
3. Send text through the Responses API and print the answer

## Prerequisites

* Python 3.11 or later
* [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
* An Azure OpenAI model deployment in Microsoft Foundry
* The Cognitive Services OpenAI User role on the Foundry resource
* A signed-in Azure account in the VS Code Azure Resources extension, or an
	authenticated Azure CLI session

## Configure and run

On Windows, install `uv` if the command is not available:

```powershell
winget install --id astral-sh.uv --exact
```

Restart the VS Code terminal after installation, then verify it:

```powershell
uv --version
```

From the repository root, install the pinned dependencies:

```powershell
uv sync
```

Sign in through the VS Code Azure Resources extension. Alternatively, sign in
with Azure CLI:

```powershell
az login
```

Copy `.env.example` to `.env`, then set the endpoint shown on your Foundry model
deployment and the deployment name. The endpoint may be the full Responses API
URL. Do not put an API key in this file. The local `.env` file is ignored by Git.
If the resource is in another tenant, set `AZURE_OPENAI_TENANT_ID` as well.

```powershell
Copy-Item 01-model-basics/01-minimal-text-request/.env.example 01-model-basics/01-minimal-text-request/.env
```

Run the default prompt:

```powershell
uv run python 01-model-basics/01-minimal-text-request/minimal_text_request.py
```

Or provide your own prompt:

```powershell
uv run python 01-model-basics/01-minimal-text-request/minimal_text_request.py "What is retrieval-augmented generation?"
```

The command prints one model-generated response. Model usage may incur Azure
charges based on the deployed model and consumed tokens.

## Run the local test

The test uses a fake client and does not need Azure credentials or make a network
request.

```powershell
uv run pytest 01-model-basics/01-minimal-text-request -q
```

## How authentication works

`DefaultAzureCredential` uses your Azure CLI identity during local development.
In an Azure-hosted application, the same code can use managed identity. The token
provider refreshes tokens for the OpenAI client automatically.

See [Azure OpenAI supported programming languages](https://learn.microsoft.com/azure/foundry/openai/supported-languages#authentication)
for the current Microsoft Entra ID authentication pattern.

## Troubleshooting

* A `401` response usually means no usable Microsoft Entra credential was found
* A `403` response usually means the signed-in identity lacks the required role
* A `404` response usually means the endpoint or deployment name is incorrect

This sample creates no Azure resources, so no cleanup is required.