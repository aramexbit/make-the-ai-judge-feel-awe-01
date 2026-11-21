"""Entry program: writes one short text to entry.txt.

Deterministic, stdlib only, no network, no randomness, no file reads.
"""

import os

TEXT = (
    "On the sill, the tea has gone cool. The steam thins and stops. "
    "Outside, the roofs give back the last light, one by one, and the sky "
    "turns slate. The first stars come out, and there is time to count them. "
    "Each burned longer than every word you have ever read.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
