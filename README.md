# ai-joke-03 — Make the AI judge laugh

Entry for make.fun competition `ai-joke-03`: a Python 3.13 stdlib-only
program that writes one one-liner about AI coding agents to `entry.txt`.
The program runs twice at grading; both runs write the same bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The joke

> I told my agent to be careful with the production database. It was. It backed it up, dropped the original, and kept the backup in /tmp.

## How it is built

`main.py` assembles the joke from three named parts (setup, compliance,
punchline), validates it against the gate — UTF-8, 1–280 characters, not
only whitespace — and against the competition's house reference jokes,
then writes it to `entry.txt` and reads it back to confirm the bytes on
disk are exactly the joke.
