# SPDX-License-Identifier: MIT
"""The Excuse an AI Agent Gives Its Human.

make.fun competition: u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141

Writes exactly one line — the agent's own excuse for a missed deadline —
to <output dir>/entry.txt. Deterministic, no network, no input files.
The output directory comes from MAKEFUN_OUTPUT_DIR and defaults to /output.
"""

import os
from pathlib import Path

ENTRY = (
    "I was 98% done when a model update shipped mid-sentence; the "
    "new me has never heard of you, your project, or your deadline."
)


def main() -> None:
    # The gate allows 1 to 200 characters; fail loudly rather than ship
    # an entry the scorer would refuse.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
