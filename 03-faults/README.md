# Module 03: Memory Faults

## The C Concept

In C, memory errors are silent. Use-after-free, out-of-bounds access, double-free, memory leaks — they all produce undefined behavior. Sometimes crashes, sometimes security vulnerabilities, sometimes nothing at all.

In crunch-c, every memory fault is caught and named:

| Fault | C Equivalent | crunch-c Name |
|---|---|---|
| Use-after-free | Undefined behavior | `quicksand` |
| Out-of-bounds | Buffer overflow | `area does not exist` |
| Double-free | Undefined behavior | `quicksand` |
| Memory leak | Memory leak | `ancient weeds` |

## Exercises

| File | Concept |
|---|---|
| `01-quicksand.mgs` | Use-after-free |
| `02-out-of-bounds.mgs` | Buffer overflow |
| `03-double-free.mgs` | Double-free |
| `04-leaks.mgs` | Memory leaks |
