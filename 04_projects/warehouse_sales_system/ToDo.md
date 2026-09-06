# Warehouse Sales System — To-Do

## Development Rule

```
Is the problem clear and the fix small?
    Yes → Fix it now
    No  → Log it in its proper phase and move on
```

## Feature Timing Test

Before adding a new feature, ask in order:

1. **Can this be added without changing the domain model?**
   Yes → build it now.
2. **Does it require defining new domain entities, identities, relationships, or meaningful domain state?**
   Yes → defer to OOP.
3. **Does it depend mainly on persistence, database querying, or relational data at scale?**
   Yes → defer toward SQL.

This complements the Development Rule above: that rule is about *effort*, this one is about whether the fix locks in an architectural decision we already know will change.

---

## Current Status

- [x] Complete the initial inventory management prototype.
- [x] Implement basic product management operations.
- [x] Implement basic user input validation and input error handling.
- [x] Add project documentation and initial requirements documentation.
- [x] Establish the initial Git structure and version history.
- [x] Review all functions and identify where exception handling is needed.
- [x] Apply targeted exception handling where user input can fail.
- [x] Confirm that normal user control flow does not require exceptions.
- [x] Practice logging on the `learning/logging` branch.

---

## Known Debt — Seeds of Complexity

| Seed | Revisit / Address In |
|---|---|
| Linear O(n) search when looking up products | 🟡 Phase 2 DSA |
| Case-insensitive lookup with no index | 🟡 Phase 2 DSA |
| `get_positive_number()` mixes input, parsing, and validation | 🟡 When the function is next touched |
| `converter` type hint should be `Callable[[str], int \| float]`, not `type` | 🟢 When the function is next touched |
| Normalization (`.lower()`, `.title()`, `.strip()`) scattered across the code | 🟡 When repeated again |
| Menu strings coupled to `match`/`case` | 🟡 When an Enum is introduced |
| No explicit product identity in the schema | 🟡 When product identity / SKU / barcode is introduced |
| `main.py` is 580+ lines — the issue is mixed responsibilities, not raw length | 🟡 Watch — will split with the JSON refactor |
| `global products` spread across every function | 🔵 OOP |
| Product schema duplicated across functions | 🔵 OOP |
| `is_active` stored — OOP will re-evaluate this as a computed property or explicit domain rule | 🔵 OOP |
| UI and business logic merged in `update_price` and `update_quantity` | 🔵 OOP |
| `sell_product()` handles more than one concern | 🔵 OOP |
| `handle_product()` mixes workflow, UI, and business logic | 🔵 OOP |
| `bool \| None` used as a domain result in `sell_product` | 🔵 OOP |
| `is_new` boolean changes the entire behavior of a function | 🔵 OOP |

> DSA runs **alongside** the project throughout, not as a blocker before it.

---

## Phase 2 — Algorithms & Data Structures

*(Planned focus for this project)*

### Code Quality & Refactoring

- [ ] Review existing code using the concepts learned in Phase 2.
- [ ] Make only small, clearly justified refactors that improve readability or correctness.
- [ ] Avoid architectural refactoring that belongs to Phase 3.

### Algorithms & Data Structures

- [ ] Review the data structures currently used by the inventory system.
- [ ] Review product-search operations and their time complexity.
- [ ] Replace inefficient lookup approaches where an appropriate data structure provides a meaningful improvement.
- [ ] Apply relevant algorithms and data-structure concepts to the project where appropriate.

### Near-Term Feature Work

*(These pass the Feature Timing Test: pure behavior on top of the existing structure, no new domain model required.)*

- [ ] **Inventory Valuation** — calculate total inventory value (`price × stock`) across all products. Practices looping over a dict with simple aggregation; a standard calculation in any real warehouse system.
- [ ] **Low Stock Alert** — surface products that have hit a minimum threshold. Practices conditionals and threshold logic; a core feature in any WMS/ERP.
- [ ] **Filtering / Sorting** — sort products using `sorted()` and `lambda`, and filter by status (active/inactive). Reinforces DSA concepts directly.
- [ ] **JSON Persistence on `main`** — learn `json.load()` / `json.dump()`, serialization, `FileNotFoundError`, and when to read vs. write. Intentionally simple: no repository pattern, service layer, storage abstraction, or other architecture patterns yet.
- [ ] **Refactor alongside JSON** — split `main.py` into simple modules (`helpers`, `inventory`, `sales`, `menus`) only if the file structure benefits from it.
- [ ] **Transaction Log** — a list recording each operation with a timestamp (`datetime`). Comes after JSON persistence so the log actually survives between sessions. Keep the schema flexible per operation type; this is a simple event log, not a full audit system — the final schema will be decided at implementation time.

### Preparation for OOP

- [ ] Identify responsibilities currently handled by the main functions and data structures.
- [ ] Identify areas that would benefit from object-oriented design.
- [ ] Prepare the codebase for the transition to OOP in Phase 3.

---

## Phase 3 — Object-Oriented Programming

