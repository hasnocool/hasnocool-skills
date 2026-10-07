---
name: skill-catalog
description: Maintain, inspect, validate, index, and organize the external Skill catalog. Use when adding, restructuring, validating, or documenting Skills.
tags: [skills, catalog, registry, maintenance]
version: 0.1.0
---

# Skill Catalog

Keep each Skill independently useful and discoverable.

## Rules

- Keep SKILL.md concise.
- Put large knowledge into references/.
- Put deterministic operations into functions/.
- Give every function a JSON manifest.
- Use descriptive names and trigger-oriented descriptions.
- Do not put runtime/orchestration code in this repository.

## Validation

Check frontmatter, directory structure, function manifests, executable paths, and JSON validity before publishing a Skill.
