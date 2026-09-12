# Chapter 3: Working Code Isn't Enough — Strategic vs. Tactical Programming

> *A Philosophy of Software Design — John Ousterhout*

---

## The Fallacy of "Working Code"

Working code is only a baseline. If it introduces unnecessary complexity, the design fails in the long run.

---

## The Real Goal of Strategic Programming

Most software is built by extending existing code. Therefore, the developer's most important job is not merely to make the current task work — it's to maintain a system structure that makes **future changes easier**.

---

## Tactical Programming

Focusing only on deadlines leads to:
- Short-sighted shortcuts
- Incremental complexity with every feature
- Quick patches instead of real fixes
- Unmaintainable legacy code and permanent technical debt

**The "Tactical Tornado":** a high-output developer who writes code rapidly but leaves structural chaos behind, shifting the cleanup burden onto the rest of the team.

---

## Technical Debt

Tactical programming is like borrowing time from the future:
- Development is faster now.
- Development becomes slower later as complexity accumulates.
- The long-term cost often exceeds the short-term time saved.
- Most technical debt is never fully repaid — it continues to cost the team over time.

---

## Strategic Programming

Treat software development as an **investment**. Prioritize long-term system structure and maintainability over short-term speed.

### Investment Types

| Type | Examples |
|------|---------|
| **Proactive** | Take extra time to explore alternative designs, choose the simplest one, think about likely future changes, write good documentation |
| **Reactive** | Fix design flaws as soon as they're discovered — rather than patching around them |

### The Cost and Payoff

- Requires roughly a **10–20% time investment** upfront.
- Ousterhout suggests the payback period is roughly **6–18 months** — but explicitly notes this is his personal opinion, not an empirically established figure.

---

## Strategic Does Not Mean Big Upfront Design

Strategic programming does **not** mean designing the entire system in advance. Instead, make **small, continuous investments** in design as you learn more about the system. This connects directly to the incremental development approach from Chapter 1.

---

## Strategic Programming Requires Judgment

Strategic programming does not mean rejecting every quick fix. Under real constraints, a tactical compromise may sometimes be necessary. The goal is to resist such compromises when possible and avoid making them the default approach.

**Example:** if a proper refactor would take three months but a quick fix takes two hours under a real deadline, the quick fix may be reasonable. The danger is when tactical thinking becomes the habit, not the exception.

---

## Startups and Investment

Startups may feel pressure to prioritize speed over design, but tactical programming can make the codebase increasingly difficult to fix later. A messy codebase also makes it harder to attract strong engineers — good developers care about design quality.

---

## Engineering Quality and Talent

Clean architectures attract top-tier engineering talent, which dramatically lowers long-term development costs compared to chaotic, hard-to-maintain codebases.