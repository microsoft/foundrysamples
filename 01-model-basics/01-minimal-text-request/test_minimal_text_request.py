"""Local tests for the minimal text request sample."""

from types import SimpleNamespace

import pytest

from minimal_text_request import ask_model, load_config, normalize_base_url


class FakeResponses:
    """Stand in for the network-backed Responses API during local tests."""

    def create(self, *, model: str, input: str) -> SimpleNamespace:
        assert model == "test-deployment"
        assert input == "Hello"
        return SimpleNamespace(output_text="Hello from the fake model")


def test_ask_model_returns_response_text() -> None:
    client = SimpleNamespace(responses=FakeResponses())

    result = ask_model(client, "test-deployment", "Hello")  # type: ignore[arg-type]

    assert result == "Hello from the fake model"


def test_load_config_requires_both_values() -> None:
    with pytest.raises(ValueError, match="AZURE_OPENAI_ENDPOINT"):
        load_config({})


@pytest.mark.parametrize(
    ("endpoint", "expected"),
    [
        (
            "https://example.services.ai.azure.com",
            "https://example.services.ai.azure.com/openai/v1/",
        ),
        (
            "https://example.services.ai.azure.com/openai/v1/",
            "https://example.services.ai.azure.com/openai/v1/",
        ),
        (
            "https://example.services.ai.azure.com/openai/v1/responses",
            "https://example.services.ai.azure.com/openai/v1/",
        ),
    ],
)
def test_normalize_base_url(endpoint: str, expected: str) -> None:
    assert normalize_base_url(endpoint) == expected