class BackAccount:
    def __init__(self, acc_no, password): #public attribute
        self.acc_no = acc_no
        self.password = password

acc1 = BackAccount(acc_no="123", password="setu")
print(acc1.acc_no)
print(acc1.password)


class Person:  #private
    __name = "anonymous"

    def __hello(self):
        print("hello world " + self.__name)

    def welcome(self):
        self.__hello()

p1 = Person()
p1.welcome()