"""
Chapter 12 — Organizing Your Code Projects with Git
Beyond the Basic Stuff with Python

This file tells the story of a small Python project as we start using Git
to organize, track, recover, and share our code.
"""


# ============================================================
# 1. We Have a Python Project
# ============================================================

# We start with a normal project folder.

project_name = "warehouse_sales_system"

print(f"Working on: {project_name}")


# ============================================================
# 2. Version Control
# ============================================================

# We are going to change our project many times.
# Version control keeps a history of those changes.

product = {
    "name": "Keyboard",
    "price": 1000,
    "quantity": 10,
}

print(product)

# If we make a mistake later, Git can help us return
# to an earlier version of the project.


# ============================================================
# 3. Git Is Distributed Version Control
# ============================================================

# In a distributed VCS, every developer has a full copy
# of the repository and its complete history locally.
# We do not need the internet to create commits.

# Local repository:
#
#     Our computer
#          |
#          +-- Git repository
#
# Remote repository:
#
#     Another computer / GitHub
#
# We can work locally and later share our commits.


# ============================================================
# 4. Create a Git Repository
# ============================================================

# From the terminal, we enter the project folder and run:
#
#     git init
#
# Git creates a hidden .git directory.
#
# The .git directory contains Git's repository metadata.
#
# We should not manually modify files inside .git.


# ============================================================
# 5. Check the Repository
# ============================================================

# We use:
#
#     git status
#
# to see what is happening in the repository.

print("Git status helps us see the current state of the project.")


# ============================================================
# 6. The Three Important Areas
# ============================================================

# Git can be understood using three main areas:
#
#     Working Directory
#             |
#          git add
#             ↓
#       Staging Area
#             |
#        git commit
#             ↓
#        Repository
#
# Working Directory:
#     The files we are currently editing.
#
# Staging Area:
#     Changes selected for the next commit.
#
# Repository:
#     The committed project history.


# ============================================================
# 7. New Files Start as Untracked
# ============================================================

# Imagine we create a new file:

new_file = "inventory.py"

# Git initially sees this file as untracked.
#
# To start tracking it:
#
#     git add inventory.py
#
# Or to add all appropriate files:
#
#     git add .


# ============================================================
# 8. Staging Changes
# ============================================================

# We modify our product:

product["quantity"] = 15

print(product)

# The change is currently in the working directory.
#
# We can stage it with:
#
#     git add inventory.py
#
# The staged version is what Git will include
# in the next commit.


# ============================================================
# 9. Commit Our First Snapshot
# ============================================================

# A commit is a snapshot of the project at a point in time.
#
# We can create one with:
#
#     git commit -m "Update product quantity"
#
# A good commit message explains what changed.

commit_message = "Update product quantity"

print(f"Commit: {commit_message}")


# ============================================================
# 10. Good Commits
# ============================================================

# A commit should represent a meaningful change.
#
# Avoid vague messages:
#
#     "Updated code"
#     "Changes"
#     "Fixed stuff"
#
# Prefer messages such as:
#
#     "Add inventory valuation"
#     "Fix product quantity validation"
#     "Update product selection logic"
#
# The goal is to understand the commit later.


# ============================================================
# 11. Keep the Project Working
# ============================================================

# Before committing, we should make sure the program is not
# obviously broken.
#
# Ideally:
#
#     run the program
#     run the tests
#     check the result
#     then commit
#
# A useful commit should leave us with a working checkpoint.


# ============================================================
# 12. git commit -am
# ============================================================

# For already tracked files, Git also provides:
#
#     git commit -am "Fix inventory calculation"
#
# The -a option stages modified and deleted tracked files.
#
# IMPORTANT:
# -am does NOT stage brand-new untracked files.
#
# New files still need:
#
#     git add new_file.py
#
# To modify the most recent commit (message or staged changes):
#
#     git commit --amend
#
# This rewrites the last commit rather than creating a new one.
# Avoid using --amend on commits already pushed to a shared remote.


# ============================================================
# 13. Commit History
# ============================================================

# Every commit has a unique hash.
#
# Example:
#
#     962a8ba
#
# We can view the history with:
#
#     git log
#
# Or use the shorter version:
#
#     git log --oneline

print("Git history contains our previous project snapshots.")


# ============================================================
# 14. Reading the Commit History
# ============================================================

# A history might look like:
#
#     a1b2c3d Add inventory report
#     7f8e9a0 Fix product validation
#     4d5e6f7 Add product status
#     123abcd Initial project
#
# Each commit gives us another point in the project's history.


# ============================================================
# 15. Limit the Log
# ============================================================

# If the history is very long:
#
#     git log --oneline -n 3
#
# shows only the most recent three commits.


