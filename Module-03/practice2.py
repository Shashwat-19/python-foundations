# Write a program to check if a list contains a palindrome of elements (Hint use .copy()

list1=[1,2,3,9,1]
list2=list1.copy()
list2.reverse()

if (list2 == list1):
    print("It is Palindrone")
else:
    print("no")