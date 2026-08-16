Troubleshooting
This document logs real technical issues encountered during the setup and development of the project, along with their resolution steps.

Issue 1: PowerShell Execution Policy
Problem
PowerShell refused to execute the virtual environment activation script (.venv\Scripts\activate) and displayed the following error:

cannot be loaded because running scripts is disabled on this system.
Solution
Opened PowerShell as Administrator and updated the execution policy:

Set-ExecutionPolicy RemoteSigned
This allows locally created scripts to run while requiring downloaded scripts to be digitally signed.
Issue 2: Project Files Created Inside .venv
Problem
Running git status showed .venv as untracked, while expected project files such as main.py, README.md, and .gitignore were missing from the expected project root structure.

Solution
The project files had accidentally been created inside the .venv/ directory.
The misplaced files were deleted from .venv/ and recreated in the project root directory, at the same level as .venv/.

Verified Project Structure
warehouse_sales_system/
├── .venv/
├── main.py
├── README.md
├── ToDo.md
├── .gitignore
└── docs/
    ├── requirements.md
    └── troubleshooting.md اديني تقييمك كده بإيجاز شديد، وقول لي هل في أي ملاحظات ولا تعتمد؟