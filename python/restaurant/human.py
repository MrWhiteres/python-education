class Human:
    cash = 0

    def __init__(self, name: str = None, cash: int = 0, work_time: str = "unemployed"):
        self._name = name
        self.cash = cash
        self.work_time = work_time

    def lock_cash(self):
        """Method shows the amount of money at the current moment"""
        print(f"Current balance {self.cash}")

    def cash_add(self, money):
        """Method allows you to add money"""
        self.cash += money
        print(f"Balance is filled: {money}. Current balance: {self.cash}.")

    def cash_turn_down(self, money):
        """Method allows you to pay for the order"""
        if self.cash >= money:
            self.cash -= money
            print(f"Payment completed, left on account{self.cash}")
        else:
            print(f"you don't have enough to pay: {money - self.cash}")

    @property
    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name
