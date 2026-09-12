# Chapter 4: Modules Should Be Deep

> *A Philosophy of Software Design — John Ousterhout*

---

## Goal of Modular Design

Decompose systems into independent modules so developers only face a fraction of the total complexity at any given time. Inter-module dependencies are inevitable (via method arguments and calls), but good modular design minimizes them so changes don't ripple across the system.

---

## Interface vs. Implementation

| Part | What It Is | Visible To |
|------|-----------|-----------|
| **Interface** | *What* the module does | Users of the module |
| **Implementation** | *How* it does it — the hidden complexity, sophisticated code, and algorithms | Module internals only |

The best modules have interfaces far simpler than their implementations, allowing internal changes without affecting other code.

### Anatomy of an Interface

| Element | Nature | Examples |
|---------|--------|---------|
| **Formal** | Explicitly specified and language-enforced | Signatures, parameter types, return values |
| **Informal** | Described via comments — often larger and more complex | High-level behavior, side effects, usage constraints |

---

## Abstraction

Simplifies complex entities by omitting unimportant details to reduce cognitive load.

**False Abstraction** occurs when:
- Critical details are omitted → leads to obscurity
- Unnecessary details are included → clutters the design

---

## Deep vs. Shallow Modules

| Type | Interface | Functionality | Result |
|------|-----------|--------------|--------|
| **Deep** ✅ | Small, simple | Massive | Hides complexity well — the ideal |
| **Shallow** ❌ | Complex relative to implementation | Limited | Adds cognitive load without structural benefit |

**Deep module examples:** Unix I/O system calls (`open`, `read`, `write`) and garbage collectors — powerful functionality behind a tiny interface.

**Shallow module red flag:** small methods/classes tend to be shallow and often make codebases worse rather than better.

### Classitis Anti-Pattern

Driven by the false dogma that *"small classes/methods are always better."* Results in massive complexity through an accumulation of tiny, shallow interfaces and excessive boilerplate.

---

## The Common Case Principle

Interfaces should make the **most frequent use case as simple as possible by default** (e.g., automatic buffering in file I/O). Advanced or rare configurations should be neatly separated so typical users can ignore them.

---

## Core Takeaway

> Deep modules are the cornerstone of clean software architecture — they hide heavy internal complexity behind simple interfaces for common operations.