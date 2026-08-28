# Warehouse Sales System
## Software Requirements Specification (SRS)

- **Version:** 0.1
- **Status:** Draft
- **Document Type:** Vision & Requirements

---

## 1. Project Overview

The Warehouse Sales System is a command-line inventory management application developed in Python. It is designed to manage products, update inventory, process sales, and display inventory information. The project is intentionally developed in incremental stages, allowing new concepts to be applied as they are learned while supporting continuous improvement and future expansion.

---

## 2. Project Goal

The primary goal of this project is educational. It serves as a practical platform for applying software engineering principles and backend development concepts throughout the learning process. At the same time, the project is designed to evolve gradually into the foundation of a full ERP system, with new features and architectural improvements added step by step as new knowledge and skills are acquired.

---

## 3. Stakeholders

The following stakeholders represent the intended users and interested parties of the project. Some stakeholders are supported by the current implementation, while others are planned as the system evolves toward a complete ERP solution.

### 3.1 Business Owner / Manager

- **Role:** Responsible for overseeing business operations and inventory
- **Status:** ✅ Supported

**Goals:**
- Monitor inventory levels
- Review business operations
- Track stock movements and sales

---

### 3.2 Warehouse Employee

- **Role:** Responsible for managing products and inventory
- **Status:** ✅ Supported

**Goals:**
- Add new products
- Update product information
- Manage stock quantities

---

### 3.3 Cashier

- **Role:** Responsible for processing sales transactions
- **Status:** 🔲 Planned

**Goals:**
- Search for products
- Process sales
- Generate sales invoices

---

### 3.4 Accountant

- **Role:** Responsible for reviewing financial and sales information
- **Status:** 🔲 Planned

**Goals:**
- Review sales reports
- Monitor financial records
- Analyze business performance

---

### 3.5 System Administrator

- **Role:** Responsible for maintaining and managing the system
- **Status:** 🔲 Planned

**Goals:**
- Manage user accounts
- Configure permissions
- Perform backups
- Maintain system reliability

---

## 4. Functional Requirements

### 4.1 Product Management

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-01 | Allow user to add a new product with: name, description, price, quantity, and category | High | Phase 1 | ✅ Implemented |
| FR-02 | Uniquely identify each product | High | Phase 1 | ✅ Implemented |
| FR-03 | Allow user to view a list of all products with their details | High | Phase 1 | ✅ Implemented |
| FR-04 | Allow user to search for a product by name or identifier | High | Phase 1 | ✅ Implemented |
| FR-05 | Allow user to update product information (name, description, price, quantity, category) | High | Phase 1 | ✅ Implemented |
| FR-06 | Allow user to remove a product from the inventory | Medium | Phase 3 | 🔲 Planned |
| FR-07 | Prevent removal of a product if it has associated sales records (soft delete or warning) | Medium | Phase 3 | 🔲 Planned |
| FR-08 | Allow user to view products that are low in stock (below a configurable threshold) — See Q-03 | Medium | Phase 2 | 🔲 Planned |

---

### 4.2 Inventory Management

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-09 | Update product quantity automatically when a sale is processed | High | Phase 2 | 🔲 Planned |
| FR-10 | Allow user to manually adjust inventory quantities (e.g., restocking or returns) | High | Phase 1 | ✅ Implemented |
| FR-11 | Prevent processing a sale if requested quantity exceeds available stock | High | Phase 2 | 🔲 Planned |
| FR-12 | Log all inventory changes (who, what, when, why) for traceability | Medium | Phase 4 | 🔲 Planned |
| FR-13 | Allow user to generate an inventory report showing current stock levels | Medium | Phase 3 | 🔲 Planned |

---

### 4.3 Sales Processing

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-14 | Allow the Cashier to start a new sales transaction | High | Phase 2 | 🔲 Planned |
| FR-15 | Allow user to add products to the current sale by product identifier | High | Phase 2 | 🔲 Planned |
| FR-16 | Calculate the total price of the sale automatically as (Price × Quantity), excluding any tax — See Out of Scope | High | Phase 2 | 🔲 Planned |
| FR-17 | Display a summary of the current sale before finalization | High | Phase 2 | 🔲 Planned |
| FR-18 | Allow user to remove or adjust quantities of items in the current sale | Medium | Phase 2 | 🔲 Planned |
| FR-19 | Generate a simple text invoice after the sale is finalized | Medium | Phase 2 | 🔲 Planned |
| FR-20 | Store sales records for future reference and reporting | High | Phase 2 | 🔲 Planned |
| FR-21 | Allow user to apply discounts (percentage or fixed amount) to a sale | Medium | Phase 3 | 🔲 Planned |
| FR-22 | Support different payment methods | Low | Phase 4 | 🔲 Planned |
| FR-23 | Calculate and display the change due when cash payment is used | Low | Phase 4 | 🔲 Planned |
| FR-24 | Allow sales to be canceled or returned | Low | Phase 4 | 🔲 Planned |
| FR-25 | Update quantity when the same product is added multiple times to the same sale | Medium | Phase 2 | 🔲 Planned |

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
| FR-33 | Persist application data (products, sales, users) between sessions | High | Phase 2 | 🔲 Planned |
| FR-34 | Load data from persistent storage upon startup | High | Phase 2 | 🔲 Planned |
| FR-35 | Automatically save data after each significant operation (add, edit, sale) | High | Phase 2 | 🔲 Planned |

