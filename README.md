# crunch-c

Learn C memory management without segfaults.

`crunch-c` teaches C concepts (pointers, structs, memory allocation, overflow) using [magmascript](https://github.com/magmacrunchmedia/magmascript)'s asthenosphere. Every memory error is caught and explained. No segfaults. No undefined behavior. Just C's behavior, narrated.

## What You'll Learn

| Module | C Concept | Asthenosphere Feature |
|---|---|---|
| 01 Types | Fixed-width integers, overflow, truncation | `i32`, `u8`, `f32`, wrapping |
| 02 Pointers | Memory addresses, allocation, dereferencing | `pine`, `garrison`, `scorch` |
| 03 Faults | Use-after-free, out-of-bounds, leaks | `quicksand`, `area does not exist`, `ancient weeds` |
| 04 Structs | Memory layout, padding, alignment | `floorplan`, `layout()`, `sizeof` |
| 05 Advanced | Type casting, arrays, binary protocols | `osmosis()`, arrays in floorplans |

## Scope

This teaches C's *memory model*: how values are sized, how the heap is
allocated and freed, how structs are laid out, and how the classic memory bugs
actually happen. Work through all 18 exercises and you will read C memory code
with real understanding.

It does not teach you to write and compile a C program. There is no `main()`,
no `#include`, no compiler, no linker. Also deliberately out of scope for now:
strings and NUL-termination, `calloc`/`realloc`, unions, bitwise operators, the
preprocessor, and the stack (every allocation here is heap).

When you leave the sandbox, the arena's job is done by real tools, and they are
worth meeting early:

- **AddressSanitizer** (`gcc -fsanitize=address -g`) reports use-after-free,
  out-of-bounds and leaks -- the whole of Module 03.
- **UndefinedBehaviorSanitizer** (`-fsanitize=undefined`) catches the signed
  overflow from Module 01.
- **Valgrind** (`valgrind --leak-check=full`) finds leaks in a binary you
  cannot rebuild.
- **`-Wall -Wextra`** catches a surprising share of this before you run
  anything.

Every "spooked", "quicksand" and "ancient weeds" message in this course is
something one of those four would have told you. The difference is that in C
nobody turns them on for you.

## Prerequisites

- Basic programming knowledge (any language)
- Python 3.10+
- magmascript installed (`pip install magmascript`)

## Quick Start

```bash
pip install magmascript
git clone https://github.com/magmacrunchmedia/crunch-c.git
cd crunch-c
magmascript repl
```

Then open any `.mgs` file and run it:

```bash
magmascript 01-types/01-widths.mgs
```

## How It Works

In C, memory mistakes cause segfaults, crashes, and security vulnerabilities. In crunch-c, the same mistakes are caught with clear error messages:

```
quicksand: tried to read scorched memory at line 12
  block was scorched at line 8
```

You learn what C does, and why it's dangerous, without the danger.

## Playground

Work through the whole course in your browser, no install required:
**[magmacrunch.com/ware/crunch-c](https://magmacrunch.com/ware/crunch-c/)**

Each lesson pairs the explanation with a live editor, so you can uncomment the
dangerous lines and watch the fault land.

## Solutions

Every exercise has a worked answer under `solutions/`, mirroring the module
layout:

```bash
magmascript solutions/03-faults/01-quicksand.mgs
```

Solutions for modules 02, 03 and 05 end by deliberately triggering the fault
they teach, so they exit non-zero on purpose. That is the lesson, not a
failure.

## Checking The Lessons

`tools/check.py` runs all 36 exercises and solutions and compares each exit
code against `tools/expected.txt`:

```bash
python tools/check.py
```

Files that are supposed to fault must still fault -- if one of them starts
exiting cleanly, that is a failure too. Run it after editing any lesson. CI
runs it on every push and pull request.

## License

Apache-2.0
