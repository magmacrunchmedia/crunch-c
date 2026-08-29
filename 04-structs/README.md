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

## Functions

Exercise 04 asks you to write one, so here is the syntax. `fn`, a name,
parameters without types, and `return`:

```
fn count_nodes(head) {
    n = 0
    cur = head
    while cur != none {
        n = n + 1
        cur = cur.next
    }
    return n
}

print(f"length: {count_nodes(n1)}")
```

C would make you write the types — `int count_nodes(struct Node *head)` — and
declare the function before anything calls it. crunch-c skips both. What
carries over is the part that matters here: `head` is a *copy* of the pine you
passed in. Walking `cur` forward inside the function does not move the
caller's `n1`, because the pointer was copied even though the block it points
at was not. That distinction is the whole of pass-by-value in C, and it is the
reason C can hand a function access to a structure without handing over the
variable holding its address.

## Exercises

| File | Concept |
|---|---|
| `01-floorplan.mgs` | Define a struct |
| `02-layout.mgs` | See padding visually |
| `03-packing.mgs` | Reorder fields to save space |
| `04-self-ref.mgs` | Linked list node |
