class Account:
      bank_name="Stanbic Bank"


      def __init__(self,name,phone,loan_limit):
          self.name=name
          self.phone=phone
          self.loan_limit=loan_limit
          self.balance=0
          self.loan=0
      def  deposit(self,amount):
          if amount<=0:
              return f"The amount is greater than 0"
          else:
            self.balance+=amount
          return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance} "
      def  show_balance(self):
          return self.balance

      def withdraw(self,amount):
          if amount<0:
              return f"Dear{self.name} with {self.phone}  your balance is {self.balance}"
          elif amount>self.balance:
             return f"Your can't withraw"

          else :
              self.balance-=amount
              return f"Dear {self.name} with {self.phone} Your balance is {self.balance}"

      def borrow(self,amount):
          if amount>=self.loan:
              return f"You can't borrow the money, your expectation is above the limits"
          elif  self.loan>=1:
              return f" Pay your first loan to borrow again"

          else:
             self.loan=0
             self.balance+=amount
             return f"Dear {self.name} you had {amount} amount and now it has increased to  balance now is {self.balance}"