# ============================================================
# 16. See Changes with git diff
# ============================================================

# We change the price:

product["price"] = 1200

print(product)

# Before committing, we can inspect the change:
#
#     git diff
#
# git diff shows unstaged changes — differences between
# the working directory and the staging area.


# ============================================================
# 17. The .gitignore File
# ============================================================

# Some files should not be tracked.
#
# Examples:
#
#     __pycache__/
#     *.pyc
#     .venv/
#     secrets.txt
#
# We put these patterns in:
#
#     .gitignore
#
# Example .gitignore:
#
#     __pycache__/
#     *.py[cod]
#     .venv/
#     secrets.txt
#
# The .gitignore file itself should normally be committed.


# ============================================================
# 18. Why Ignore Generated Files?
# ============================================================

# Python can generate files such as:
#
#     __pycache__/
#     *.pyc
#
# These files can be generated again.
#
# The repository should normally contain the source code,
# not unnecessary generated files.


# ============================================================
# 19. Never Commit Secrets
# ============================================================

# Imagine we need a password or API key.

database_password = "DO_NOT_PUT_REAL_PASSWORDS_HERE"

# Sensitive information should not be placed directly
# in source code that will be committed.
#
# Instead, keep it in a separate private file and ignore it:
#
#     secrets.txt
#
# .gitignore:
#
#     secrets.txt


# ============================================================
# 20. Important Warning About Secrets
# ============================================================

# If a secret was already committed, simply deleting it
# from the current file is NOT enough.
#
# The old commit can still contain the secret.
#
# To stop tracking a file that was accidentally committed:
#
#     git rm --cached secrets.txt
#
# Then add secrets.txt to .gitignore and commit the change.
# Note: this removes the file from future tracking,
# but the old commits still contain the secret.
# Removing it from full Git history requires more advanced tools.


# ============================================================
# 21. Delete a Tracked File
# ============================================================

# Suppose we no longer need old_file.py.
#
# We should use:
#
#     git rm old_file.py
#
# Git removes the file and stages the deletion.
#
# Then:
#
#     git commit -m "Remove old file"


# ============================================================
# 22. Rename or Move Files
# ============================================================

# When working with tracked files, use Git-aware operations
# for renaming or moving files.
#
#     git mv old_name.py new_name.py
#
# This renames the file and stages the change in one step.
# The important idea is that Git should know about the change.


# ============================================================
# 23. Undo Uncommitted Changes
# ============================================================

# Imagine we change a file but do not commit it.

product["price"] = 999999

print(product)

# If we decide that we do not want this uncommitted change:
#
#     git restore inventory.py
#
# This restores the file to the version in the most recent
# commit (HEAD), discarding all uncommitted changes.
#
# Be careful:
# discarded uncommitted changes may be impossible to recover.


# ============================================================
# 24. Git Remembers Older Versions
# ============================================================

# Git does not only know the current version.
# It remembers previous commits.
#
# We can inspect a file from an older commit:
#
#     git show <commit_hash>:<filename>


# ============================================================
# 25. Restore One File from an Old Commit
# ============================================================

# We can restore a particular file from an old commit:
#
#     git checkout <commit_hash> -- inventory.py
#
# Then:
#
#     git add inventory.py
#     git commit -m "Restore inventory file"
#
# Only that file is restored;
# other files do not have to be changed.


# ============================================================
# 26. Reverting a Commit
# ============================================================

# Suppose a commit introduced a bug.
#
# Instead of deleting the old commit, Git can create
# a new commit that reverses its changes.
#
#     git revert <commit_hash>
#
# git revert does NOT delete or rewrite history.
# The original commit remains intact.


# ============================================================
# 27. Git History Is Preserved
# ============================================================

# Imagine this history:
#
#     Commit A
#        ↓
#     Commit B
#        ↓
#     Commit C
#
# If we revert C:
#
#     Commit A
#        ↓
#     Commit B
#        ↓
#     Commit C
#        ↓
#     Revert C
#
# The original C still exists.
# The new commit simply reverses its effect.


# ============================================================
# 28. Revert Several Changes
# ============================================================

# The chapter also shows that several commits can be reverted.
#
# Example:
#
#     git revert -n HEAD~3..HEAD
#
# Then:
#
#     git add .
#     git commit -m "Start over from previous version"
#
# This creates a new commit that reverses those changes.


# ============================================================
# 29. Commit Size
# ============================================================

# We should not commit every tiny character change.
#
# But we also should not wait until the project contains
# hundreds of unrelated changes.
#
# A useful commit represents a meaningful unit of work.
#
# Example:
#
#     Add product barcode support
#
# is better than:
#
#     Updated code


