class User:
    def __init__(self, user_name, email_address):
        self.name = user_name
        self.email= email_address
        self.account_balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: ${}".format(self.balance))
        return self

    def transfer(self, receiver, amount):
        if self.balance > amount:
            self.balance -= amount
            receiver.balance += amount
        else:
            self.balance -= 5
            print("insufficient funds: Charging a $5 fee")
        return self
      
first_user = User("Chloe Dong","chloedong@gmail.com")
second_user = User("Cindy Zhang","cindyzhang@gmail.com")
third_user = User("Coco Zhao","cocozhao@gmail.com")

first_user.deposit(100).deposit(100).deposit(100).withdraw(500).display_account_info()

second_user.deposit(100).deposit(100).withdraw(500).withdraw(1800).display_account_info()

third_user.deposit(100).withdraw(500).withdraw(500).withdraw(500).display_account_info()

first_user.transfer(third_user, 500).display_account_info()

third_user.display_account_info()

