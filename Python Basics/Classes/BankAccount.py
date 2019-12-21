
class BankAccount:
    total_overdraft = 0
    max_overdraft = -1000
    max_overdraft_per_client = -300

    def __init__(self):
        self.balance = 0

    @classmethod
    def print_total_overdraft(cls):
        print(f'Total overdraft: {cls.total_overdraft:,.2f}')

    @classmethod
    def update_total_overdraft(cls, amount):
        cls.total_overdraft += amount

    @classmethod
    def approve_overdraft(cls, overdraft):
        return (cls.total_overdraft + overdraft > cls.max_overdraft and
        overdraft > cls.max_overdraft_per_client)

    def withdrow(self, amount):
        overdraft = self.balance - amount
        if self.approve_overdraft(overdraft):
            self.balance -= amount
            self.update_total_overdraft(overdraft)
        else:
            print('Your overdraft wasn\'t approverd')

    def deposit(self, amount):
        if self.balance < 0:
            self.update_total_overdraft(min(abs(self.balance), amount))
        self.balance += amount


acc1 = BankAccount()
acc2 = BankAccount()
acc3 = BankAccount()
