from order import Order


class OrderOnline(Order):
    """child class that extends the main one with new fields"""
    address: str = None
    phone_number: str = None
    name_cust: str = None

    def __init__(self, address: str= None, phone_number: str= None, name_cust: str= None):
        self.address = address
        self.phone_number = phone_number
        self.name_cust = name_cust
