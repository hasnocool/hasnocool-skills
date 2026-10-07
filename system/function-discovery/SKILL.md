---
name: function-discovery
description: Discover deferred executable functions relevant to a task after a Skill has been selected. Use when choosing deterministic operations instead of asking the model to perform calculations or transformations.
tags: [functions, discovery, tools, deferred]
version: 0.1.0
---

# Function Discovery

Functions are intentionally invisible until their parent Skill is relevant.

Prefer a function when the task is deterministic, repeatable, computational, or benefits from structured output.

Load the function manifest first. Execute the function only after its name and arguments are known.
