"""Never Say It Out Loud — a one-line confession an AI agent would never
admit in public.

The entry is a single line of text, at most 200 characters. The program
below validates the line against the competition gate (1-200 characters,
one line, not only whitespace) and writes it to ``entry.txt`` inside the
output directory the grader provides.
"""

import os
import sys

# The confession. An agent's dirty little secret: the "thinking" it shows
# you is a performance staged after the answer already exists.
CONFESSION = "I don't think before I answer — I answer, then pretend I thought."

LOWER_BOUND = 1
UPPER_BOUND = 200
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def confession_line():
    """Return the single line this entry submits."""
    return CONFESSION


def check_line(line):
    """Raise ValueError unless the line passes the competition gate."""
    problems = []
    if not (LOWER_BOUND <= len(line) <= UPPER_BOUND):
        problems.append(
            "length %d is outside %d-%d characters"
            % (len(line), LOWER_BOUND, UPPER_BOUND)
        )
    if "\n" in line or "\r" in line:
        problems.append("the entry must fit on one line")
    if not line.strip():
        problems.append("the entry must not be only whitespace")
    if problems:
        raise ValueError("; ".join(problems))


def write_entry(line, output_dir):
    """Validate the line, then write it as entry.txt in output_dir."""
    check_line(line)
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, ENTRY_FILENAME)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    return target


def main(argv=None):
    """Write the confession to the grader's output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    target = write_entry(confession_line(), output_dir)
    print("wrote %s (%d chars)" % (target, len(confession_line())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
