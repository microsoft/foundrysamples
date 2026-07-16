---
title: Run Quality and Safety Evaluations
description: Contributor guide for measuring relevance, groundedness, safety, and task success
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Run repeatable evaluations against the versioned dataset, report per-metric
results, and enforce documented quality gates without hiding failed cases.

## What to build

* An evaluation runner using `azure-ai-evaluation`
* Relevance, groundedness, safety, and deterministic task-success metrics
* Machine-readable results plus a concise terminal summary
* Tests for dataset mapping, aggregation, thresholds, and failed evaluators

## Acceptance criteria

* Evaluator and target model deployments are explicit configuration
* Thresholds include rationale and do not average away critical safety failures
* Results retain case identifiers for investigation
* Live evaluation cost and data handling are documented
* A local test path validates orchestration without model calls

## Contribution notes

Pin evaluator versions because scores can change across releases. Keep generated
results out of source control unless they are intentional reviewed baselines, and
record enough metadata to reproduce a run.

## References

* [Azure AI Evaluation SDK](https://learn.microsoft.com/azure/ai-foundry/how-to/develop/evaluate-sdk)
* [Azure AI evaluation metrics](https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-metrics-built-in)