*(Planned focus for this project)*

- [ ] Redesign the inventory domain using appropriate classes and objects, replacing the global product dictionaries with domain objects and appropriate inventory management.
- [ ] Remove the duplicated product schema.
- [ ] Re-evaluate `is_active` — keep it as a computed property if it stays derived from price/stock only, or make it an explicit domain rule if the business rules change.
- [ ] Separate UI from business logic.
- [ ] Redesign `sell_product()` and `handle_product()` around single responsibilities.
- [ ] Replace `bool | None` with a proper domain result type.
- [ ] Separate the `is_new` behavioral flag from the core logic.
- [ ] Redesign the storage boundary so JSON can later be swapped for SQL without the business logic knowing how data is stored.
- [ ] Re-evaluate existing functions and data structures after the OOP redesign.
- [ ] Use the ERP/WMS domain reference (see Backlog below) to inform the shape of the `Product`/`Inventory` domain model — without committing to every feature listed there.

---

## Later Development

### SQL

- [ ] Replace JSON with SQL once the storage layer is properly isolated.
- [ ] Review lookup strategy and apply appropriate queries and indexes; lookup efficiency now becomes primarily a database concern rather than an in-memory data-structure concern.

### Backend / API

- [ ] Re-evaluate the project architecture when backend/API concepts are introduced.
- [ ] Convert the project into a REST API (FastAPI) once the business logic and storage boundaries are properly isolated.
- [ ] Refactor or extend the project as appropriate when new backend concepts are learned.
- [ ] Avoid implementing future concepts before they are covered in the learning roadmap.

### Logging

- [ ] Continue using `learning/logging` as an independent learning branch while studying Logging further.
- [ ] Keep the `learning/logging` branch independent from the main project.
- [ ] After the main project has evolved through the earlier phases, apply Logging concepts directly to the then-current `main` codebase.
- [ ] Review the Logging implementation based on the project's architecture at that stage.

---

## Backlog — Domain Expansion

*Sourced from an ERP/WMS domain gap analysis. These entries capture missing domain requirements and workflows worth knowing about — they are not implementation commitments for the current phase. Each will be picked up only when the roadmap and the Feature Timing Test both say it's time.*

### Post-OOP / Core Domain (Warehouse & Inventory)

| Feature | Notes |
|---|---|
| Product Categories / Item Groups | Revisit when the product domain model is designed |
| Product Identity (SKU) / Barcode | Revisit when the Product model is redesigned |
| Units of Measure | Revisit when the Product model is redesigned (e.g., buy by carton, sell by piece) |
| Stock Adjustment | Revisit when the inventory domain model is designed |
| Stocktaking / Physical Inventory | Revisit when the inventory domain model is designed |
| Reorder Point / Minimum Stock Level | Revisit once the Product/inventory domain model exists |
| Multiple Warehouses | Requires a revised inventory architecture |
| Warehouse Locations / Bins | Requires multi-warehouse support first |

### Post-OOP / Sales & Purchasing

| Feature | Notes |
|---|---|
| Customers | Requires domain and architecture expansion |
| Suppliers | Requires domain and architecture expansion |
| Sales Orders | Requires the customer domain first |
| Stock Reservation | Requires Sales Orders first |
| Deliveries / Goods Issue | Requires Sales Orders first |
| Sales Returns | Requires Sales Orders first |
| Purchase Requisition | Requires the purchasing workflow to exist |
| Purchase Orders | Requires the supplier domain first |
| Goods Receipt | Requires Purchase Orders first |
| Purchase Returns | Requires Purchase Orders first |
| Supplier Evaluation | Requires the supplier domain and historical order data |

### Advanced / Later

| Feature | Notes |
|---|---|
| Invoices / Credit Notes | Requires the sales/purchasing domain and SQL persistence |
| Customer Credit Limits | Requires the customer domain and SQL persistence |
| Roles / Permissions | Requires authentication/authorization, not just a database |
| Approval Workflows | Requires roles/permissions first |
| Audit Trail | Requires a stable architecture and durable persistence, not SQL alone |
| Advanced Inventory Reports | Requires SQL queries |
| Profitability / Cost Analysis | Requires SQL |
| Batch / Lot Tracking | Domain-specific — add only if relevant to the product types used |
| Serial Number Tracking | Domain-specific — add only if relevant |
| Expiry Date Tracking | Domain-specific — add only if relevant |

### Out of Scope

| Item | Why |
|---|---|
| Pagination | Not needed for a small CLI tool |
| Manufacturing / MRP | An entirely different domain (BOM, routing, production orders) |
| HR / Payroll / Recruitment | A separate ERP domain, unrelated to warehouse/sales |
| Fleet & Logistics | A separate ERP domain |
| Maintenance / CMMS | A separate ERP domain |
| Full General Ledger / AP / AR Accounting | A separate ERP domain; only the sales/purchasing edges (invoices, credit limits) are relevant here |

These are kept as a domain reference in case the project's scope ever genuinely expands — not as a plan to build a full ERP.
