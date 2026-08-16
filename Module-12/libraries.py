# # Import
# import random
# coin = random.choice(["Heads", "Tails"])
# print(coin)
#
#
# # from
# from random import choice
# print(choice(["Heads", "Tails"]))
#
#
# # randint is a function in the random module that
# # returns a random integer between two specified values (inclusive).
# # It is used to generate random numbers within a given range.
# from random import randint
# print(randint(1, 100))
#
#
# # shuffle is a function in the random module that randomly shuffles the elements of a list in place.
# # It modifies the original list and does not return a new list.
# from random import shuffle
# my_list = [1, 2, 3, 4, 5]
# shuffle(my_list)
# print(my_list)
#
# # also you can use the random module to shuffle a list of cards. Here's an example:
# import random
# cards = ["jack", "queen", "king", "ace"]
# random.shuffle(cards)
# for card in cards:
#     print(card)
#
# # Statistics module
# # The statistics module in Python provides functions for calculating mathematical statistics of numeric data.
# # It includes functions for calculating mean, median, mode, variance, standard deviation, and other
# import statistics
# print(f" The mean is {statistics.mean([100,90,45,98,99,56,78,89,67,45,34,23,12,11,10]):.2f}")
#
#
# # Sys module
# # The sys module in Python provides access to some variables used or maintained by the interpreter and to
# # functions that interact strongly with the interpreter. It allows you to manipulate the Python runtime environment.
# import sys
# print(f"Python version: {sys.version}")
# print(f"Python version info: {sys.version_info}")
# print("hello, my name is", sys.argv[1])  # Accessing command line arguments
#
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
#
# for arg in sys.argv[1:]:
#     print(f"Hello, {arg}")
#
#
# # pakages
# # A package is a way of organizing related modules in Python. It is a directory that contains a special file called __init__.py,
# # which indicates that the directory is a package. Packages can contain sub-packages and modules, allowing for a hierarchical organization of code.
# import cowsay
# cowsay.trex("Hi Bhondu...")
# cowsay.daemon("Hi Bhondu...")
# cowsay.octopus("Hi Bhondu...")
# cowsay.ghostbusters("Hi Bhondu...")
# cowsay.dragon("Hi Bhondu...")


