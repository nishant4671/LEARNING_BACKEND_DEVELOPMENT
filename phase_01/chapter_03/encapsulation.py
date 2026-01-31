class InventoryItem:
    def __init__(self, name, quantity, price_per_unit, supplier_ids):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.supplier_ids = supplier_ids
        self.__discount = 0.1  # Correct private attribute

    def total_value(self):
        return self.quantity * self.price_per_unit
    
    def get_discounted_price(self):
        return self.price_per_unit * (1 - self.__discount)

class PerishableItem(InventoryItem):  # Note: Capital P
    def __init__(self, name, quantity, price_per_unit, supplier_ids, expiry_date):
        super().__init__(name, quantity, price_per_unit, supplier_ids)
        self.expiry_date = expiry_date
    
    def total_value(self):  # This overrides the parent's total_value
        if self.expiry_date < "2024-05-01":
            return 0
        else:
            return self.quantity * self.price_per_unit
item3 = PerishableItem("Milk", 50, 1.5, [201, 202], "2024-06-15")    
print(item3.total_value())  # Should print 75.0
print(item3.get_discounted_price())  # Should print 1.35
