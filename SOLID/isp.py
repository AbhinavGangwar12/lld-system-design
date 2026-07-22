from abc import ABC, abstractmethod

# Interface for vegetarian menu
class IVegetarianMenu(ABC):
    @abstractmethod
    def getVegetarianItems(self):
        pass

# Interface for non-vegetarian menu
class INonVegetarianMenu(ABC):
    @abstractmethod
    def getNonVegetarianItems(self):
        pass

# Interface for drinks menu
class IDrinkMenu(ABC):
    @abstractmethod
    def getDrinkItems(self):
        pass

# Class for vegetarian menu
class VegetarianMenu(IVegetarianMenu):
    def getVegetarianItems(self):
        return ["Vegetable Curry", "Paneer Tikka", "Salad"]

# Class for non-vegetarian menu
class NonVegetarianMenu(INonVegetarianMenu):
    def getNonVegetarianItems(self):
        return ["Chicken Curry", "Fish Fry", "Mutton Biryani"]

# Class for drinks menu
class DrinkMenu(IDrinkMenu):
    def getDrinkItems(self):
        return ["Water", "Soda", "Juice"]

# Function to display menu items for a vegetarian customer
def displayVegetarianMenu(menu):
    print("Vegetarian Menu:")
    for item in menu.getVegetarianItems():
        print(f"- {item}")

# Function to display menu items for a non-vegetarian customer
def displayNonVegetarianMenu(menu):
    print("Non-Vegetarian Menu:")
    for item in menu.getNonVegetarianItems():
        print(f"- {item}")

def main():
    vegMenu = VegetarianMenu()
    nonVegMenu = NonVegetarianMenu()
    drinkMenu = DrinkMenu()

    displayVegetarianMenu(vegMenu)
    displayNonVegetarianMenu(nonVegMenu)

if __name__ == "__main__":
    main()


"""
+ IVegetarianMenu Interface:      This interface defines a method to get vegetarian items. It ensures that only classes implementing vegetarian menus will need to provide this functionality.
+ INonVegetarianMenu Interface:   Similar to the vegetarian interface, this one defines a method for getting non-vegetarian items.
+ IDrinkMenu Interface:           This interface defines a method for getting drink items, keeping it separate from food items.
+ VegetarianMenu Class:           Implements the IVegetarianMenu interface and provides a list of vegetarian items.
+ NonVegetarianMenu Class:        Implements the INonVegetarianMenu interface and provides a list of non-vegetarian items.
+ DrinkMenu Class: Implements the IDrinkMenu interface and provides a list of drink items.
"""