# ============================================================
# 30. Cookiecutter
# ============================================================

# Cookiecutter can create a new project from a template.
#
# It can provide a starting structure such as:
#
#     project/
#     ├── README.md
#     ├── .gitignore
#     ├── LICENSE
#     ├── source/
#     └── configuration files
#
# This gives a project a consistent starting point.


# ============================================================
# 31. Configure Git
# ============================================================

# Git commits contain author information.
#
# Configure the username:
#
#     git config --global user.name "Your Name"
#
# Configure the email:
#
#     git config --global user.email "you@example.com"
#
# View configuration:
#
#     git config --list


# ============================================================
# 32. Git GUI and Diff Tools
# ============================================================

# Git can be used from the command line.
#
# The chapter also discusses GUI tools that can make
# Git operations and diffs easier to inspect.
#
# Git can be configured to use an external diff tool:
#
#     git config diff.tool <tool_name>
#     git difftool <filename>
#
# To avoid being prompted every time difftool is launched:
#
#     git config --global difftool.prompt false
#
# The important point is:
# a GUI is another way to interact with Git;
# Git remains the version control system.


# ============================================================
# 33. GitHub
# ============================================================

# Our Git repository can exist only on our computer.
#
# But we can also host a copy online.
#
# GitHub is a website that hosts Git repositories.
#
# Remember:
#
#     Git     = version control software
#     GitHub  = online hosting/service for Git repositories


# ============================================================
# 34. Remote Repository
# ============================================================

# A remote repository is another copy of the repository,
# usually hosted somewhere online.
#
# We can connect our local repository to it:
#
#     git remote add origin <repository-url>
#
# "origin" is the common name for the remote.


# ============================================================
# 35. Push Local Commits
# ============================================================

# After committing locally, we can send commits to GitHub:
#
#     git push -u origin main
#
# Note: modern repositories use 'main' as the default branch name.
#
# Later, after the remote tracking relationship is configured:
#
#     git push
#
# Now the remote repository contains our pushed commits.


# ============================================================
# 36. Clone a Repository
# ============================================================

# Someone can download an existing Git repository with:
#
#     git clone <repository-url>
#
# Cloning creates a local copy containing:
#
#     project files
#     Git history
#     remote connection


# ============================================================
# 37. The Complete Local Workflow
# ============================================================

# We edit our project:

product["quantity"] = 20

print(product)

# Then the normal workflow is:
#
#     git status
#     git add .
#     git commit -m "Update product quantity"
#
# If we use GitHub:
#
#     git push


# ============================================================
# 38. The Complete Collaboration Workflow
# ============================================================

# A simplified workflow looks like this:
#
#     Edit
#       ↓
#     git status
#       ↓
#     git add
#       ↓
#     git commit
#       ↓
#     Local repository
#       ↓
#     git push
#       ↓
#     GitHub
#
# Another developer can:
#
#     git clone
#
# and get a local copy of the project.


# ============================================================
# 39. Our Warehouse Project
# ============================================================

# Now imagine applying everything to our Warehouse System.
#
# We start with:
#
#     warehouse_sales_system/
#
# Git tracks the project history.
#
# Example history:
#
#     Initial WMS structure
#            ↓
#     Add product validation
#            ↓
#     Add product status
#            ↓
#     Add inventory valuation
#            ↓
#     Add JSON persistence


# ============================================================
# 40. Final Mental Model
# ============================================================

# Think of Git as a history machine for your project.
#
# Working Directory
#     = What I am currently editing
#
# Staging Area
#     = What I want in the next snapshot
#
# Commit
#     = A saved project snapshot
#
# Repository
#     = The complete history of snapshots
#
# Remote
#     = Another copy of the repository
#
# GitHub
#     = A service that hosts Git repositories
#
# Push
#     = Send local commits to a remote
#
# Clone
#     = Create a local copy of a remote repository


# ============================================================
# 41. The Core Git Story
# ============================================================

# We write code.
#
#     ↓
#
# Git sees changes.
#
#     ↓
#
# We inspect them.
#
#     git status
#
#     ↓
#
# We select changes.
#
#     git add
#
#     ↓
#
# We create a snapshot.
#
#     git commit
#
#     ↓
#
# Git remembers the snapshot.
#
#     ↓
#
# We can inspect history.
#
#     git log
#
#     ↓
#
# We can recover or reverse changes when necessary.
#
#     git restore
#     git checkout
#     git revert
#
#     ↓
#
# We can share the repository online.
#
#     git push
#
#     ↓
#
#     GitHub
#
#     ↓
#
# Other developers can obtain a copy.
#
#     git clone


# ============================================================
# END OF CHAPTER 12
# ============================================================
