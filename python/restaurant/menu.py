class Menu:
    def __init__(self):
        pass

    dishes: dict = dict()
    drinks: dict = dict()
    merge_menu: dict = {**dishes, **drinks}

    def show_menu(self):
        """Method allows you to see the entire menu or only parts of it"""
        if menu is None:
            print("All Menu:")
            merge_menu = {**self.dishes, **self.drinks}
            for name, price in merge_menu.items():
                print(f"{name} - {price}$")
        else:
            print("Menu dishes:" if menu == "dishes" else "Menu drinks:")
            if menu == "dishes":
                for name, price in self.dishes.items():
                    print(f"{name} - {price}$")
            if menu == "drinks":
                for name, price in self.drinks.items():
                    print(f"{name} - {price}$")

    def add_new(self, dishes_or_drink: str, name: str, price: int):
        """Method allows you to add new dishes or drinks to the menu"""
        if dishes_or_drink == "dishes":
            self.dishes[name] = price
            self.merge_menu = {**dishes, **drinks}
            print(f"Dishes {name} is added to the menu with a cost of {price}$.")
        elif dishes_or_drink == "drinks":
            self.drinks[name] = price
            self.merge_menu = {**dishes, **drinks}
            print(f"Drinks {name} is added to the menu with a cost of {price}$.")

    def del_dishes_or_drinks(self, menu: str, name: str):
        """Method allows you to delete existing dishes or drinks changed"""
        menu = self.dishes if menu == "dishes" else self.drinks if menu == "drinks" else None
        try:
            del menu[name]
            print(f"Dish '{name}' removed from the menu.")
        except KeyError:
            print(f"Dish '{name}' is not on the menu.")
