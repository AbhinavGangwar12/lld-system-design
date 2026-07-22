class BreadBaker:
    def __init__(self, name):
        self.name = name

    def bake_bread(self):
        print(f"{self.name} is baking bread.")

    def sell_bread(self):
        print(f"{self.name} is selling bread.")
class InventoryManager:
    def __init__(self, name):
        self.name = name

    def manage_inventory(self):
        print(f"{self.name} is managing inventory.")
class SupplyOrder:
    def __init__(self, name):
        self.name = name

    def order_supplies(self):
        print(f"{self.name} is ordering supplies.")
class CustomerService:
    def __init__(self, name):
        self.name = name

    def handle_customer_queries(self):
        print(f"{self.name} is handling customer queries.")
class BakeryCleaner:
    def __init__(self, name):
        self.name = name

    def clean_bakery(self):
        print(f"{self.name} is cleaning the bakery.")

def main():
    baker = BreadBaker("Alice")
    baker.bake_bread()
    baker.sell_bread()

    inventory_manager = InventoryManager("Bob")
    inventory_manager.manage_inventory()

    supply_order = SupplyOrder("Charlie")
    supply_order.order_supplies()

    customer_service = CustomerService("Diana")
    customer_service.handle_customer_queries()

    cleaner = BakeryCleaner("Eve")
    cleaner.clean_bakery()

if __name__ == "__main__":
    main()
