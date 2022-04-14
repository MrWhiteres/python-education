from abc import ABC


class Transport(ABC):
    transport_list: list = []

    def __init__(self, max_speed_kmh: float, top: bool, ct: bool):
        self.max_speed_kmh = max_speed_kmh
        self.transportation_of_people = top
        self.cargo_transportation = ct

    def __eq__(self, other: object):
        """Magic method that returns whether the speed is equal"""
        return self.max_speed_kmh == other.max_speed_kmh

    def __lt__(self, other: object):
        """Magic method that shows if the maximum speed is less"""
        return self.max_speed_kmh < other.max_speed_kmh

    def __gt__(self, other: object):
        """Magic method that shows more or maximum speed"""
        return self.max_speed_kmh > other.max_speed_kmh

    def info_transport(self):
        """Method that returns complete information about the given object"""
        return f'Maximum speed - {self.max_speed_kmh}\n' \
               f'Is it possible to transport people{"Yes" if self.transportation_of_people else "No"}\n' \
               f'is it possible to carry cargo{"Yes" if self.cargo_transportation else "No"}'

    @staticmethod
    def drive(command: bool):
        """Method that controls transport"""
        if command:
            print("Transport started moving.")
        else:
            print('transport stopped.')


class Engine(ABC):
    engine = False

    def __init__(self, type_fuel: str, use_fuel: float, power: int):
        self.type_fuel = type_fuel
        self.use_fuel = use_fuel
        self.power = power

    def __eq__(self, other: object):
        """Magic method that shows whether the power is equal"""
        return self.power == other.power

    def __lt__(self, other: object):
        """Magic method that shows whether the power is less"""
        return self.power < other.power

    def __gt__(self, other: object):
        """Magic method that shows more power"""
        return self.power > other.power

    def engine_control(self, command: bool):
        """Motor control method"""
        from time import sleep
        if command and self.engine:
            return 'Engine is already running'
        elif command and not self.engine:
            print('The engine is starting')
            sleep(3)
            print('Engine running')
            return self.engine == True
        elif not command and self.engine:
            print('Engine stop')
            sleep(3)
            print('Engine stopped')
            return self.engine == False
        elif not command and not self.engine:
            print("Engine not running")

    def info_engine(self):
        """method that returns complete information about the given object"""
        return f'Type fuel - {self.type_fuel}\nPower - {self.power}\nFuel consumption - {self.use_fuel}'


class Car(Transport, Engine):
    number_of_cars = 0

    def __init__(self, name: str, max_speed_kmh: float, top: bool, ct: bool, type_fuel: str, use_fuel: float,
                 power: int):
        Transport.__init__(self, max_speed_kmh, top, ct)
        Engine.__init__(self, type_fuel, use_fuel, power)
        self.name_transport = name

    def __new__(cls, *args, **kwargs):
        """Method that records the total number of vehicles and adds a transport to a list of all transports"""
        Transport.transport_list.append(cls)
        cls.number_of_cars += 1
        return object.__new__(cls)

    def __str__(cls):
        return cls.name_transport

    @classmethod
    def current_fleet(cls):
        if cls.number_of_cars == 0:
            print('At the moment we do not have cars')
        else:
            print(f'At the moment we have - {cls.number_of_cars}')

    def info_car(self):
        print(f"{self.name_transport}\n{self.info_transport()}\n{self.info_engine()}")
        return self.name_transport


class HandCart(Transport):
    number_cart = 0

    def __init__(self, name, max_speed_kmh, top, ct):
        Transport.__init__(max_speed_kmh, top, ct)
        self.name = name

    def __new__(cls, *args, **kwargs):
        """Method that records the total number of vehicles and adds a transport to a list of all transports"""
        Transport.transport_list.append(cls)
        cls.number_cart += 1
        return object.__new__(cls)

    def cargo_work(self):
        """shipping method"""
        pass

    @classmethod
    def current_fleet(cls):
        if cls.number_cart == 0:
            print('At the moment we do not have cart')
        else:
            print(f'At the moment we have - {cls.number_cart}')

    def __str__(cls):
        return cls.name_transport


class Pipeline(Transport):
    number_pipe = 0

    def __init__(self, max_speed_kmh, ct):
        Transport.__init__(self, max_speed_kmh, top=False, ct=ct)

    def __new__(cls, *args, **kwargs):
        """Method that records the total number of vehicles and adds a transport to a list of all transports"""
        Transport.transport_list.append(cls)
        cls.number_pipe += 1
        return object.__new__(cls)

    def work_zone(self):
        """the method indicates in which zones pipeline work can be carried out"""
        pass

    @classmethod
    def current_fleet(cls):
        if cls.number_pipe == 0:
            print('At the moment we do not have pipline')
        else:
            print(f'At the moment we have - {cls.number_pipe}')


