# Warehouse Sales System

## Project Overview
A CLI-based prototype for managing warehouse inventory and sales operations.

## Setup Instructions

### Prerequisites
- Python 3.11 or higher

### Installation

1. Clone the repository
2. Create virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`

## Features (Current Version)

### Product Management
- ✅ Add new products with name, price, and quantity
- ✅ Update existing product prices with confirmation
- ✅ Add stock quantity to existing products
- ✅ Product search by name (partial match)
- ✅ Product selection via numbered list
- ✅ Input validation for all user inputs
- ✅ Product active/inactive status based on price and quantity
- ✅ Continue/exit flow after each operation

## Usage
Run the main script:
```
python main.py
```

## Future Roadmap
- Persistent storage with JSON/PostgreSQL
- Sales reports (daily/monthly)
- Low stock alerts
- REST API with FastAPI
- Authentication and role-based access

## Tech Stack (Current)
- Python 3
- CLI interface

## Project Status
Prototype phase - Basic CRUD operations for inventory management