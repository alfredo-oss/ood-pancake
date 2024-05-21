"""
Imagine a drive-thru where customers order meals by number, such as "Combo 1". Customers
don't specify ingredients or preparation details; they trust the kitchen to handle that.
"""
###### Option (1): Direct instantiation by the client

class Burger:
    def prepare(self):
        pass

class CheeseBurger(Burger):
    def prepare(self):
        return "Preparing a CheeseBurger"

class DeluxeCheeseBurger(Burger):
    def prepare(self):
        return "Preparing a DeluxeCheeseBurger"
    
class VeganBurger(Burger):
    def prepare(self):
        return "Preparing a VeganBurger"
    
# Enum for burger types
class TYPES:
    CHEESE = 1
    DELUXE = 2
    VEGAN = 3

# Client Code
def order_burger(burger_type):
    burger = None
    if burger_type == TYPES.CHEESE:
        burger = CheeseBurger()
    elif burger_type == TYPES.DELUXE:
        burger = DeluxeCheeseBurger()
    elif burger_type ==TYPES.VEGAN:
        burger = VeganBurger()

    if burger:
        print(burger.prepare())
    else:
        print("Unknown burger type")

# Usage
order_burger(TYPES.CHEESE)


































































































