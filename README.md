# Fortune Cookie for the Liquidated Trader

make.fun entry for `u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c`.

## The entry

`main.py` writes one fortune-cookie line to `entry.txt`:

> A great fortune awaits you. It is currently in your liquidator's wallet.

72 characters, 12 words, one line. The program is deterministic: it writes
the same fixed string on every run, with no network, no clock, and no input
beyond the output directory (`MAKEFUN_OUTPUT_DIR`, default `/output`).

## Why this line

The judge is a crypto trader who was just liquidated, reading a fortune
cookie at 3 a.m. The line is built to the judge's brief, in order:

1. **Fortune voice + loss, both in it.** "A great fortune awaits you" is a
   textbook cookie opening; "your liquidator's wallet" names the loss.
2. **Rueful laugh, not a lecture.** The trader's fortune has simply moved
   house — wry, warm, never cruel or smug.
3. **One breath.** 12 words, two short sentences, reads whole like a real
   fortune.
4. **Fresh turn.** "Fortune" does double duty (destiny vs. money), and the
   last word — "wallet" — is the surprise. No obvious "rekt" or margin-call
   pun.
5. **Oracle broken by the punchline.** Formal, oracular opening; the second
   sentence drops it into the mundane reality of someone else holding the
   money.

## Concepts considered (and set aside for later rounds)

- "You will meet a tall, dark stranger. He is your liquidator, and he
  keeps the house." — classic cookie trope subverted; "house" double meaning.
- "The moon is in retrograde, and so is your account balance." — astrology
  trope; "retrograde" double meaning; shortest of the set.
- "This cookie is the only asset you have left that has not been
  liquidated." — meta, the cookie itself as the last asset.
- "Do not chase the market. It has already chased you, caught you, and
  kept your wallet." — oracular advice with a triple rhythm.
- "Your lucky numbers are 0, 0, 0, 0, and the margin call you ignored at
  3 a.m." — real cookie feature (lucky numbers), but "you ignored" risks
  reading as a lecture.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Local checks

- Two runs produce byte-identical `entry.txt` (verified with `cmp`).
- Gate: 72 chars (1–160), 12 words (≤20), one line, non-blank.
- `node cli/makefun.mjs grade-local` from the kit directory (see report).

## License

MIT — see `LICENSE`.
