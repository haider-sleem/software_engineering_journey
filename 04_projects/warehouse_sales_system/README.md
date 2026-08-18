# Warehouse Sales System

A learning project for building a small warehouse and sales management system, developed while progressively applying Python and Software Engineering concepts studied throughout the learning roadmap.

The project evolves alongside the roadmap rather than being built as a single finished application. Its current implementation reflects the concepts learned up to this stage and is not intended to represent a final or production-ready design.

## Current Status

**Prototype — In Development**

The current version provides basic inventory and sales management functionality through a command-line interface and serves as a practical environment for applying concepts learned throughout the roadmap.

## Current Features

- Add new products with name, price, and quantity.
- Search and select products by name using partial matching.
- Update existing product prices with confirmation.
- Update existing product quantities.
- View product status and details.
- Basic cashier and inventory management menus.
- Basic input validation and input error handling using `try`/`except` for invalid input.

## Project Structure

```text
warehouse_sales_system/
├── main.py
├── README.md
├── ToDo.md
└── docs/
    ├── requirements.md
    └── troubleshooting.md
```

## Setup & Usage

### Prerequisites

- Python 3.11 or higher

### Installation

Clone the repository, then create and activate a virtual environment:

```bash
python -m venv .venv
```

**Windows:**

```cmd
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### Run the Project

```bash
python main.py
```

## Learning Roadmap

The project is developed incrementally as new concepts are learned and applied.

### Phase One — Software Foundations

The initial version of the project was developed while building fundamental Python skills, including:

- Python fundamentals and functions.
- Basic data structures.
- Input validation.
- Basic project organization.

### Phase 2 — Algorithms & Data Structures

*(Planned focus for this project)*

The project will be reviewed and improved using concepts learned during this phase, including:

- Refactoring existing functions.
- Improving error handling using exceptions and concepts learned in this phase.
- Reviewing the data structures used by the inventory system.
- Reviewing product-search operations and their efficiency.
- Preparing the codebase for the transition to OOP.

### Phase 3 — Object-Oriented Programming

*(Planned focus for this project)*

The project will gradually evolve toward an object-oriented design, including:

- Redesigning the inventory domain using appropriate classes and objects.
- Separating responsibilities according to OOP principles.
- Refactoring workflows and business logic where appropriate.
- Improving the overall project structure based on the OOP concepts learned.

### Later Stages

As the learning roadmap progresses, additional concepts may be applied to the project when they become relevant. The project intentionally avoids implementing future concepts before they are covered in the learning process.

See [`ToDo.md`](./ToDo.md) for the detailed and up-to-date list of planned work.

## Learning Branches

This repository includes independent branches used to practice specific concepts while they are being learned. These branches are kept separate from `main` and are not intended to be merged into it:

- **`learning/logging`**: An independent branch for practicing Logging concepts. Logging will later be applied directly to the then-current `main` codebase after the project has evolved through the relevant learning phases.
- **`docs/requirements`**: An independent branch for applying Software Requirements concepts to the project. The branch remains separate from `main` and is not intended to be merged into it.

These branches represent learning activities and experiments rather than separate production versions of the project.

## Documentation

- [`docs/requirements.md`](./docs/requirements.md) — project requirements and scope documentation.
- [`docs/troubleshooting.md`](./docs/troubleshooting.md) — documented problems and solutions.
- [`ToDo.md`](./ToDo.md) — planned project improvements organized by learning phase.

## Purpose

This is primarily a learning and practical application project.

Its purpose is to provide a continuously evolving codebase where programming and Software Engineering concepts can be applied progressively.

The goal is not to maximize the number of features, but to improve the codebase, design, and engineering practices as the learning roadmap advances.