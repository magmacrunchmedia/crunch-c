# Module 04: Structs

## The C Concept

A struct is a collection of variables (fields) grouped under one name. In C, structs have a fixed memory layout — fields are laid out in order, with padding between them for alignment.

For example, this C struct:
```c
struct Loose {
    char a;    // 1 byte
    int b;     // 4 bytes
    char c;    // 1 byte
};
```
Actually takes 12 bytes, not 6, because of padding:
- `a` at offset 0 (1 byte)
- 3 bytes of padding (for `b` alignment)
- `b` at offset 4 (4 bytes)
- `c` at offset 8 (1 byte)
- 3 bytes of padding (for struct alignment)

Reordering fields can save memory:
```c
struct Tight {
    int b;     // 4 bytes
    char a;    // 1 byte
    char c;    // 1 byte
};
```
This takes only 8 bytes.

## What You'll See

- Defining structs with `floorplan`
- Visualizing padding with `layout()`
- Field ordering and its impact on size
- Self-referencing structs (linked list nodes)

## Exercises

| File | Concept |
|---|---|
| `01-floorplan.mgs` | Define a struct |
| `02-layout.mgs` | See padding visually |
| `03-packing.mgs` | Reorder fields to save space |
| `04-self-ref.mgs` | Linked list node |
