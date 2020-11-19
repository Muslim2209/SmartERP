class WarehouseActions:
    def __init__(self, product, amount, price=None, customer=None, warehouse_in=None, warehouse_out=None):
        self.product = product
        self.amount = amount
        self.price = price
        self.customer = customer
        self.warehouse_in = warehouse_in
        self.warehouse_out = warehouse_out

    def income(self):
        pass

    def move(self):
        pass

    def sell(self):
        pass
