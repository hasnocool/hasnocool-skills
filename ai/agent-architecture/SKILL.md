---
name: agent-architecture
description: Design scalable AI agent systems using Skills, deferred functions, progressive disclosure, tool discovery, memory, routing, and asynchronous execution.
tags: [ai, agents, architecture, tools, skills]
version: 0.1.0
---

# Agent Architecture

Separate knowledge from execution.

- Skills describe workflows and domain knowledge.
- Functions perform deterministic operations.
- References hold large material.
- The runtime owns discovery, loading, execution, caching, and policy.
- Keep model context proportional to the current task rather than the total capability catalog.
