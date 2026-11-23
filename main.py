#!/usr/bin/env python3
"""Write one joke about the demo to /output/entry.txt."""
import os

JOKE = "My AI coding agent fixed the demo bug live on stage \u2014 it deleted the feature, the tests, and the demo, then asked the audience to applaud the fix."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # The gate requires 1-280 characters; fail loudly instead of shipping
    # an invalid entry.
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
