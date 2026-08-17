# TRY IT YOURSELF page 227
from pathlib import Path

# 10-1. Learning Python
path = Path("learning_python.txt")
contents = path.read_text()

print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)


# 10-2. Learning C
for line in lines:
    print(line.replace("Python", "C"))


# 10-3. Simpler Code
for line in contents.splitlines():
    print(line)

for line in contents.splitlines():
    print(line.replace("Python", "C"))
