"""

We know the burger menu may evolve over time, but we would prefer not to directly modify all 
the parts of code that instantiate a burger.
Taking the design principle, "encapsulate what varies" into consideration, we can create a 
class SimpleBurgerFactory and isolate the burger creation logic to a method called 
"createBurger".
This still violates the open/closed principle but it also violates the dependency inversion 
principle. The simple factory has direct dependencies on the concrete classes that it 
is creating. And while the simple factory is abstracting away the creation process, the 
product type still needs to be provided to the factory.

"""
from enum import Enum

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

class BurgerType(Enum):
    CHEESEBURGER = 1
    DELUXE_CHEESEBURGER = 2
    VEGANBURGER = 3

class SimpleBurgerFactory:
    def create_burger(self, burger_type: BurgerType) -> Burger:
        if burger_type == BurgerType.CHEESEBURGER:
            return CheeseBurger()
        elif burger_type == BurgerType.DELUXE_CHEESEBURGER:
            return DeluxeCheeseBurger()
        elif burger_type == BurgerType.VEGANBURGER:
            return VeganBurger()
        else:
            return None

# Test the SimpleBurgerFactory
fact = SimpleBurgerFactory()
burger = fact.create_burger(BurgerType.CHEESEBURGER)

if burger:
    print(burger.prepare())
else:
    print("Unknown burger type")

