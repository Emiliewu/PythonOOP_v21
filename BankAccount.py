class BankAccount:
  # class attribute
    all_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    #deposit method
    def deposit(self, amount):
        self.balance += amount
        return self
    #withdraw method
    def withdraw(self, amount):
        # validation 
        if self.balance < amount:
            self.balance -= 5
            print("insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self
    #display
    def display_account_info(self):
        print("Balance: ${}".format(self.balance))
        return self
    #interest
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate*self.balance
        return self
    # class method to print all instances of a Bank Account's info
    @classmethod
    def display_all_balances(cls):
      # we use cls to refer to the class
        for account in cls.all_accounts:
            print("Interest Rate is: ${} and Balance is: ${}".format(account.int_rate, account.balance))

      
#BankAccount instances
first_account = BankAccount(0.01, 1000)
second_account = BankAccount(0.01)
#chaining method
print(first_account.deposit(100).deposit(100).deposit(100).withdraw(300).yield_interest().display_account_info())

print(second_account.deposit(500).deposit(500).withdraw(200).withdraw(200).withdraw(300).withdraw(301).yield_interest().display_account_info())

#call class method
BankAccount.display_all_balances()