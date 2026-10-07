# hasnocool Skills

An independently versioned Skill catalog for the Skill Function Agent System.

This repository contains **Skills and their executable functions only**. Runtime/orchestration code belongs in [hasnocool/skill-function-agent-system](https://github.com/hasnocool/skill-function-agent-system).

## Layout

- system/ - meta-skills for operating and maintaining the catalog
- coding/ - software development skills
- trading/ - quantitative/trading skills
- ai/ - AI/agent skills
- linux/ - Linux/system skills
- game-dev/ - game-development skills

Every Skill has a small SKILL.md frontmatter block. Heavy references and executable functions are loaded only when needed.

## Skill contract

A Skill contains:

    SKILL.md
    references/       optional
    functions/        optional

Function manifests are JSON files under functions/. Their command points to an executable function in the same Skill directory.
