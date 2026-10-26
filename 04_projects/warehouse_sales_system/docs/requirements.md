# Warehouse Sales System
## Software Requirements Specification (SRS)

- **Version:** 1.1
- **Status:** Approved
- **Document Type:** Vision & Requirements

---

## 1. Project Overview

The Warehouse Sales System is a command-line inventory management application developed in Python. It is designed to manage products, update inventory, process sales, and display inventory information. The project is intentionally developed in incremental stages, allowing new concepts to be applied as they are learned while supporting continuous improvement and future expansion.

---

## 2. Project Goal

The primary goal of this project is educational. It serves as a practical platform for applying software engineering principles and backend development concepts throughout the learning process. At the same time, the project is designed to evolve gradually into the foundation of a full ERP system, with new features and architectural improvements added step by step as new knowledge and skills are acquired.

---

## 3. Stakeholders

*(Note: "Workflow Supported" means the system allows the user to perform their core tasks via the CLI. It does **not** mean the system has user identities, authentication, or role-based permissions yet. Those are Planned for Phase 3.)*

### 3.1 Business Owner / Manager
- **Role:** Responsible for overseeing business operations and inventory
- **Workflow Status:** ✅ Supported (Can view current inventory data)
**Goals:** Monitor current inventory levels, Review current business operations, Track historical stock movements and sales *(Note: Historical tracking, auditing, and sales reporting are Planned for later phases. Current support only provides a snapshot of the present state.)*

### 3.2 Warehouse Employee
- **Role:** Responsible for managing products and inventory
- **Workflow Status:** ✅ Supported (Can add and update products)
**Goals:** Add new products, Update product information, Manage stock quantities

### 3.3 Cashier
- **Role:** Responsible for processing sales transactions
- **Workflow Status:** ✅ Supported (Basic single-item sale)
**Goals:** Search for products, Process sales, Generate sales invoices *(Note: Invoices are planned for a later phase)*

### 3.4 Accountant
- **Role:** Responsible for reviewing financial and sales information
- **Workflow Status:** 🔲 Planned
**Goals:** Review sales reports, Monitor financial records, Analyze business performance

### 3.5 System Administrator
- **Role:** Responsible for maintaining and managing the system
- **Workflow Status:** 🔲 Planned
**Goals:** Manage user accounts, Configure permissions, Perform backups, Maintain system reliability

---

### 3.6 Requirement Status Definitions

To maintain accurate tracking, requirements will follow these mutually exclusive statuses:
- **Planned**: Work has not started.
- **Partially Implemented**: Only part of the requirement's scope is implemented (e.g., core logic exists, but UI, persistence, or edge cases are missing).
- **Implemented**: The intended complete implementation exists in the code, but it has not yet been fully verified against acceptance criteria (e.g., no formal testing or performance measurement has been done).
- **Verified**: The implementation has passed the required tests or measurements and is confirmed to meet the expected behavior.
- **Deferred**: Postponed to a future phase.

---

## 4. Functional Requirements

### 4.1 Product Management

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-01 | Allow user to add a new product with: name, price, and stock | High | Phase 1 | ✅ Implemented |
| FR-02 | Use the product name as the product key in the current in-memory data structure | High | Phase 1 | ✅ Implemented |
| FR-03 | Allow user to view a list of all products with their details | High | Phase 1 | ✅ Implemented |
| FR-04 | Allow user to search for a product by name | High | Phase 1 | ✅ Implemented |
| FR-05 | Allow user to update product price and stock | High | Phase 1 | ✅ Implemented |
| FR-05b| Allow user to update product description and category | Medium | Phase 3 | 🔲 Planned |
| FR-06 | Allow user to remove a product from the inventory | Medium | Phase 3 | 🔲 Planned |
| FR-07 | Prevent removal of a product if it has associated sales records (soft delete or warning) | Medium | Phase 3 | 🔲 Planned |
| FR-08 | Allow user to view products that are low in stock (below a configurable threshold) | Medium | Phase 2 | 🔲 Planned |

---

### 4.2 Inventory Management

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-09 | Update product quantity automatically when a sale is processed | High | Phase 2 | 🟡 Partially Implemented |
| FR-10 | Allow user to manually add positive quantities to inventory (e.g., restocking) | High | Phase 1 | ✅ Implemented |
| FR-11 | Prevent processing a sale if requested quantity exceeds available stock | High | Phase 2 | 🟡 Partially Implemented |
| FR-12 | Log all inventory changes (who, what, when, why) for traceability | Medium | Phase 4 | 🔲 Planned |
| FR-13 | Allow user to generate an inventory report showing current stock levels | Medium | Phase 3 | 🟡 Partially Implemented |
| FR-13b| Calculate and display total inventory valuation (Price × Stock) | Medium | Phase 2 | ✅ Implemented |

