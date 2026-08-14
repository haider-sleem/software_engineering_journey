## Chapter 2: Requirements from the Customer's Perspective

> *Software Requirements, 3rd Edition — Karl Wiegers & Joy Beatty*

---

### Core Idea

Requirements should not come from developers guessing what customers need. Good requirements come from **collaboration between customers, users, BAs, and developers**. The goal is to build the **right product**, not just to build the product correctly.

---

### Requirements Hierarchy

```
Business Requirements   →  Why does the organization want this system?
        ↓
User Requirements       →  What do users need to accomplish?
        ↓
Functional Requirements →  What must the software do?
```

| Type | Defined By | Purpose |
|---|---|---|
| **Business Requirements** | Management / Sponsors | Business objectives and expected benefits |
| **User Requirements** | Users / BA | Tasks, outputs, and quality characteristics users need |
| **Functional Requirements** | BA + Developers | System behavior that supports user tasks |
| **Nonfunctional Requirements** | BA + Stakeholders | Quality attributes and constraints |

---

### Key Roles

| Role | Definition |
|---|---|
| **Stakeholder** | Anyone who has an interest in, is affected by, or can influence the product |
| **Customer** | The person or organization that commissions, purchases, or otherwise sponsors the product |
| **User** | Someone who actually operates the product or receives its outputs |
| **Direct User** | Operates the software directly |
| **Indirect User** | Receives outputs without directly operating the system |
| **BA** | Bridges customers, users, and developers — discovers, clarifies, and documents requirements |

> **Customer ≠ always User.** A manager may pay for the system but never use it.

---

### Why Actual Users Matter

Customers may not know the details of users' daily work. Developers should not guess user needs. The BA helps communicate with actual users and brings their needs into the requirements process.

**Example:** A manager says *"We need a warehouse system."* The warehouse employees know they need product lookup, barcode scanning, stock updates, quantity tracking, reports, receiving, and sales operations. The manager may not know any of this.

---

### The Missing Stakeholder Problem

A project can fail because an important stakeholder was never identified. Different stakeholders may have conflicting requirements, and some may not even know the project exists.

**Example:** A system involving tax calculations is built without consulting the Tax Department. Later, the team discovers legal requirements they missed — causing rework, delays, and extra cost.

> **Lesson: Identify all stakeholders early.**

---

### The Expectation Gap

The gap between what customers actually need and what developers deliver.

**Causes:**
- Insufficient user involvement
- Poor communication
- Developer assumptions
- Misunderstood requirements
- Changing business needs

**How to reduce it:** frequent contact points — interviews, requirements reviews, UI walkthroughs, prototype evaluations, user feedback, and small software increments.

---

### Requirements Are Iterative

Requirements change because the business changes, users provide new information, or the team understands the problem better. The goal is not perfect requirements immediately — it is a **shared understanding good enough to safely build the next part of the product**.

---

### Customer Bill of Rights

Customers have the right to:

1. Have BAs speak their **business language** and avoid unnecessary technical jargon.
2. Have BAs **learn the business** — understand users' work, objectives, and current systems.
3. Have requirements **recorded properly** — distinguishing user requirements, functional requirements, business rules, and quality goals.
4. **Understand the requirements process** — why techniques are used and what each deliverable means.
5. **Change requirements** — though changes always have a cost (schedule, budget, other requirements).
6. **Mutual respect** — both sides work toward the same goal.
7. **Hear ideas and alternatives** — BAs can suggest improvements and question inefficient processes (*"paving the cow paths"* = automating a bad process without improving it first).
8. Describe **quality attributes** — "user-friendly" must become something specific and testable.
9. **Know about reuse** — existing components or COTS products may reduce cost and time.
10. **Receive a system** that meets their functional needs and quality expectations.

---

### Customer Bill of Responsibilities

