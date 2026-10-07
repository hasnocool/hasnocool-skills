# filename: system/skill-catalog/functions/validate_skill.py
import json
import sys
from pathlib import Path


def main() -> int:
    payload = json.load(sys.stdin)
    root = Path(payload["skill_dir"]).expanduser().resolve()
    skill_file = root / "SKILL.md"
    errors: list[str] = []

    if not skill_file.is_file():
        errors.append("missing SKILL.md")

    function_dir = root / "functions"
    if function_dir.is_dir():
        for manifest in function_dir.glob("*.json"):
            try:
                spec = json.loads(manifest.read_text(encoding="utf-8"))
                for key in ("name", "description", "command"):
                    if key not in spec:
                        errors.append(f"{manifest}: missing {key}")
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"{manifest}: {exc}")

    print(json.dumps({"ok": not errors, "skill": str(root), "errors": errors}))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
