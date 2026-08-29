# Module 06: Strings

## The C Concept

C has no string type. It has a convention.

A "string" in C is a block of bytes that happens to end with a zero. That zero
— the NUL terminator, written `'\0'` — is not a length, not a header, and not
stored anywhere separate. It is one byte of value 0 sitting in the data, and
every function that touches a string finds the end by walking forward until it
hits one.

```c
char name[6] = "hello";   // 5 letters and a terminator: 6 bytes, not 5
```

Everything follows from that:

- **`strlen` is a loop, not a lookup.** It walks until it finds the zero, so it
  costs time proportional to the length, and it has no idea how big the buffer
  actually is.
- **A missing terminator is not a short string. It is an unbounded read.**
  `strlen` keeps walking into whatever comes next until it happens to find a
  zero byte or the program dies.
- **Every buffer needs one more byte than its text.** The `+ 1` that C
  programmers write everywhere is room for the terminator, and forgetting it
  is the single most common bug in the language.

This is where C's memory model stops being an abstract concern. Unterminated
strings and undersized buffers are the mechanism behind a large share of the
security vulnerabilities of the last thirty years.

## Writing Text By Hand

crunch-c has no character literals, so you write bytes as decimal ASCII codes.
This is tedious on purpose — it keeps the fact that a string *is just bytes*
impossible to forget. Keep your words short.

```
 space 32      0-9  48-57
 A-Z   65-90   a-z  97-122
```

So `A` is 65, `H` is 72, and the terminator is plain `0`.

`bathysphere()` prints the ASCII alongside the hex, which is where this pays
off — you write `72 73 0` and the dump shows you `|HI.|`.

## What You'll See

- A string as a `u8` block ending in zero
- Writing `strlen` as a `while` loop over bytes
- What an unterminated string does to that loop
- `sizeof` vs `strlen`, and where the `+ 1` comes from
- A copy that overruns its buffer and silently rewrites the field next door

## Exercises

| File | Concept |
|---|---|
| `01-bytes-are-characters.mgs` | A string is bytes plus a zero |
| `02-strlen.mgs` | Walk to the terminator, then lose it |
| `03-off-by-one.mgs` | The `+ 1` that everyone forgets |
| `04-strcpy.mgs` | Overrun a buffer, corrupt a neighbour |
