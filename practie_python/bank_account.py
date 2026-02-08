class BankAccount:
    def __init__(self):
        self.balance = 0
        self.tran_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError('Invalid Amount!')
        msg = f'Deposit: Credited Rupees {amount}. Current Balance is {self.balance}'
        self.tran_history.append(msg)

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            msg = f'Withdrawal: Debited Rupees {amount}. Current Balance is {self.balance}'
        else:
            msg = f'Insufficient Amount : Available balance {self.balance}'
        self.tran_history.append(msg)
        return msg

    def check_balance(self):
        msg = f'Balance Enquiry : Your balance is {self.balance}'
        self.tran_history.append(msg)
        return msg

    def get_history(self):
        return self.tran_history



def main():
    #add here
    pass

if __name__ == '__main__':
    main()

