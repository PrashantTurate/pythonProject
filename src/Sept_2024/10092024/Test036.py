# Custom Exception - Own

class BalanceLowException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)


balance = 100
withdraw = int(input("Enter the amount you want to withdraw "))
if withdraw > balance:
    raise BalanceLowException("Balance is Low!!")
else:
    print("Remain Bal ", (balance - withdraw))