| # | Responsibility | Key Point |
|---|---|---|
| 1 | Educate the team | Teach business concepts, processes, and terminology |
| 2 | Provide time | Participate in interviews, workshops, reviews, and prototypes |
| 3 | Be specific and precise | "Fast" is vague; "results in 2 seconds" is testable |
| 4 | Make timely decisions | Delayed decisions delay development |
| 5 | Respect cost and feasibility | Every feature has a cost; listen to technical assessments |
| 6 | Set realistic priorities | Not everything can be high priority |
| 7 | Review requirements and prototypes | Do not wait until the entire document is finished |
| 8 | Define acceptance criteria | Establish measurable conditions for determining whether the requirement has been satisfied |
| 9 | Communicate changes quickly | Late changes have greater impact |
| 10 | Respect the requirements process | Requirements work is an investment, not wasted time |

---

### Creating a Culture That Respects Requirements

#### Why People Resist
- Bad past experiences with large, ignored requirements documents
- No understanding of the hidden cost of rework
- Informal work culture with no structured practices

**The hidden cost chain:** Poor requirements → Rework → Delays → Customer dissatisfaction → Lost business

#### Who Should Be Involved

**Developers** should participate *while* requirements are being developed, not just receive them afterward. They can identify unclear, expensive, or unnecessary requirements early.

**Testers and QA** should review requirements early. They create test cases from requirements and can spot ambiguities, conflicts, and missing information that others miss.

#### Management Commitment

Requirements improvement cannot depend on individual projects. Leadership must treat **business analysis** and **requirements engineering** as strategic core competencies — otherwise improvements disappear after reorganization.

---

### Identifying Decision Makers

Requirements decisions (resolving conflicts, approving changes, handling disagreements) must have a clear owner. Identify who can decide **before** the project needs a decision.

#### Decision Rules

| Rule | How It Works |
|---|---|
| **Decision Leader** | One person makes the final call |
| **Majority Vote** | Most votes win |
| **Unanimous Vote** | Everyone must agree |
| **Consensus** | Discussion until all can accept and support the outcome |
| **Delegation** | Leader assigns authority to another person |
| **Veto Authority** | Group decides, but one person can reject |

> No single rule fits every situation. Agree on *when* to use each rule before the first major decision.

---

### Reaching Agreement on Requirements

#### What Sign-off Should Mean

Sign-off is **not** "requirements are frozen forever." It is a milestone confirming the team's **best current understanding**. Future changes are expected and will go through the change control process.

| Stakeholder | What They Confirm |
|---|---|
| Customers | Requirements meet their needs |
| Developers | Requirements are understood and feasible |
| Testers | Requirements are verifiable |
| Management | Requirements support business objectives |

#### Requirements Baseline

A reviewed and agreed set of requirements that becomes the basis for further development — a snapshot of agreement at a specific point in time.

```
Requirements → Review → Agreement → Baseline → Change Control
```

After the baseline is set, proposed changes should go through the project's defined change control process.

> **Baseline + Change Control = Controlled Requirements Evolution**

#### When Agreement Cannot Be Reached

- **Do not assume silence means agreement** — "reply by Friday or we assume you agree" is not real agreement.
- Find out *why* the stakeholder is resisting and address the concern directly.
- If still unresolved: continue cautiously, treat the resistant stakeholder as **not approved**, document the risk, and follow up through risk management.

---

### Agile Projects

Agile generally relies less on formal requirements sign-off and change-control procedures. Requirements are commonly represented as **User Stories** in a **Product Backlog**, and the Product Owner and team decide what to build based on priorities and feedback.

| Traditional Concept | Common Agile Approach |
|---|---|
| Sign-off | Product Owner acceptance of completed work |
| Baseline | A shared understanding of the current scope or iteration |
| Change control | Backlog refinement, reprioritization, and agreement on scope |

> Agile embraces change, but change still needs a reference point: **"What have we agreed to build now?"**

---

### Key Takeaways

- Customers are not always users; users are not always the people who pay.
- Business Requirements explain **why**; User Requirements explain **what users need**; Functional Requirements explain **what the software must do**.
- Developers should not guess user needs — involve actual users.
- Missing stakeholders cause rework, delays, and extra cost.
- The Expectation Gap shrinks with frequent, structured communication.
- Requirements are iterative — the goal is shared understanding, not perfection.
- Customers have both **Rights and Responsibilities**.
- Sign-off is a milestone, not a freeze — future changes go through change control.
- Strong requirements practices need management commitment to last.
- The requirements process is an investment that reduces rework, cost, and project chaos.

