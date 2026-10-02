# Chapter 12 — Organizing Your Code Projects with Git

## 1. Version Control

* **Version control** records the history of changes made to a project.
* It allows you to:

  * Save snapshots of your project.
  * Review previous changes.
  * Recover earlier versions.
  * Find when a bug was introduced.
* **Git** is a distributed version control system.
* In a distributed VCS, every developer has a full copy of the repository and its history locally — not just the latest snapshot.
* Commits do not require an internet connection because the full history is stored locally.

---

## 2. Git vs. GitHub

| Tool       | Purpose                                    |
| ---------- | ------------------------------------------ |
| **Git**    | Version control software                   |
| **GitHub** | Website that hosts Git repositories online |

* A **local repository** exists on your computer.
* A **remote repository** can exist on another computer/server, such as GitHub.
* Git can work completely locally; GitHub is not required for basic Git operations.

---

## 3. Creating a Git Repository

```bash
git init
```

* Converts the current folder into a Git repository.
* Creates a hidden `.git` directory.
* `.git` contains Git's repository metadata.
* Do not manually modify files inside `.git`.

Check repository status:

```bash
git status
```

Typical states include:

```text
untracked
modified
staged
committed
```

---

## 4. Working Directory and Repository

Think of Git as tracking changes through several states:

```text
Working Directory
       ↓
     git add
       ↓
 Staging Area
       ↓
   git commit
       ↓
   Repository
```

* **Working directory** — files you are currently editing.
* **Staging area** — changes selected for the next commit.
* **Repository** — committed history stored by Git.

---

## 5. Untracked Files

A newly created file is initially **untracked**.

```bash
git status
```

Git will show files that it is not currently tracking.

Add a file:

```bash
git add filename.py
```

Add all files:

```bash
git add .
```

After `git add`, the files/changes become staged.

---

## 6. Commits

A **commit** is a snapshot of the project's state.

```bash
git commit -m "Add inventory calculation"
```

A good commit message should describe the change clearly.

Avoid vague messages such as:

```text
Updated code
Fixed stuff
Changes
```

Prefer messages that explain what changed:

```text
Add inventory valuation
Fix product quantity validation
Update product selection logic
```

### Good commits

* Should represent a meaningful change.
* Should ideally leave the project in a working state.
* Run tests before committing when tests are available.
* Do not commit code containing obvious syntax errors or broken functionality.

---

## 7. Staging

`git add` selects changes for the next commit.

```bash
git add file.py
git commit -m "Update product validation"
```

Git allows changes to be staged separately from other modifications.

For modified tracked files, the book also introduces:

```bash
git commit -am "Fix currency conversion bug"
```

`-a` stages modified/deleted tracked files before committing.

> `git commit -am` does **not** add brand-new untracked files.

> To modify the most recent commit (message or staged changes), use `git commit --amend`. This rewrites the last commit rather than creating a new one — avoid using it on commits already pushed to a shared remote.

---

## 8. Why Commits Matter

Commits create checkpoints in the project's history.

```text
Commit A
   ↓
Commit B
   ↓
Commit C
   ↓
Commit D
```

You can inspect previous commits and recover earlier versions.

A commit has a unique **hash**.

Example:

```text
962a8ba
```

The full hash is longer, but Git commonly displays a shortened version.

---

## 9. Viewing Commit History

```bash
git log
```

A shorter version:

```bash
git log --oneline
```

Limit the number of commits:

```bash
git log --oneline -n 3
```

Useful information includes:

* Commit hash
* Commit message
* Branch
* Position of `HEAD`

---

## 10. Viewing Changes

Show unstaged changes:

```bash
git diff
```

`git diff` shows unstaged changes — differences between the working directory and the staging area.

The output commonly shows:

```text
- removed lines
+ added lines
```

The chapter also introduces GUI diff tools such as WinMerge, Meld, Kompare, and tkdiff.

---

## 11. `.gitignore`