> **Note:** Implementation technology (SQLite, PostgreSQL, JSON, etc.) will be selected during Phase 2.

---

### 4.7 Command-Line Interface

| ID | Description | Priority | Target Release | Status |
|----|-------------|:--------:|:--------------:|:------:|
| FR-36 | Provide a text-based menu interface for navigation | High | Phase 1 | ✅ Implemented |
| FR-37 | Display clear prompts and error messages for invalid input | High | Phase 1 | ✅ Implemented |
| FR-38 | Support a command-prefix pattern (e.g., `/help`, `/add`, `/list`) for efficiency | Low | Phase 1 | ✅ Implemented |

---

## 5. Non-Functional Requirements

### 5.1 Performance

| ID | Description | Target Release |
|----|-------------|:--------------:|
| NFR-01 | Load inventory data within 2 seconds for up to 10,000 products | Phase 3 |
| NFR-02 | Process a sales transaction in under 1 second | Phase 3 |

### 5.2 Reliability

| ID | Description | Target Release |
|----|-------------|:--------------:|
| NFR-03 | Handle invalid input gracefully without crashing | Phase 1 |
| NFR-04 | Maintain data integrity during unexpected shutdowns | Phase 3 |

### 5.3 Security

| ID | Description | Target Release |
|----|-------------|:--------------:|
| NFR-05 | User passwords shall be hashed before storage | Phase 3 |
| NFR-06 | Log all authentication attempts for audit purposes | Phase 4 |

### 5.4 Maintainability

| ID | Description | Target Release |
|----|-------------|:--------------:|
| NFR-07 | Codebase shall be organized by module (e.g., product, sales, user) | Phase 1 |
| NFR-08 | New features shall be added without modifying existing working code (Open/Closed Principle) | Phase 2 |

### 5.5 Usability

| ID | Description | Target Release |
|----|-------------|:--------------:|
| NFR-09 | The interface shall be intuitive for users with basic computer literacy | Phase 1 |

---

## 6. Out of Scope

The following items are explicitly excluded from the current scope:

- **Graphical User Interface (GUI):** The system is strictly command-line based
- **Mobile Application:** No mobile version is planned
- **Multi-warehouse Management:** The system assumes a single warehouse location
- **Barcode / QR Code Scanning:** No hardware integration is supported
- **Currency Exchange:** The system operates in a single currency
- **Tax Calculation:** Tax handling is not included in the initial scope (total price = Price × Quantity only)
- **E-commerce Integration:** No integration with online stores
- **Third-party Accounting Integration:** No external software integration
- **Real-time Inventory Updates:** No concurrent multi-user inventory updates

---

## 7. Open Questions

| ID | Question | Status | Target Resolution |
|----|----------|:------:|:-----------------:|
| Q-01 | What technology will be used for data persistence? (JSON, CSV, SQLite, etc.) | 🔲 Open | Phase 2 |
| Q-02 | Should the system support multiple languages? | 🔲 Open | Future |
| Q-03 | What is the configurable threshold for low-stock alerts? (Referenced in FR-08) | 🔲 Open | Phase 2 |
| Q-04 | Should product categories be predefined or user-defined? | 🔲 Open | Phase 2 |
| Q-05 | How will sales tax be handled if required in the future? | 🔲 Open | Future |

---

## 8. Implementation Phases

| Phase | Focus | Requirements | Time Estimate |
|-------|-------|--------------|:-------------:|
| **Phase 1** | Product Management + Inventory Core | FR-01 to FR-05, FR-10, FR-36 to FR-38 | ~2 weeks |
| **Phase 2** | Data Persistence + Basic Sales | FR-08, FR-09, FR-11, FR-14 to FR-20, FR-25, FR-33 to FR-35 | ~3 weeks |
| **Phase 3** | User Management + Low Stock Alerts | FR-06, FR-07, FR-13, FR-21, FR-26 to FR-29 | ~2 weeks |
| **Phase 4** | Advanced Sales + Reports | FR-12, FR-22 to FR-24, FR-30, FR-32 | ~2 weeks |
| **Phase 5** | Full ERP Foundation | FR-31 + remaining backlog | ~1 week |

---

## 9. Document History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1 | 2025-01-XX | Project Owner | Initial draft of SRS |

---

## 10. Revision Log

| Revision | Date | Description |
|----------|------|-------------|
| v0.1 | 2025-01-XX | Initial creation with stakeholder definitions, functional requirements, non-functional requirements, out-of-scope items, open questions, and phase planning |

---

> **Document Status:** Draft. This document serves as the authoritative reference for the Warehouse Sales System project. All implementation decisions shall be validated against the requirements and open questions documented herein.