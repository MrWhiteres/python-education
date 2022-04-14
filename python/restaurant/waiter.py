from human import Human


class Waiter(Human):
    order = None
    availability = True

    def get_order(self, order):
        """Method responsible for taking an order from a customer"""
        from time import sleep
        self.order = order
        if len(self.order.order_list) > 0:
            self.availability = False
            sleep(5)
            print()
        else:
            print("Sorry, come again")
            self.order.order_status = False
            self.availability = True

    def delivery_order(self, order):
        """delivery method"""
        self.order = order
        if self.order.order_status:
            self.availability = True
            self.order.order_status = "Completed"
            print("bon appetit")

    def info(self):
        """Method displays information about the waiter"""
        print(f"Name waiter - {self._name}\n"
              f"Work time - {self.work_time}")
