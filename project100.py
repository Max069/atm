class Atm():
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def cashWithdrawl(self):
        print('You have sucessfully removed the money')

    def balanceEnquiry(self):
        print('you balance is 000')

cardNumber =input('what is your cardNumber?')
pinNumber =input('what is your pin?')
atm1= Atm(cardNumber,pinNumber)

options = int(input('what do you want to do \n1 1.Withdraw \n1 2.Check your balance'))

if(options == 1):
    atm1.cashWithdrawl()
elif(options == 2):
    atm1.balanceEnquiry()
else:
    print('you have chosen the wrong option')