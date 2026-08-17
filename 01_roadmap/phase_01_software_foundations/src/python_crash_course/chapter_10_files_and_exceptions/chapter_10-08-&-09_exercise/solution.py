# # 10-8. Cats and Dogs:
# from pathlib import Path

# path1 = Path("cats.txt")
# path2 = Path("dogs.txt")
# path3 = Path("birds.txt")

# for path in [path1, path2, path3]:
#     try:
#         contents = path.read_text()

#     except FileNotFoundError:
#         print(f"Please, enter a correct path for {path.stem} file.")

#     else:
#         print(f"{path.stem.capitalize()}' Names are:\n{contents}")


# # 10-9. Silent Cats and Dogs:
# from pathlib import Path

# path1 = Path("cats.txt")
# path2 = Path("dogs.txt")
# path3 = Path("birds.txt")

# for path in [path1, path2, path3]:
#     try:
#         contents = path.read_text()

#     except FileNotFoundError:
#         pass

#     else:
#         print(f"{path.stem.capitalize()}' Names are:\n{contents}")