A `.gitignore` file tells Git which files should not be tracked.

Common examples:

```text
__pycache__/
*.pyc
.venv/
```

Files commonly ignored include:

* Temporary files
* Python-generated files
* Build/generated files
* Tool-generated directories
* Authentication tokens
* Passwords
* Other sensitive information

Example:

```gitignore
__pycache__/
*.py[cod]
.venv/
secrets.txt
```

Important:

* `.gitignore` itself should normally be committed.
* Ignoring a file prevents it from being accidentally added.
* `.gitignore` does not erase a file that has already been committed.

---

## 12. Sensitive Information

Never commit sensitive information such as:

```text
passwords
API keys
authentication tokens
credit card numbers
```

A common approach is to keep sensitive values in a separate file and add that file to `.gitignore`.

Example:

```gitignore
secrets.txt
```

If sensitive information has **already been committed**, simply deleting it in a later commit is not enough because the old commit remains in repository history.

Removing sensitive data from Git history requires specialized procedures/tools.

---

## 13. Deleting Files

Use Git when removing a tracked file:

```bash
git rm filename.py
```

`git rm`:

1. Removes the file from the working directory.
2. Stages the deletion.

Then commit:

```bash
git commit -m "Remove obsolete file"
```

The deleted file still exists in Git's history and can potentially be recovered.

---

## 14. Renaming and Moving Files

Use Git when renaming or moving tracked files.

The chapter demonstrates Git-aware file movement so Git can properly track the change.

```bash
git mv old_name.py new_name.py
```

`git mv` renames or moves the file and stages the change in one step.

The important idea is:

```text
Old filename
      ↓
Renamed/moved
      ↓
Git records the change
```

---

## 15. Recovering Uncommitted Changes

If you modified a file but have not committed the changes, you can restore it to the latest committed version:

```bash
git restore filename.py
```

This restores the file to the version in the most recent commit (HEAD), discarding all uncommitted changes.

Be careful: discarded uncommitted changes may be difficult or impossible to recover.

---

## 16. Recovering Previous Versions

Git keeps previous versions in its history.

View a file from a specific commit:

```bash
git show <commit_hash>:<filename>
```

Restore a particular file from an old commit:

```bash
git checkout <commit_hash> -- <filename>
```

Then stage and commit the restored version:

```bash
git add <filename>
git commit -m "Restore filename from previous version"
```

---

## 17. Reverting Commits

Git generally preserves history rather than deleting it.

`git revert` creates a **new commit** that reverses the effect of an earlier commit. It does not delete or rewrite history — the original commit remains intact.

Example:

```bash
git revert <commit_hash>
```

Conceptually:

```text
Original commit
       ↓
Later commits
       ↓
Revert commit
       ↓
Changes are undone
```

The original commit remains in the history.

---

## 18. Git History Is Append-Oriented

A useful mental model:

```text
Commit A
   ↓
Commit B
   ↓
Commit C
   ↓
Revert C
```

The old commits still exist.

A revert adds another commit that changes the project's state.

This is different from simply deleting historical information.

---

## 19. Rolling Back Several Commits

The chapter demonstrates reverting multiple commits together.

Example:

```bash
git revert -n HEAD~3..HEAD
```

Then:

```bash
git add .
git commit -m "Start over from previous version"
```

The important concept is that multiple previous changes can be reversed while preserving the existing history.

---

## 20. Rolling Back One File

A commit represents the state of the **repository**, not just one file.

To inspect a file from an earlier commit:

```bash
git show <hash>:<filename>
```

To restore that file:

```bash
git checkout <hash> -- <filename>
```

Then:

```bash
git add <filename>
git commit -m "Restore filename"
```

Other files remain unchanged.

---

## 24. How Often Should You Commit?

The chapter discusses the trade-off:

### Too frequently

* Creates many insignificant commits.
* Makes history harder to navigate.

### Too infrequently

* Creates very large commits.
* Makes it harder to identify or undo a specific change.

General principle:

