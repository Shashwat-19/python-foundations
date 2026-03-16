# ## 📋 Level 3 — Strings

# 11. Input a string and print it in **reverse**.
# 12. Input a sentence and count the **number of words** in it.
# 13. Input a string and check if it's a **palindrome** _(e.g., "racecar")_.
# 14. Input a string and print only the **uppercase letters** from it.
# 15. Input a username and check if it contains **any digit** — if yes, print `"Valid username"`, else `"Invalid username"`.

#11.
str = input("Enter your Name: ")
print(str[::-1])

#12.
name = input("Enter your name: ")
print(name.count(" "))  