# OCP: The Open-Closed Principle

# (2017) A software artifact should be open for extension but
# closed for modification.

# (2002) Software entities (classes, modules, functions, etc.) should be
# open for extension but closed for modification.

# (2000) A module should be open for extension but
# closed for modification


class DiscountCalculator:
    def __init__(self, product_type, cost):
        self.product_type = product_type
        self.cost = cost

    def get_discounted_price(self):
        if self.product_type == 'electronics':
            return self.cost - self.cost * 0.10
        elif self.product_type == 'cosmetics':
            return self.cost - self.cost * 0.15
        elif self.product_type == 'fitness':
            return self.cost - self.cost * 0.25
        elif self.product_type == 'ayurvedic':
            return self.cost - self.cost * 0.10
