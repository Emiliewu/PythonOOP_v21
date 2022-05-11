class BankAccount:
    def __init__(self, int_rate, name, balance=0,):
        self.int_rate = int_rate
        self.balance = balance
        self.name = name
    #deposit method
    def deposit(self, amount):
        self.balance += amount
        return self
    #withdraw method
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self
    #display account balance method
    def display_account_info(self):
        print("Balance: ${}".format(self.balance))
        return self
    #yield interest method
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate*self.balance
        return self
#user class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = []
    #user instance can open several bankaccount  
    def user_open_account(self, int_rate, name, balance):
        #validation for account name uniqueness
        account_exist = False
        for eachaccount in self.account:
            if eachaccount.name == name:
                print("{} already exists, try another name".format(name))
                account_exist = True
                break
        if account_exist == False:
            new_account = BankAccount(int_rate, name, balance)
            self.account.append(new_account)
            print("{} is opened".format(name))
        return self.account
    #user can deposit to specific account by name
    def user_deposite(self, amount, account_name):
      for i in range(0, len(self.account)):
        if self.account[i].name == account_name:
          self.account[i].deposit(amount)
          print("Deposite ${} to {} and the new balance is ${}". format(amount, self.account[i].name, self.account[i].balance))
      return self
    #user can withdraw from specific account by name
    def user_withdraw(self, amount, account_name):
        for i in range(0, len(self.account)):
            if self.account[i].name == account_name:
                self.account[i].withdraw(amount)
                print("withdraw ${} from {} and the new balance is ${} ". format(amount,self.account[i].name, self.account[i].balance))
        return self
    #iterate through all the accounts of one user instance and print balance
    def display_user_balance(self, account_name):
        for i in range(0, len(self.account)):
            if self.account[i] == account_name:
                print("Current balance of ${} is ${} ". format(self.account[i].name, self.account[i].balance))
        return self

#create user instance
first_user = User("Harry Potter", "harrypotter@gmail.com")
#user create accounts
first_user.user_open_account(0.02, "account1", balance = 0)
first_user.user_open_account(0.02, "account2", balance = 0)
first_user.user_open_account(0.02, "account1", balance = 0)
#user deposite and display
first_user.user_deposite(200, "account1").display_user_balance("account1")
#chaning methods
first_user.user_deposite(200, "account1").user_deposite(200, "account2").user_withdraw(10, "account1").user_withdraw(10,"account1").user_withdraw(50, "account2").display_user_balance("account1").display_user_balance("account2")