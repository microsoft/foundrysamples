---
title: Send a Multimodal Request
description: Contributor guide for sending text and an image to a Foundry model
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Send a text instruction and an image in one request, while validating image
type, size, and source before data crosses the service boundary.

## What to build

* A runnable `multimodal_request.py` example
* One small, redistributable sample image with attribution when required
* Support for a local image and a documented remote-image alternative
* Deterministic tests for request construction and invalid image input

## Acceptance criteria

* The chosen deployment is documented as vision capable
* Unsupported formats and oversized files fail before the model call
* Image data and credentials are not logged
* The expected response and accessibility-oriented image description are shown
* Tests make no network requests; any live test is explicitly marked

## Contribution notes

Do not commit customer images, screenshots containing personal data, or large
binary assets. Keep image encoding and message construction visible in the
sample, and document token and image-processing costs.

## References

* [Azure OpenAI vision-enabled chat](https://learn.microsoft.com/azure/foundry/openai/how-to/gpt-with-vision)
* [OpenAI Python image input examples](https://github.com/openai/openai-python#vision)