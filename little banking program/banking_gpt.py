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
            print("Sorry, you can only withdraw or deposit.")
            decision = input(f"Would you like to withdraw or deposit?\n").lower()

def withdrawing():
    while True:
        try:
            num = float(input("How much do you wish to withdraw?\n"))
            if num > current_balance:
                print("Insufficient funds. Please enter an amount less than or equal to your current balance.")
            elif num <= 0:
                print("Amount must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    balance = current_balance - num
    print(f"Thank you for your transaction. Your new balance is ${balance:.2f}")

def depositing():
    while True:
        try:
            num = float(input("How much do you wish to deposit?\n"))
            if num <= 0:
                print("Deposit amount must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    balance = current_balance + num
    print(f"Thank you for your deposit. Your new balance is ${balance:.2f}")

if __name__ == "__main__":
    greeting()