*(Note on FR-09 & FR-11: Current implementation supports a single-item sale. The requirement as written implies a complete sales cycle, which is not yet fully implemented.)*
*(Note on FR-10: Current implementation allows adding a positive number to stock. A full Stock Adjustment workflow requiring a reason, user ID, and timestamp is deferred to OOP/Architecture.)*
*(Note on FR-13: Current `view_products()` displays stock levels, but a dedicated, exportable independent inventory report remains Planned.)*
*(Note on FR-13b: Inventory Valuation is currently calculated using the **selling price** × stock. It does not represent the accounting cost of goods. Cost-based valuation is out of scope for the current phase.)*

---

### 4.3 Sales Processing

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-14 | Allow the Cashier to start a new sales transaction | High | Phase 2 | 🟡 Partially Implemented |
| FR-15 | Allow user to add products to the current sale by product identifier | High | Phase 2 | 🟡 Partially Implemented |
| FR-16 | Calculate the total price of the sale automatically as (Price × Quantity), excluding any tax | High | Phase 2 | ✅ Implemented |
| FR-17 | Display a summary of the current sale before finalization | High | Phase 2 | 🔲 Planned |
| FR-18 | Allow user to remove or adjust quantities of items in the current sale | Medium | Phase 2 | 🔲 Planned |
| FR-19 | Generate a simple text invoice after the sale is finalized | Medium | Phase 2 | 🔲 Planned |
| FR-20 | Store sales records for future reference and reporting | High | Phase 2 | 🔲 Planned |
| FR-21 | Allow user to apply discounts (percentage or fixed amount) to a sale | Medium | Phase 3 | 🔲 Planned |
| FR-22 | Support different payment methods | Low | Phase 4 | 🔲 Planned |
| FR-23 | Calculate and display the change due when cash payment is used | Low | Phase 4 | 🔲 Planned |
| FR-24 | Allow sales to be canceled or returned | Low | Phase 4 | 🔲 Planned |
| FR-25 | Update quantity when the same product is added multiple times to the same sale | Medium | Phase 2 | 🔲 Planned |

*(Note on Sales Processing: Current implementation supports a basic single-item sale workflow. A multi-item cart, transaction summary, finalization workflow, invoice generation, and persistent sales records are not implemented.)*

---

### 4.4 User Management

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-26 | Support multiple user roles: Warehouse Employee, Cashier, Business Owner, Accountant, System Administrator | High | Phase 3 | 🔲 Planned |
| FR-27 | Require authentication (username and password) before access | High | Phase 3 | 🔲 Planned |
| FR-28 | Restrict access to features based on user roles | High | Phase 3 | 🔲 Planned |
| FR-29 | Allow System Administrator to create, update, and delete user accounts | Medium | Phase 3 | 🔲 Planned |

---

### 4.5 Reporting

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-30 | Allow Business Owner to generate a sales report by date range | Medium | Phase 4 | 🔲 Planned |
| FR-31 | Allow Accountant to generate a profit/loss summary | Low | Phase 5 | 🔲 Planned |
| FR-32 | Display the top-selling products for a given period | Low | Phase 4 | 🔲 Planned |

---

### 4.6 Data Persistence

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-33 | Persist application data between sessions (JSON first, then SQL) | High | Phase 2 | 🔲 Planned |
| FR-34 | Load data from persistent storage upon startup | High | Phase 2 | 🔲 Planned |
| FR-35 | Automatically save data after each significant operation | High | Phase 2 | 🔲 Planned |

> **Note:** The project roadmap dictates using JSON for early persistence (Phase 2), and migrating to SQL in a later phase.

---

### 4.7 Command-Line Interface

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-36 | Provide a text-based menu interface for navigation | High | Phase 1 | ✅ Implemented |
| FR-37 | Display clear prompts and error messages for invalid input | High | Phase 1 | 🟡 Partially Implemented |
| FR-38 | Support a command-prefix pattern (e.g., `/help`, `/add`, `/list`) for efficiency | Low | Phase 5 | 🔲 Planned |
| FR-39 | Search products by Barcode/QR Code | Low | Phase 5 | 🔲 Planned |

---

## 5. Non-Functional Requirements

### 5.1 Performance

