# Module 02: Pointers

## The C Concept

A pointer is a variable that holds a memory address. In C, pointers are powerful but dangerous — you can dereference a null pointer, read freed memory, or walk off the end of an array.

In crunch-c, pointers are called `pine` (a play on "pointer" and "pine" — something that points upward). You allocate memory with `garrison` and free it with `scorch`.

## What You'll See

- Allocating memory: `garrison(n)` claims n bytes
- Reading/writing: `p[i]` for byte access, `p.peek(i32)` for typed access
- Pointer arithmetic: `p + 1` shifts the pointer forward
- Freeing memory: `scorch(p)` releases the block

## Two Tools For Looking At Memory

The course uses both of these from here on, so meet them now.

### `bathysphere(p)` — dump the raw bytes

`bathysphere` prints a block exactly as it sits in memory, with no
interpretation: a header line describing the block, then a hex dump.

```
pine 0x0008 (4 bytes, alive, garrisoned at line 11)
  0008  e8 03 00 00                                         |....|
```

Reading that: the block lives at address `0x0008`, it is 4 bytes long, it has
not been scorched yet, and it was allocated at line 11. Then the dump — offset
on the left, the bytes in hex, and the same bytes as printable characters on
the right (a `.` stands in for anything unprintable).

This is the tool that makes the invisible visible. `peek(i32)` tells you a
block holds 1000; `bathysphere` shows you it holds `e8 03 00 00`, which is
where endianness stops being a word and starts being something you can see.

### `.arena` — list every live block

`.arena` is a REPL command, not a function, so it works inside
`magmascript repl` rather than in a `.mgs` file. Run some code, then type
`.arena`, and you get every block still allocated: where it lives, how big it
is, and which line garrisoned it.

That last column is what makes it useful. When the run ends with an
ancient-weeds warning about a leak, `.arena` is how you find out what is still
holding memory and where it came from.

## A Note On `while`

From Exercise 03 onward the exercises loop:

```
i = 0
while i < 4 {
    print(f"i = {i}")
    i = i + 1
}
```

If you have written a loop in any other language this is the shape you expect,
minus the parentheses around the condition.

crunch-c does have `for` (`for i in range(4) { ... }`), and it is the nicer
loop. The exercises use `while` anyway, on purpose: walking memory means
holding an index you increment yourself and choosing when to stop, and that is
what a `for` hides. C's own `for` is shorthand for exactly the setup-test-
increment above. Write the long form a few times and the shorthand stops being
magic.

## Exercises

| File | Concept |
|---|---|
| `01-garrison.mgs` | Allocate memory |
| `02-peek-poke.mgs` | Read and write typed values |
| `03-pine-arithmetic.mgs` | Shift pointers, iterate through blocks |
| `04-scorch.mgs` | Free memory and see what happens |
