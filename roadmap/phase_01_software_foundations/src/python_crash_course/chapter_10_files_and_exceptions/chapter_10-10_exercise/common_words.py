from pathlib import Path

path1 = Path("alice.txt")
path2 = Path("sherlock_holmes.txt")
path3 = Path("time_machine.txt")

for path in [path1, path2, path3]:
    try:
        content = path.read_text(encoding="utf-8")
        count1 = content.lower().count("the")
        count2 = content.lower().count("the ")
    except FileNotFoundError:
        pass
    else:
        display_name = path.stem.replace("_", " ").title()
        print(f"The word 'the' appears {count1} times in the novel {display_name}.")
        print(f"The word 'the' appears {count2} times in the novel {display_name}.")
