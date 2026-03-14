# 🐍 Python Practice Questions — Complete Roadmap

> 📺 Source: Apna College – Python Full Course
> ✅ Topics: I/O · Conditionals · Strings · Lists · Dicts & Sets · Loops · Functions · File I/O · OOP

---

## 🔢 Level 1 — Basics & Arithmetic

1. Take two numbers as input and print their **product, difference, and quotient**.
2. Input the **radius of a circle** and print its area and circumference. _(Use `math.pi`)_
3. Input a **temperature in Celsius** and convert it to Fahrenheit.
4. Input a person's **weight (kg) and height (m)** and calculate their BMI.
5. Input the **length and breadth** of a rectangle and print its area and perimeter.

---

## 🔀 Level 2 — Conditionals

6. Input a **year** and check if it's a **leap year**.
7. Input **three sides of a triangle** and check if it's valid _(sum of any two sides > third)_.
8. Input a **character** and check if it's a **vowel or consonant**.
9. A shopkeeper gives discount based on purchase amount:
   - Above ₹5000 → 20% off
   - ₹2000–₹5000 → 10% off
   - Below ₹2000 → No discount

   Print the **final amount payable**.

10. Input a number and check if it's **positive, negative, or zero**.

---

## 📋 Level 3 — Strings

11. Input a string and print it in **reverse**.
12. Input a sentence and count the **number of words** in it.
13. Input a string and check if it's a **palindrome** _(e.g., "racecar")_.
14. Input a string and print only the **uppercase letters** from it.
15. Input a username and check if it contains **any digit** — if yes, print `"Valid username"`, else `"Invalid username"`.

---

## 📦 Level 4 — Lists & Tuples

16. Input 5 numbers into a list and print the **maximum and minimum**.
17. Input names of 5 students and print the list in **alphabetical order**.
18. Create a list of 10 numbers and print only the **even numbers** from it.
19. Input items into a shopping cart (list) until user types `"done"`, then print the **full cart and total count**.
20. Given a list `[3, 1, 4, 1, 5, 9, 2, 6, 5]`, remove all **duplicate elements** and print the result.

---

## 🗂️ Level 5 — Dictionaries & Sets

21. Store the following word meanings in a Python dictionary:
    - `"table"` → `"a piece of furniture"`, `"list of facts and figures"`
    - `"cat"` → `"a small animal"`
22. You are given a list of subjects for students. Assume one classroom is required per subject. Write a program to find how many **unique classrooms** are needed. _(Hint: Use a set)_
23. Write a program to input marks for **3 subjects** from the user and store them in a dictionary. Start with an **empty dictionary**.
24. Find a way to store `9` and `99.0` as **separate values** in a set. _(Hint: Use strings or tuples to differentiate them)_

---

## 🔁 Level 6 — Loops (While & For)

25. Print numbers from **1 to 100** using a loop.
26. Print numbers from **100 to 1** (reverse order) using a loop.
27. Print the **multiplication table** of a number `n` entered by the user.
28. Print all **elements of a given list** using a loop.
29. Search for a specific number `x` in a given **tuple** using a loop _(Linear Search)_.
30. Find the **sum of first `n` natural numbers** using a loop.
31. Find the **factorial of first `n` natural numbers** using a loop.

---

## ⚙️ Level 7 — Functions & Recursion

32. Write a function to **print the length of a list** _(list passed as parameter)_.
33. Write a function to **print all elements of a list in a single line**. _(Hint: use `end` parameter in `print()`)_
34. Write a function to **calculate the factorial** of a number `n`.
35. Write a function to **convert USD to INR**.
36. Write a function that takes a number and returns `"ODD"` or `"EVEN"`.
37. Write a **recursive function** to calculate the **sum of first `n` natural numbers**.
38. Write a **recursive function** to print all elements in a list.

---

## 📁 Level 8 — File I/O

39. Create a new text file `practice.txt` using Python and **write a few lines** of data into it.
40. Write a function that reads the file and **replaces all occurrences** of `"java"` with `"python"`.
41. Write a program to **search if the word `"learning"` exists** in the file or not.
42. Write a function to find the **exact line number** where `"learning"` first occurs.
43. From a file containing numbers separated by commas (e.g., `1, 2, 76, 84, 90`), extract the numbers and **count how many are even**.

---

## 🏗️ Level 9 — Object-Oriented Programming (OOP)

44. Define a `Circle` class with:
    - Constructor that takes radius `r`
    - `area()` method
    - `perimeter()` method
45. Define an `Employee` class with attributes `role`, `department`, `salary` and a `showDetails()` method.
    Then create an `Engineer` class that **inherits** from `Employee` and adds `name` and `age`.
46. Create an `Order` class that stores `item` and `price`.
    **Overload the `>` operator** using `__gt__()` so two Order objects can be directly compared by price.

---

## 🧩 Bonus Challenges (Mix of Everything)

47. Build a **simple calculator** — input two numbers and an operator (`+`, `-`, `*`, `/`) and display the result.
48. Input marks for 10 students and **count how many got A, B, C, D, and F** grades.
49. Input a sentence and **replace every space with `_`**.
50. Check if a number is a **perfect number** _(e.g., 6 = 1+2+3)_.
51. Build a **mini login system** — store a username & password, ask the user to enter them, and print `"Access Granted"` or `"Access Denied"`.

---

## 🚀 Study Roadmap

| Step | Topic              | Key Concepts                                   |
| ---- | ------------------ | ---------------------------------------------- |
| ✅ 1 | **Basics & I/O**   | `input()`, `print()`, operators                |
| ✅ 2 | **Conditionals**   | `if`, `elif`, `else`                           |
| ✅ 3 | **Strings**        | indexing, slicing, methods                     |
| ✅ 4 | **Lists & Tuples** | `.append()`, `.sort()`, `.copy()`              |
| 🔲 5 | **Dicts & Sets**   | `{}`, `.keys()`, `.values()`, uniqueness       |
| 🔲 6 | **Loops**          | `for`, `while`, `range()`, `break`, `continue` |
| 🔲 7 | **Functions**      | `def`, `return`, recursion                     |
| 🔲 8 | **File I/O**       | `open()`, `read()`, `write()`                  |
| 🔲 9 | **OOP**            | classes, objects, inheritance, dunder methods  |

---

> 💡 _Tip: Solve at least 5 questions a day. Check off each topic as you go. You've got this! 🚀_
