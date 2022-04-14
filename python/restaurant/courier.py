from human import Human


class Courier(Human):
    def __init__(self, name: str, transport: str,work_time:str):
        self.transport = transport
        self.name = name
        self.work_time = work_time

    def delivery(self, package):
        """Delivery method"""
        address = package.address
        print('Delivery...')

    def info(self):
        """Method that displays information about the courier"""
        print(f"Name courier - {self.name}\n"
              f"Work time - {self.work_time}")