| ID | Description | Target Release | Status |
|----|-------------|:--------------:|:------:|
| NFR-01 | Load inventory data within 2 seconds for up to 10,000 products | Phase 3 | 🔲 Planned |
| NFR-02 | Process a sales transaction in under 1 second | Phase 3 | 🔲 Planned |

### 5.2 Reliability

| ID | Description | Target Release | Status |
|----|-------------|:--------------:|:------:|
| NFR-03 | Handle invalid input gracefully without crashing | Phase 1 | 🟡 Partially Implemented |
| NFR-04 | Maintain data integrity during unexpected shutdowns | Phase 3 | 🔲 Planned |

### 5.3 Security

| ID | Description | Target Release | Status |
|----|-------------|:--------------:|:------:|
| NFR-05 | User passwords shall be hashed before storage | Phase 3 | 🔲 Planned |
| NFR-06 | Log all authentication attempts for audit purposes | Phase 4 | 🔲 Planned |

### 5.4 Maintainability

| ID | Description | Target Release | Status |
|----|-------------|:--------------:|:------:|
| NFR-07 | Codebase shall be organized by module (e.g., product, sales, user) | Phase 2 | 🔲 Planned |
| NFR-08 | The codebase should be structured to support maintainable extensions and minimize unnecessary changes to existing functionality | OOP / Architecture Redesign | 🟡 Partially Implemented |

### 5.5 Usability

| ID | Description | Target Release | Status |
|----|-------------|:--------------:|:------:|
| NFR-09 | The interface shall be intuitive for users with basic computer literacy | Phase 1 | 🔲 Planned |

---

## 6. Scope Boundaries

### Outside the current implementation scope
- Graphical User Interface (GUI)
- Mobile Application
- Multi-warehouse Management
- Currency Exchange
- Tax Calculation
- E-commerce Integration
- Third-party Accounting Integration
- Real-time Concurrent Updates
- Barcode/QR Code Scanning *(Note: Current implementation only supports searching by product name. The prompt mentions barcode, but no actual barcode logic exists yet).*

### Long-term direction (Not permanently excluded)
- GUI and Mobile applications.
- Multi-warehouse operations.
- External integrations and additional ERP modules.
- Real-time capabilities and multi-user concurrency.
- Barcode/QR Code Scanning.

---

## 7. Open Questions

| ID | Question | Status | Target Resolution |
|----|----------|:------:|:-----------------:|
| Q-01 | ~~What technology will be used for data persistence?~~ Resolved: JSON first, then SQL. | ✅ Resolved | Phase 2 |
| Q-02 | Should the system support multiple languages? | 🔲 Open | Future |
| Q-03 | What is the configurable threshold for low-stock alerts, and does the rule use `<` (strictly below) or `<=` (at or below)? | 🔲 Open | Phase 2 |
| Q-04 | Should product categories be predefined or user-defined? | 🔲 Open | Phase 3 |
| Q-05 | How will sales tax be handled if required in the future? | 🔲 Open | Future |

---

## 8. Implementation Phases

| Phase | Focus | Requirements |
|-------|-------|--------------|
| **Phase 1** | Product Management + Inventory Core | FR-01 to FR-05, FR-10, FR-36 to FR-37 |
| **Phase 2** | Data Persistence + Basic Sales + Low Stock | FR-08, FR-09, FR-11, FR-13b, FR-14 to FR-20, FR-25, FR-33 to FR-35 |
| **Phase 3** | User Management | FR-05b, FR-06, FR-07, FR-13, FR-21, FR-26 to FR-29 |
| **Phase 4** | Advanced Sales + Reports | FR-12, FR-22 to FR-24, FR-30, FR-32 |
| **Phase 5** | Future ERP Expansion | FR-31, FR-38, FR-39 + remaining backlog |

**Roadmap Note:** These phases describe the intended functional goals and scope. Listing a requirement in a phase does not mean it is fully implemented; it may be partially implemented or still planned. The implementation sequence may be revised as the project evolves.

---

## 9. Document History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1 - 0.8 | 2025-2026 | Project Owner | Iterative drafts and refinements based on code reviews. |
| 1.0 | 2026-10-24 | Project Owner | **Approved**. Aligned Q-04 and FR-39 with phases, clarified barcode scope, added selling-price note to Inventory Valuation, and clarified phase scope. |
| 1.1 | 2026-10-24 | Project Owner | Corrected FR-09, FR-11, FR-16, FR-24 statuses. Updated FR-02 wording. Added Sales Processing implementation note. |

---

> **Document Status:** Approved. This document serves as the authoritative reference for the Warehouse Sales System project. All implementation decisions shall be validated against the requirements and open questions documented herein.
