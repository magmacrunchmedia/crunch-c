# Module 01: Types

## The C Concept

In C, the `<stdint.h>` types have fixed sizes. A `uint8_t` can only hold 0–255. An `int32_t` can hold roughly -2 billion to +2 billion. (Plain `int` and `long` are the ones that are *not* fixed — their widths are implementation-defined, which is exactly why portable code reaches for the `uint8_t`/`int32_t` names.)

What happens when you exceed the range depends on the sign, and the difference matters more than it looks:

- **Unsigned types wrap**, silently and by guarantee. `uint8_t` 255 + 1 is 0. The standard says so, and you can rely on it.
- **Signed overflow is undefined behavior.** Not a wrap, not a promise of anything. The compiler is entitled to assume it never happens and optimise on that basis, so the symptom can be code that vanished rather than a wrong number.

Both are among the most common sources of bugs in C programs. The signed one is the more dangerous, because testing it on your machine tells you nothing about what it does on someone else's.

C also has implicit type promotion: when you add an `int` and a `char`, the `char` is silently promoted to `int`. This is well-defined but confusing, and it's one of C's worst-understood corners.

## What You'll See

- Fixed-width integers (`i8`, `u16`, `i32`, etc.) and their ranges
- Wrapping behavior: what happens when `u8` goes above 255
- Signed underflow: what happens when `i8` drops below -128
- Truncating division: `-7 / 2` is `-3`, not `-4`
- No integer promotion: `i32 + u8` is an error, not silent promotion

### Where crunch-c differs from C

Two deliberate divergences, both worth holding onto:

- **crunch-c wraps *and warns* on signed overflow too.** Real C gives you
  undefined behavior with no warning at all. The sandbox shows you the shape of
  the bug; C would show you nothing, or something worse.
- **crunch-c has no integer promotion.** `i32 + u8` is an error here, where C
  would quietly promote and carry on. This is the course refusing to hide a
  conversion from you, not a claim about how C behaves.

## Exercises

| File | Concept |
|---|---|
| `01-widths.mgs` | See how different widths hold different ranges |
| `02-overflow.mgs` | Watch a `u8` wrap from 255 to 0 |
| `03-division.mgs` | Truncating vs floor division |
