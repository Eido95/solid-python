# OCP: The Open-Closed Principle

# (2017) A software artifact should be open for extension but
# closed for modification.

# (2002) Software entities (classes, modules, functions, etc.) should be
# open for extension but closed for modification.

# (2000) A module should be open for extension but
# closed for modification
from abc import ABC, abstractmethod


class DiscountCalculator(ABC):
    @abstractmethod
    def get_discounted_price(self):
        pass


class ElectronicsDiscountCalculator(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - self.cost * 0.10


class CosmeticsDiscountCalculator(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - self.cost * 0.15


dc_cosmetic = CosmeticsDiscountCalculator(100)
dc_price = dc_cosmetic.get_discounted_price()
