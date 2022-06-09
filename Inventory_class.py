
class Inventory:
    
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {}
        self.item_count = 0
        

    def add_item(self, name, price, quantity):
        if name in self.items:
            print('False')
        
        if self.item_count + quantity > self.max_capacity:
            print (False)
        
        self.items[name] = {"name": name, "price": price, "quantity": quantity}
        self.item_count += quantity
        print (True)

    def delete_item(self, name):
        if name not in self.items:
            print (False)
        
        self.item_count -= self.items[name]["quantity"]
        del self.items[name]
        print("true")

    def get_items_in_price_range(self, min_price, max_price):
        item_names = []
        
        for item in self.items.values():
            name = item['name']
            price = item["price"]
            
            if min_price <= price <= max_price:
                item_names.append(name)
            
        print(item_names)

        

    def get_most_stocked_item(self):
        most_stocked_item = None
        largest_quantity = 0

        for item in self.items.values():
            name = item['name']
            quantity = item['quantity']

            if quantity > largest_quantity:
                most_stocked_item = name
                largest_quantity = quantity
        
        print(most_stocked_item)


i = Inventory(3)
i.add_item('chocolate', 1.99, 1)
i.add_item('milk', 5.99, 2)

i.get_most_stocked_item()

