# Chapter 2: Environment Setup and the Command Line

---

## The Filesystem

- The filesystem organizes data into folders and files. The starting point is the **Root**.
  - Windows: `C:\`
  - Linux/macOS: `/`
- On Linux, external drives or Windows partitions are mapped inside folders like `/mnt/d/`.

### The Slash Problem

Hardcoding **backslashes** (`\`) in Python strings breaks cross-platform code (works on Windows, fails on Linux/macOS). Forward slashes (`/`) generally work on all modern platforms, but `pathlib` is still the recommended, safest approach.

### `pathlib` Solution

```python
from pathlib import Path

# The / operator joins paths safely, regardless of OS
config_path = Path("folder") / "subfolder" / "file.py"

# Get the user's home directory dynamically — never hardcode it
home = Path.home()
```

- `Path` automatically builds the correct path format for the running OS.
- `Path.home()` ensures compatibility across machines and correct read/write permissions.

---

## Absolute vs. Relative Paths

| Type | Meaning |
|------|---------|
| **Absolute** | Starts from the root (`C:\` or `/`) — full path regardless of where the program runs |
| **Relative** | Relative to the Current Working Directory (CWD) |

- `.` = current directory, `..` = parent directory
- `./file.txt` and `file.txt` are equivalent — the `./` prefix is optional

---

## Programs and Processes

| Term | Meaning |
|------|---------|
| **Program** | Static software stored on disk (e.g., a `.py` file) |
| **Process** | A running instance of a program in memory |

- Multiple processes can run the same program simultaneously (e.g., several calculator windows).
- Each process is fully independent — separate variables, environment variables, and CWD.
- Use Task Manager (Windows/Ubuntu) or Activity Monitor (macOS) to monitor or terminate processes.

### Working Directory

```python
import os

os.chdir("/path/to/folder")  # changes the process's CWD
# raises FileNotFoundError if the path doesn't exist,
# PermissionError if access is denied,
# or NotADirectoryError if the path points to a file
```

---

## Command Line Basics

**CLI vs. GUI:** CLI is text-based, faster, less ambiguous, and ideal for automation.

**Shell:** the program that processes commands — `cmd.exe`/PowerShell (Windows), `bash`/`zsh` (macOS/Linux).

**The Prompt:** the text shown before you type a command — often displays the CWD (e.g., `C:\Users\Al>`).

### The `PATH` Variable

- `PATH` is a list of folders the OS searches when you type a command name.
- If a program isn't in `PATH`: `cd` to its folder, or type its full absolute path.
- Linux filesystems are **case-sensitive**. macOS is typically case-insensitive by default (though this depends on the filesystem format). Windows filesystems are case-insensitive — but note that PowerShell cmdlets themselves are case-insensitive, while Linux shell commands are case-sensitive.

### Arguments and Options

- **Arguments:** data passed to a command (e.g., `C:\Users` in `cd C:\Users`).
- **Options/Flags:** modify behavior — Windows uses `/` (e.g., `/?`), Linux/macOS use `-` or `--` (e.g., `--help`).
- **Spaces in names:** wrap in double quotes — `cd "Vacation Photos"`.

---

## Python from the Command Line

```bash
# Run throwaway code without a .py file
python -c "print('Hello, world')"

# Run a script
python script.py       # Windows
python3 script.py      # macOS/Linux

# Run a specific Python version (Windows Launcher)
py -3.6 -c "import sys; print(sys.version)"
```

### `subprocess` Module

```python
import subprocess

# Recommended — list of separate strings
result = subprocess.run(["ls", "-al"], stdout=subprocess.PIPE)
output = result.stdout.decode()

# Also works but carries shell injection risk — avoid unless necessary
subprocess.run("ls -al", shell=True)
```

A list of arguments is the recommended and safest approach — a single combined string only works with `shell=True`, which introduces security risks.

---

## Listing and Searching Files

```bash
dir              # Windows — list CWD contents
ls                # macOS/Linux — list CWD contents
ls ../other_folder    # list a different folder without navigating to it

