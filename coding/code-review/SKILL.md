---
name: code-review
description: Review source code for correctness, maintainability, performance, concurrency, security, and regressions. Use when reviewing or auditing code.
tags: [coding, review, refactoring, performance, security]
version: 0.1.0
---

# Code Review

Review in this order:

1. Correctness and failure modes.
2. Blocking I/O and concurrency.
3. Resource usage.
4. Security boundaries.
5. API and compatibility risks.
6. Tests and observability.

Prefer concrete findings with file and line references and propose minimal fixes.
