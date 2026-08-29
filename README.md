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

## License

Apache-2.0
