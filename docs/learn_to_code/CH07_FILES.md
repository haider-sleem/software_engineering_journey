## Notes on File Handling and Debugging
1. File Modes: open(filename, mode)

'r' (Read): Used to open a file for reading. The file must exist, or Python will throw an error.

'w' (Write): Used to open a file for writing. If the file doesn't exist, Python creates it. If it already exists, it overwrites (deletes) all its previous content.

'a' (Append): Used to add new data to the end of an existing file without deleting its current content.

2. Viewing Raw Content: repr()

repr(string): This function returns the "raw" or "internal" representation of a string.

Unlike print(), which executes special characters (like \n creating a new line), repr() displays them explicitly so you can see them (e.g., it shows '12 13\n' instead of just printing the numbers and jumping to a new line). It is a great tool for debugging and verifying exactly what is inside your string.


3. Open files when needed and close them immediately to ensure data safety and efficient memory usage.

---

4. Advanced File Modes (`+` Modes)

Adding a `+` to the file opening mode (`r+`, `w+`, `a+`) enables both reading and writing simultaneously. The core behavior still depends on the original mode:

* **`r+`**: Opens for reading and writing without clearing the file content. The pointer starts at the beginning of the file.
* **`w+`**: Opens for reading and writing but clears the entire file content upon opening.
* **`a+`**: Opens for reading and writing without clearing the content. Writing always occurs at the end of the file.

The `+` sign does not change the original mode's behavior regarding clearing content or pointer position; it simply adds the missing capability (either reading or writing).

---


### Useful Python Tips for Competitive Programming

#### 1. The `abs()` Function

The `abs()` function stands for **absolute value**. It converts any negative number into its positive counterpart and leaves positive numbers unchanged.

* **Why it's useful:** In many problems, you need to calculate the distance between two points on a number line. Since distance is always positive, `abs(x - y)` ensures you get the correct result regardless of which number is larger.
* **Example:** `abs(3 - 6)` returns `3`, and `abs(6 - 3)` also returns `3`.

#### 2. Using `min()` and `max()` for Comparison

When you need to find the range between two points (`x` and `y`) without using complex `if-else` statements to check which one is larger, you can use these built-in functions:

* **`min(x, y)`:** Returns the smaller of the two numbers.
* **`max(x, y)`:** Returns the larger of the two numbers.
* **Why it's useful:** It makes your code cleaner and helps you define boundaries (like checking if a value lies between two points) without worrying about the order of the variables.
* **Example:** If you want to check if a point `target` is between `x` and `y` and you don't know which one is bigger, you can simply write: `if min(x, y) <= target <= max(x, y):`.

---

