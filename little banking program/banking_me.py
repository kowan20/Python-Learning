current_balance = 1089.96

def greeting():
    decision = input(f"Hi, welcome to the bank, your current balance is ${current_balance}, would you like to withdraw or deposit?\n").lower()
    while True:
            if decision == "deposit":
                 depositing()
                 break
            elif decision == "withdraw":
                 withdrawing()
                 break
            else:
                 print("sorry, you are only withdrawing or depositing")
                 decision = input(f"Would you like to withdraw or deposit?\n").lower()
                 
                 


def withdrawing():
    while True:
        try:
            num = float(input("How much do you wish to withdraw?\n"))
            if num > 1089.96:
                    print("you thought didn't you...")
                    num = float(input("how much do you wish to withdraw?\n"))
            elif num < 1089.96:
                 break
        except ValueError:
             print("must be a number")
    balance = current_balance - num
    print(f"Thankyou for your transaction. your new balance is ${balance:.2f}")


def depositing():
    while True:
            try:
                num = float(input("How much do you wish to deposit?\n"))
                if num <= 0:
                    input("Must be greater than 0")
                else:
                    break
            except ValueError:
                 print("must be a number")
                 
    
            
    balance = current_balance + num
    print(f"Thankyou for your deposit, your new balance is: ${balance:.2f}")

if __name__ == "__main__":
    greeting()