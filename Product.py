class Product:
    product_name = ''
    product_quantity = 0
    product_cost = 0
    product_description = ''

    def __init__(self, name = '', quantity = 0, cost = 0, description = ''):
        self.product_name = name
        self.product_quantity = quantity
        self.product_cost = cost
        self.product_description = description

    def get_name(self):
        return self.product_name

    def get_quantity(self):
        return self.product_quantity

    def set_quantity(self, quantity = 0):
        self.product_quantity = quantity

    def get_cost(self):
        return self.product_cost

    def set_cost(self, cost = 0.0):
        self.product_cost = cost

    def get_description(self):
        return self.product_description

    def set_description(self, description = ''):
        self.product_description = description

    def get_total(self):
        return self.product_cost * self.product_quantity