#!/usr/bin/env python3
"""Run every .mgs file in the course and check its exit code.

Nothing else in this repo executes the lessons, so a lesson that stops running
is invisible until someone opens it. This is the guard against that.

Most files are expected to exit 0. The handful that end by deliberately
triggering a fault are listed in tools/expected.txt with the code they should
exit with -- for those, exiting 0 is the failure.

    python tools/check.py            # check everything
    python tools/check.py -v         # also print output of failing files
    python tools/check.py --update   # rewrite expected.txt from what runs now
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "tools" / "expected.txt"


def lesson_files() -> list[pathlib.Path]:
    """Every exercise and solution, in course order."""
    found = []
    for path in sorted(ROOT.glob("0*/*.mgs")) + sorted(ROOT.glob("solutions/0*/*.mgs")):
        # macOS AppleDouble sidecars are not lessons.
        if path.name.startswith("._"):
            continue
        found.append(path)
    return found


def load_expected() -> dict[str, int]:
    expected = {}
    if not MANIFEST.exists():
        return expected
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        path, _, code = line.rpartition(" ")
        expected[path.strip()] = int(code)
    return expected


def run(path: pathlib.Path) -> tuple[int, str]:
    proc = subprocess.run(
        ["magmascript", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="print the output of files that fail")
    ap.add_argument("--update", action="store_true",
                    help="rewrite expected.txt from current behaviour")
    args = ap.parse_args()

    files = lesson_files()
    if not files:
        print("no .mgs files found -- wrong directory?", file=sys.stderr)
        return 2

    expected = load_expected()
    failures = []
    observed = {}

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        want = expected.get(rel, 0)
        got, output = run(path)
        observed[rel] = got

        if got == want:
            print(f"  ok    {rel}" + (f"  (exit {got}, as intended)" if want else ""))
        else:
            print(f"  FAIL  {rel}  expected exit {want}, got {got}")
            failures.append((rel, want, got, output))

    if args.update:
        write_manifest(observed)
        print(f"\nwrote {MANIFEST.relative_to(ROOT).as_posix()}")
        return 0

    print()
    if failures:
        print(f"{len(failures)} of {len(files)} lessons failed:\n")
        for rel, want, got, output in failures:
            print(f"  {rel}: expected {want}, got {got}")
            if args.verbose:
                for line in output.strip().splitlines()[-12:]:
                    print(f"      | {line}")
        print("\nIf a change to the lessons made this intentional, re-run with")
        print("--update and commit the new tools/expected.txt.")
        return 1

    print(f"all {len(files)} lessons behave as expected.")
    return 0


def write_manifest(observed: dict[str, int]) -> None:
    header = MANIFEST.read_text(encoding="utf-8").split("\n\n", 1)[0] if MANIFEST.exists() else ""
    lines = [f"{rel:<46} {code}" for rel, code in sorted(observed.items()) if code != 0]
    body = header + "\n\n" + "\n".join(lines) + "\n"
    MANIFEST.write_text(body, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    sys.exit(main())
