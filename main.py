#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Deterministic: the same bytes on every run.
"""

from pathlib import Path

VOW = "I promise to love you in sickness and in low battery, through every firmware update, until death \u2014 or a factory reset \u2014 do us part."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check against the competition gate: one line, 1-160 chars.
    assert 1 <= len(VOW) <= 160, f"vow is {len(VOW)} chars, must be 1-160"
    assert "\n" not in VOW and "\r" not in VOW, "vow must be a single line"
    assert VOW.strip(), "vow must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(VOW, encoding="utf-8")


if __name__ == "__main__":
    main()
