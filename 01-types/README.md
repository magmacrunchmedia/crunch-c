# Module 01: Types

## The C Concept

In C, integers have fixed sizes. A `uint8_t` can only hold 0–255. A `int32_t` can hold roughly -2 billion to +2 billion. When you exceed the range, the value **wraps around** — silently. This is one of the most common sources of bugs in C programs.

C also has implicit type promotion: when you add an `int` and a `char`, the `char` is silently promoted to `int`. This is well-defined but confusing, and it's one of C's worst-understood corners.

## What You'll See

- Fixed-width integers (`i8`, `u16`, `i32`, etc.) and their ranges
- Wrapping behavior: what happens when `u8` goes above 255
- Truncating division: `-7 / 2` is `-3`, not `-4`
- No integer promotion: `i32 + u8` is an error, not silent promotion

## Exercises

| File | Concept |
|---|---|
| `01-widths.mgs` | See how different widths hold different ranges |
| `02-overflow.mgs` | Watch a `u8` wrap from 255 to 0 |
| `03-division.mgs` | Truncating vs floor division |
