from customer import Customer
from order_online import OrderOnline


class CustomerOnline(Customer):

    def __init__(self,name:str, address: str, phone_number: str):
        Customer.__init__(self, name)
        self.address = address
        self.phone_number = phone_number

    order = OrderOnline()

    def create_order(self):
        """Method that allows you to create an order"""
        self.order.phone_number = self.phone_number
        self.order.address = self.address
        self.order.name_cust = self._name
        self.order.open_order()
