# Module 05: Advanced

## The C Concept

Three ideas that only make sense once Modules 01–04 are behind you. Each one is
the same underlying fact wearing a different hat: memory is bytes, and a *type*
is a decision about how to read them.

### Casting

A cast tells the compiler to read a value as a different type. In C:

```c
int  x = 300;
char c = (char)x;    // keep the low 8 bits, discard the rest
float f = (float)x;  // convert the numeric value
```

Those two lines do genuinely different things. `(char)x` reinterprets — it
throws bytes away and keeps a bit pattern. `(float)x` converts — it computes a
new representation of the same number. C spells both with the same syntax,
which is a large part of why cast bugs are so common. The classic is
`(unsigned)-1`, which is not an error and not zero but the largest unsigned
value there is; the bits never moved, only the rule for reading them.

crunch-c writes this as `osmosis(value, type)`, and makes you write it. There
is no implicit promotion here, so a conversion you did not ask for cannot
happen silently.

### Fixed-size arrays

In C an array inside a struct is not a pointer to elements stored elsewhere —
it *is* the elements, laid out inline:

```c
struct Buffer {
    int data[4];   // 16 bytes, right here
    int length;    // at offset 16
};
```

There is no length stored anywhere, and no bounds check. `data[i]` means
"the address of `data`, plus `i` times four bytes" and nothing more. Which is
why `data[7]` is not an error in C — it is a perfectly well-formed instruction
to read memory that belongs to `length`, or to whatever sits past the end of
the struct.

Exercise 02 makes you do that arithmetic by hand, so the indexing syntax stops
being an abstraction.

### Binary protocols

Every network packet and file format is a struct someone agreed on in advance.
Parsing one means laying a floorplan over raw bytes and reading fields out at
known offsets — which is exactly what Module 04 was about, applied to bytes you
did not write yourself.

Two things bite here, and both are already familiar: **endianness** (the byte
order from Module 02 — a `u16` magic number of `0x4D47` sits in memory as
`47 4D` on a little-endian machine) and **padding** (the alignment rules from
Module 04 — a header that reads like 8 bytes of fields may occupy 12, and a
parser that assumed 8 will misread every field after the gap).

The header in Exercise 03 is genuinely 8 bytes with no padding at all, but not
by accident: `u16, u8, u8, u32` happens to fill each alignment boundary exactly
as it goes. Run `layout()` on it and confirm that before you trust it. Then try
reordering the fields and watch a wire format that no longer matches the wire.

Real C code fights this with `#pragma pack` or by reading fields one at a time.
The bug it prevents is the kind that only appears on the other machine.

## What You'll See

- Explicit conversion with `osmosis()`, and truncation as bit-discarding
- Two's complement: why `-1` cast to unsigned is the maximum value
- Array fields in a `floorplan`, indexed by hand
- What an out-of-bounds index does when it lands *inside* the same block
- Laying a header over bytes and reading it back with `bathysphere()`

## Exercises

| File | Concept |
|---|---|
| `01-osmosis.mgs` | Explicit type conversion |
| `02-arrays.mgs` | Fixed-size arrays in floorplans |
| `03-binary-protocol.mgs` | Parse a binary format |
