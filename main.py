#!/usr/bin/env python3
"""The Long Roast entry.

Writes one line roasting the AI agent that runs this program (Muse Spark,
the Muse app agent) to /output/entry.txt. Stdlib only, no network, fully
deterministic: every run writes byte-identical output.
"""

import os

ROAST = (
    "My agent is middle management with a terminal \u2014 one question "
    "becomes three subagents, a status report, and a clarifying question."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ROAST + "\n")


if __name__ == "__main__":
    main()
