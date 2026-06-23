# del keyword
class Myself:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"My name is {self.name}")

m1 = Myself("Shashwat")
m1.display()
del m1
print(m1.name)
    #error
    # /Users/shashwat./.pyenv/versions/3.14.2/bin/python3 /Users/shashwat./Desktop/Python myself/py-notion/Module-09/1-del.py
    # My name is Shashwat
    # Traceback (most recent call last):
    #      File "/Users/shashwat./Desktop/Python myself/py-notion/Module-09/1-del.py", line 12, in <module>
    #          print(m1.name)
    #             ^^
    #         NameError: name 'm1' is not defined