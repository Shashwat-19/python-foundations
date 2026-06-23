class Person:
    name = "Anonymous"

    # def change_name(self, new_name):
    #     self.new_name = new_name

    @classmethod
    def change_name(cls, name):
        cls.name = name

c1 = Person()
print(c1.name)
c1.change_name("Setu")
print(c1.name)
print(Person.name)