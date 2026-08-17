from pathlib import Path

# 10-4. Guest
name = input("what is your name ? ")
path = Path("guest.txt")
path.write_text(name)
