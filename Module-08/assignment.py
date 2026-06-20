# Product Store
# Design & create an online store for products(name, price)
# Track total products being created
# Create a static method to calculate discount on each product based on a % parameter.

class product_store:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        product_store.count += 1

    def get_info(self):
        print(f"{self.name} is having the price of Rs{self.price}")

    @classmethod
    def get_count(self):
        return product_store.count

    @staticmethod
    def claculate_items(price):
        final_price = price - (price * 10/ 100)
        print(f"Your final price is Rs{final_price}")

p1 = product_store("Shoes", 12345)
p2 = product_store("Iphone", 125345)
p3 = product_store("Books", 345)

product_store.get_count()

p1.get_info()
p2.get_info()
p3.get_info()

p1.claculate_items(12345)