> Commit meaningful, working changes rather than every tiny edit.

---

## 25. Cookiecutter

**Cookiecutter** is introduced as a tool for creating project templates.

It can generate a starting project structure containing files such as:

```text
project/
├── README.md
├── .gitignore
├── LICENSE
├── source files
└── configuration files
```

The generated project can then be placed under Git version control.

The chapter uses a Python project template as its example.

---

## 26. Git Configuration

After installing Git, configure the author information used by commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

View configuration:

```bash
git config --list
```

The configuration is stored in the user's Git configuration file.

---

## 27. Git GUI Tools

The chapter focuses on the Git command line but also discusses GUI tools.

Examples include:

* TortoiseGit
* GitHub Desktop
* GitExtensions
* WinMerge
* Meld
* Kompare
* tkdiff

GUI tools can make some operations easier, but the chapter emphasizes that learning the Git command line is still important.

Configure a diff tool:

```bash
git config diff.tool <tool_name>
```

Use it:

```bash
git difftool <filename>
```

---

## 28. GitHub

GitHub can host an online copy of a Git repository.

Benefits include:

* Online backup
* Sharing projects
* Collaboration
* Remote access
* Sharing commits with other developers

Remember:

```text
Git     → version control software
GitHub  → online hosting/service for Git repositories
```

---

## 29. Remote Repositories

A local repository can be connected to a remote repository.

Example:

```bash
git remote add origin https://github.com/<username>/<repo>.git
```

Here:

```text
origin → name of the remote repository
```

---

## 30. Pushing to GitHub

Send local commits to the remote repository:

```bash
git push -u origin main
```

> Note: modern repositories use `main` as the default branch name. Older repositories may use `master`. The `-u` flag sets the upstream tracking branch so future `git push` calls work without arguments.

After the first push:

```bash
git push
```

The remote repository then contains the commits pushed from the local repository.

---

## 31. Cloning a Repository

You can create a local copy of an existing remote repository:

```bash
git clone https://github.com/<username>/<repo>.git
```

`git clone`:

* Downloads the repository.
* Creates a local working copy.
* Includes the repository's Git history.
* Configures the cloned repository to work with the remote.

---

## 32. Local vs. Remote Workflow

A common workflow is:

```text
Edit files
    ↓
git status
    ↓
git add
    ↓
git commit
    ↓
git push
    ↓
GitHub
```

To obtain an existing repository:

```text
GitHub
   ↓
git clone
   ↓
Local repository
```

---

## 33. Core Git Commands

| Command             | Purpose                                                        |
| ------------------- | -------------------------------------------------------------- |
| `git init`          | Create a Git repository                                        |
| `git status`        | Show repository status                                         |
| `git add`           | Stage changes                                                  |
| `git commit`        | Create a commit                                                |
| `git log`           | View commit history                                            |
| `git log --oneline` | Compact commit history                                         |
| `git diff`          | View changes                                                   |
| `git restore`       | Restore uncommitted changes                                    |
| `git rm`            | Remove a tracked file                                          |
| `git show`          | Inspect a commit/object                                        |
| `git revert`        | Create a commit that reverses changes                          |
| `git checkout`      | Used in the chapter for restoring files/working with revisions |
| `git remote add`    | Add a remote repository                                        |
| `git push`          | Send commits to a remote                                       |
| `git clone`         | Copy a remote repository locally                               |

---

## 34. Core Mental Model

```text
Git
│
├── Repository
│   └── Project history
│
├── Working Directory
│   └── Current files
│
├── Staging Area
│   └── Changes selected for next commit
│
├── Commit
│   └── Snapshot of project state
│
├── Branch
│   └── Separate line of development
│
└── Remote
    └── Repository hosted elsewhere
```

### Basic Workflow

Create/Edit
    ↓
git status
    ↓
git add
    ↓
Staging Area
    ↓
git commit
    ↓
Repository
    ↓
git push
    ↓
Remote / GitHub
