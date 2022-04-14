from courier import Courier


class DeliveryService:
    def __init__(self, work_time: dict = dict(), courier_list: list = list()):
        self.package = None
        self.work_time = work_time
        self.courier_list = courier_list

    def hire_a_courier(self, name, work_time, transport):
        """Method that allows you to create a courier"""
        courier = Courier(name=name, work_time=work_time, transport=transport)
        self.courier_list.append(courier)
        print(f"Waiter {courier.name} hired.")
        return courier

    def fire_the_courier(self, name):
        """Method that allows you to fire a courier"""
        try:
            del self.courier_list[self.courier_list.index(name)]
            print(f"Courier {name} fired from his job")
        except (IndexError, ValueError):
            print(f"Courier {name} doesn't work here")

    def waiters_on_shift(self):
        """Method shows which of the couriers is currently at work"""
        if len(self.courier_list) > 0:
            for i in self.courier_list:
                print(i.name, i.work_time)
        else:
            print("Everyone is resting today")

    def check_list(self, list_delivery: list):
        """Method that shows and gives the order if it is in the list"""
        from random import choice
        if len(list_delivery) > 1:
            self.package = choice(list_delivery.pop())
            return self.package
        else:
            print('Nothing')

    def info_package(self):
        """Method shows order information and customer information"""
        print(
            f'Name customer - {self.package.name_cust}\nPhone number - {self.package.phone_number}\n'
            f'Address - {self.package.address}')
