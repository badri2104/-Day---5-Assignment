class Account:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
  def __str__(self):
    return f"Account owner: {self.owner} \nAccount balance: {self.balance}"
  def deposit(self, dep_amt):
    self.balance += dep_amt
    print("Deposit Accepted")
    print(f"Account balance: {self.balance}")
  def withdraw(self, wd_amt):
    try:
      if self.balance >= wd_amt:
        self.balance -= wd_amt
        print("Withdrawal accepted")
        print(f"Account balance: {self.balance}")
      else:
        print("You don't have enought fund")
    except ValueError:
      print("valueerror for fund")


raj = Account("Raj",100000)
print(raj)
print(f"Account Owner : {raj.owner}")
print(f"Account Balance : {raj.balance}")
raj.withdraw(51000)
raj.deposit(1000)
raj.withdraw(100000)