ls -l             # long format: permissions, size, date
ls -a             # show hidden files (start with .)
ls -al            # both combined
```

### Recursive Search

```bash
dir /s *.py                 # Windows — search CWD and subfolders
find . -name "*.py"         # Linux/macOS — pattern must be quoted
```

---

## File and Folder Management

| Action | Linux/macOS | Windows |
|--------|------------|---------|
| Copy | `cp source dest` | `copy source dest` |
| Move/Rename | `mv source dest` | `move` / `ren` |
| Delete file | `rm file` | `del file` |
| Create folder | `mkdir name` | `mkdir` / `md` |
| Delete empty folder | `rmdir name` | `rmdir` / `rd name` |
| Delete non-empty folder | `rm -r` / `rm -rf` | `rd /s /q name` |

**Notes:**
- `cp file.txt newname.txt` works even if `newname.txt` doesn't exist yet (this renames while copying). But `cp file.txt backup/` fails if the `backup/` folder doesn't exist — create it first with `mkdir`.
- `rmdir` only works on **empty** folders.
- `del` never deletes folders, even with `/s` — `del /s /q folder\*` deletes files inside the folder (including subfolders) but leaves the folder structure intact. To delete a folder and everything inside it, use `rd /s /q folder`.

### `mv` vs. `git mv`

- Use plain `mv` for untracked files or outside a Git repo.
- Use `git mv` inside a Git repo as a convenience — it stages the rename immediately in one step. Note that Git actually detects renames automatically at commit time based on content similarity, so plain `mv` followed by `git add` achieves the same practical result — `git mv` is simply a shortcut for `mv` + `git add`.

---

## Finding Programs and Clearing the Terminal

```bash
which python      # Linux/macOS — find the executable's absolute path
where python       # Windows equivalent

clear              # Linux/macOS — clear the screen
cls                # Windows equivalent
```

- `which`/`where` searches the `PATH` folders sequentially and returns the exact executable that will run — useful for resolving version conflicts.
- Clearing the screen is purely visual — it does **not** delete command history (`.bash_history` / `.zsh_history` persist across restarts).

---

## Environment Variables

- A set of string values storing systemwide settings accessible to running processes (e.g., `TEMP`, `HOME`).
- Each process gets its own independent copy — changes affect only that process and its children.

```bash
# View all variables
set        # Windows
env        # Linux/macOS

# View a single variable
echo %HOMEPATH%   # Windows
echo $HOME        # Linux/macOS
```

### `PATH` Specifics

- Windows separates folders with `;`; Linux/macOS use `:`.
- The OS scans left to right — the **first match found** is the one that runs.
- Missing command → `command not found` (Linux/macOS) or "not recognized..." (Windows).

**Temporary modification (current terminal only):**
```bash
path C:\newFolder;%PATH%      # Windows cmd.exe — PATH is a built-in command that can display or set the value
set PATH=C:\newFolder;%PATH%  # equivalent alternative in cmd.exe
$env:PATH = "C:\newFolder;$env:PATH"   # PowerShell
PATH=/newFolder:$PATH         # Linux/macOS
```
Permanent changes require updating the OS-level environment variable settings.

---

## Running Python Programs Without the CLI

### Windows

- `WIN-R` → `py C:\path\to\script.py` runs directly (`.exe` optional, `py.exe` already in `PATH`).
- **Batch file (`.bat`)** to avoid typing paths and keep the window open:
  ```bat
  @py.exe C:\path\to\yourScript.py %*
  @pause
  ```
  `@` hides the command display; `%*` forwards arguments to `sys.argv`.

### macOS

- Create a `.command` file:
  ```bash
  #!/usr/bin/env bash
  python3 /path/to/yourScript.py
  ```
- Make it executable: `chmod u+x yourScript.command`
- Launch via Spotlight (`COMMAND-SPACE`) and type the filename.

### Ubuntu Linux

- Add a shebang line as the first line of the `.py` file:
  ```python
  #!/usr/bin/env python3
  ```
- Make it executable: `chmod u+x yourScript.py`
- Run with `./yourScript.py` — the `./` explicitly points to the current directory.

---

## Chapter Summary

- Environment setup requires understanding filesystems, paths, processes, the command line, and environment variables.
- CLI, terminal, shell, and console all refer to text-based command interfaces — functionally similar across OSes with minor naming differences.
- The `PATH` variable is the key to understanding `command not found` errors.
- Comfort with the command line takes time — even experienced developers search for help regularly.