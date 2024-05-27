from enum import Enum
from abc import ABC, abstractmethod

class Burgers(Enum):
    CHEESE = "CHEESE"
    DELUXECHEESE = "DELUXECHEESE"
    VEGAN = "VEGAN"
    DELUXEVEGAN = "VEGAN"

class Burger(ABC):
    def __init__(self):
        self.name = ""
        self.bread = ""
        self.sauce = ""
        self.toppings = []

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass

    def get_name(self) -> str:
        return self.name

class CheeseBurger(Burger):
    def __init__(self):
        super().__init__()
        self.name = "CheeseBurger"
        self.bread = "Dam Good English Muffins"
        self.sauce = "Salsa Picante"
        self.toppings = ["Tomato", "Pickles", "Onions"]
    
    def prepare(self) -> str:
        return f"Preparing a {self.name}"

    def cook(self) -> str:
        return f"Cooking a {self.name}"
    
    def serve(self) -> str:
        return f"Serving a {self.name}"
    
    def get_name(self) -> str:
        return self.name

class DeluxeCheeseBurger(Burger):
    def __init__(self):
        super().__init__()
        self.name = "DeluxeCheeseBurger"
        self.bread = "Dam Good English Muffins"
        self.sauce = "Salsa Marinara"
        self.toppings = ["Cheese", "Bacon", "Mango"]

    def prepare(self) -> str:
        return f"Preparing a {self.name}"

    def cook(self) -> str:
        return f"Cooking a {self.name}"
    
    def serve(self) -> str:
        return f"Serving a {self.name}"
    
    def get_name(self) -> str:
        return self.name    
    
class VeganBurger(Burger):
    def __init__(self):
        super().__init__()
        self.name = "DeluxeCheeseBurger"
        self.bread = "Dam Good English Muffins"
        self.sauce = "Salsa Marinara"
        self.toppings = ["Cheese", "Bacon", "Mango"]

    def prepare(self) -> str:
        return f"Preparing a {self.name}"

    def cook(self) -> str:
        return f"Cooking a {self.name}"
    
    def serve(self) -> str:
        return f"Serving a {self.name}"
    
    def get_name(self) -> str:
        return self.name
    
class DeluxeVeganBurger(Burger):
    def __init__(self):
        super().__init__()
        self.name = "DeluxeCheeseBurger"
        self.bread = "Dam Good English Muffins"
        self.sauce = "Salsa Marinara"
        self.toppings = ["Cheese", "Bacon", "Mango"]

    def prepare(self) -> str:
        return f"Preparing a {self.name}"

    def cook(self) -> str:
        return f"Cooking a {self.name}"
    
    def serve(self) -> str:
        return f"Serving a {self.name}"
    
    def get_name(self) -> str:
        return self.name   

class BurgerStore(ABC):
    @abstractmethod
    def create_burger(self, item: Burgers) -> Burger:
        pass
    def order_burger(self, type: Burgers) -> Burger:
        burger = self.create_burger(type)
        print(f"--- Making a {burger.get_name()} ---")
        burger.prepare()
        burger.cook()
        burger.serve()
        return burger
    
class CheeseBurgerStore(BurgerStore):

    def create_burger(self, item: Burgers) -> Burger:
        if item == Burgers.CHEESE:
            return CheeseBurger()
        elif item == Burgers.DELUXECHEESE:
            return DeluxeCheeseBurger()
        else:
            return None

class VeganBurgerStore(BurgerStore):

    def create_burger(self, item: Burgers) -> Burger:
        if item == Burgers.VEGAN:
            return VeganBurger()
        elif item == Burgers.DELUXEVEGAN:
            return DeluxeVeganBurger()
        else:
            return None
               
    
cheese_store = CheeseBurgerStore()
vegan_store = VeganBurgerStore()

burger = cheese_store.order_burger(Burgers.CHEESE)
print(f"Ethan ordered a {burger.get_name()}")