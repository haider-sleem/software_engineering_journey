# Chapter 1: The Essential Software Requirement

> *Software Requirements, 3rd Edition — Karl Wiegers & Joy Beatty*

---

## Why Requirements Matter

- Most software problems originate from poor requirements.
- Requirements errors account for a large percentage of software defects.
- Early requirements defects are much cheaper to fix than late defects.
- Good requirements are an investment, not a cost — they reduce rework, cost, risk, and project chaos.
- There are no shortcuts to good requirements engineering.

---

## What Is a Requirement?

- A requirement can describe behavior, a property, an attribute, or a constraint.
- Requirements represent both the user's and the developer's perspectives.
- Requirements can be current, future, deferred, or even discarded — deferred requirements are still requirements.
- Do not confuse the dictionary meaning of "requirement" with its software engineering usage.
- Every requirement should be explicit, clear, and testable.

---

## Terminology and Communication

- Different stakeholders often use the term "requirement" differently — agree on common terminology before any discussion begins.
- A shared glossary reduces misunderstandings across the project team.
- Clear communication reduces ambiguity and expectation gaps.
- Document requirements; do not rely on conversations or memory.

---

## Types of Requirements

| Type | Purpose |
|------|---------|
| **Business Requirements** | Explain *why* the product is needed — the business goal |
| **User Requirements** | Describe *what* users need to accomplish |
| **Functional Requirements** | Define *how* the system should behave |
| **Nonfunctional Requirements** | Define quality attributes and constraints |
| **Business Rules** | Not requirements themselves, but often generate functional requirements |
| **Transition Requirements** | Essential for successful system migration |

- Features provide user value and are supported by functional requirements.
- Functional Requirements support User Requirements, which in turn support Business Requirements.
- The SRS documents the expected behavior of the software.
- A system may include software, hardware, people, and processes.
- Use Cases and User Stories are common ways to represent User Requirements.

---

## Requirements Hierarchy

```
Business Needs
    └── Business Requirements  (why)
            └── User Requirements  (what)
                    └── Functional Requirements  (how)
```

- Start from business goals before defining system behavior.
- Every feature and user requirement should support a business objective.
- Every new requirement should be evaluated against the project scope.

---

## Stakeholders

- Requirements are the intersection point of all stakeholders.
- Different stakeholders participate at different requirement levels.
- Every important stakeholder should have a voice.
- Maintenance and support teams also have requirements.
- User involvement and customer involvement are critical to project success and reduce expectation gaps.
- Developers implement functional and nonfunctional requirements.
- Testers verify that requirements are correctly implemented.

---

## Requirements Engineering

Requirements Engineering consists of two distinct activities:

**Requirements Development**
- Elicitation → Analysis → Specification → Validation

**Requirements Management**
- Baselines, traceability, and change control
- Use impact analysis before accepting requirement changes

> Product Requirements are different from Project Requirements. Requirements development is iterative, not strictly linear.

---

## Common Pitfalls to Avoid

- **Ambiguity** — unclear requirements lead to different interpretations.
- **Scope creep** — accepting requirements that don't support a business objective.
- **Gold plating** — implementing features beyond what was required.
- **Tribal knowledge** — requirements kept in people's heads, not documented.
- Small projects may combine requirement documents, but the information types remain distinct.

---

## Key Takeaways

- Good requirements improve both product quality and project success.
- Clear requirements simplify testing and reduce rework and project risk.
- Requirements Engineering improves product quality and stakeholder satisfaction.
- Continuous improvement of requirements practices benefits the entire project team.
- Focus on user goals before implementing features.
- Maintain traceability across all requirement levels.