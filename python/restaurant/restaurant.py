from menu import Menu
from waiter import Waiter


class Restaurant:
    menu = Menu()
    order = None
    list_package_delivery = []

    def __init__(self, name: str = None, address: str = None, work_time: dict = dict(),
                 waiter_list: list = list()):
        self.name = name
        self.address = address
        self.work_time = work_time
        self.waiter = waiter_list

    def add_work_time(self, day: str, time: str):  # Time format 08:00 - 20:00
        """Method allows you to add working hours"""
        self.work_time[day] = time

    def del_work_time(self, day: str):
        """Method that allows you to delete working hours"""
        try:
            del self.work_time[day]
            print(f"Business day '{day}' removed")
        except KeyError:
            print(f"This day '{day}' is a holiday and it's not on the list")

    def show_work_time(self):
        """Method that shows working time"""
        for day, time in self.work_time.items():
            print(f"{day} {time}")

    def hire_a_waiter(self, name: str, work_time: str):
        """Method that allows you to hire a waiter"""
        waiter = Waiter(name=name, work_time=work_time)
        self.waiter.append(waiter)
        print(f"Waiter {waiter.name} hired.")
        return waiter

    def fire_the_waiter(self, name: str):
        """Method allows you to fire the waiter"""
        try:
            del self.waiter[self.waiter.index(name)]
            print(f"Waiter {name} fired from his job")
        except (IndexError, ValueError):
            print(f"Waiter {name} doesn't work here")

    def waiters_on_shift(self):
        """Method shows whether there are currently waiters at work"""
        if len(self.waiter) > 0:
            for i in self.waiter:
                print(i.name, i.work_time)
        else:
            print("Everyone is resting today")

    def info_of_waiter(self):
        """Method shows information about the waiter"""
        for i in self.waiter:
            i.info()

    def list_package_delivery(self, order: object):
        """Method adds the order to the list of ready to ship"""
        self.list_package_delivery.append(order)

    def package_order(self):
        """method checks the status of the order, whether it is ready for shipment, transfers its list of ready"""
        self.order.order_status("Ready to delivery")
        self.list_package_delivery(self.order)

    def order_preparation(self, order: object, offline: str = "offline"):
        """Method checks order status offline or online and prepares it"""
        from time import sleep
        self.order = order
        if self.order.order_status and offline == "offline":
            print("order in progress")
            sleep(len(self.order.order_list) + 5)
            print("Order is ready")
        if self.order.order_status and offline == "online":
            print("order in progress")
            sleep(len(self.order.order_list) + 5)
            self.package_order()
            print("Order is ready")
