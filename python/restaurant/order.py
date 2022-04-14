from menu import Menu


class Order:
    order_status: str = None
    price: int = 0
    cash_customer: int = 0
    order_payment: bool = False
    order_list: list = list()

    def add_dishes_to_order(self, name: str = None, price: int = 0):
        """Method adds a dish or drink to the order and deducts money from the customer"""
        self.order_list.append(name)
        self.cash_customer -= price
        self.price += price

    def check_continue_order(self):
        """Method checks whether the order will be supplemented
        with new dishes and also allows you to close the order"""
        later = input("Would you like something else? (Y/N) ").lower()
        while True:
            if later not in ['y', 'n']:
                later = input('Invalid input:(Y/N) ')
            elif later == 'y':
                return True
            elif len(self.order_list) > 0 and later == 'n':
                self.order_status = "during"
                print("Order is accepted")
                self.order_payment: bool = True
                return False
            else:
                print("Empty order")
                return False
        print()

    def check_payment(self, price: int):
        """Method checks whether the buyer can pay for the order"""
        if self.cash_customer >= price:
            return True
        else:
            return False

    def checker_order(self, customer_choose):
        """Method complements the method that opens the order; we sort out part of the checks"""
        price = Menu.merge_menu[customer_choose]
        if self.check_payment(price):
            self.add_dishes_to_order(customer_choose, price)
            print(
                f'Current order: {" ".join(self.order_list) if len(self.order_list) == 1 else ",".join(self.order_list)} '
                f'\nOrder cost: {self.price}, {self.cash_customer}')
            print()
            if self.check_continue_order():
                return True
            else:
                return False
        else:
            print("You don't have enough money to pay")
            if self.check_continue_order():
                return True
            else:
                return False

    def open_order(self):
        """Method that allows you to start placing an order"""
        create = Menu()
        create.show_menu()
        while True:
            customer_choose = input("Choose a dish from the menu : ")
            print()
            if customer_choose in Menu.merge_menu:
                if self.checker_order(customer_choose):
                    continue
                else:
                    break
            else:
                print("This is not on the menu")

    def order_info(self):
        """Method that displays order information"""
        print(
            f'Order status - {self.order_status}\nOrder list - {" ".join(self.order_list) if len(self.order_list) == 1 else ",".join(self.order_list)}'
            f'\nTotal price - {self.price}\n Order payment - {self.order_payment}')
