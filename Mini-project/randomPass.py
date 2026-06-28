import random, string
values = string.ascii_letters + string.digits + string.punctuation
password = "".join([random.choice(values) for i in range(1, 13)])
print(f"Your password is : {password}")