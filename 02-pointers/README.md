# Module 02: Pointers

## The C Concept

A pointer is a variable that holds a memory address. In C, pointers are powerful but dangerous — you can dereference a null pointer, read freed memory, or walk off the end of an array.

In crunch-c, pointers are called `pine` (a play on "pointer" and "pine" — something that points upward). You allocate memory with `garrison` and free it with `scorch`.

## What You'll See

- Allocating memory: `garrison(n)` claims n bytes
- Reading/writing: `p[i]` for byte access, `p.peek(i32)` for typed access
- Pointer arithmetic: `p + 1` shifts the pointer forward
- Freeing memory: `scorch(p)` releases the block

## Exercises

| File | Concept |
|---|---|
| `01-garrison.mgs` | Allocate memory |
| `02-peek-poke.mgs` | Read and write typed values |
| `03-pine-arithmetic.mgs` | Shift pointers, iterate through blocks |
| `04-scorch.mgs` | Free memory and see what happens |
