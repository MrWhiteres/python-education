from human import Human
from order import Order


class Customer(Human):
    order = Order()

    def cash_have(self):
        """Method that shows the current state of the buyer's funds"""
        return self.cash

    def create_order(self):
        """Method that allows you to create an order"""
        self.order.cash_customer = self.cash_have()
        self.order.open_order()

    def check_order(self):
        if self.order.order_status == 'Completed' or not self.order.order_status:
            print("Order close")
