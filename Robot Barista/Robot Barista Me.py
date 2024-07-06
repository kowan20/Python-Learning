# Menu and price
menu = ["Beans = $4", "Rice = $3", "Chicken = $5", "Kangaroo = $6"]
print(f"Hi, welcome to the Robot Barista. Please take a look at our menu and tell us what coffee you would like to order?\n\n\n{', '.join(menu)}")

order = input("What would you like to order?\n").lower()

# If order isn't on the menu
if order not in ["beans", "rice", "chicken", "kangaroo"]:
    print("Pick something off the menu!")
    order = input("What would you like to order?\n").lower()

# Assign price based on the order
if order == "beans":
    price = 4
elif order == "rice":
    price = 3
elif order == "chicken":
    price = 5
elif order == "kangaroo":
    price = 6

# Get quantity and calculate total
while True:
    try:
        quantity = int(input("How many coffees would you like?\n"))
        if 1 <= quantity <= 6:
            break
        else:
            print("Please enter a number between 1 and 6.")
    except ValueError:
        print("Please enter a valid number.")

total = quantity * price

# Get name
print(f"Of course, your total is ${total}. May I get a name?")
name = input("What is your name?\n")

while name == "":
    print("Please tell me your name")
    name = input("What is your name?\n")

# Hayley suck part
if name.lower() == "hayley":
    suck_status = input("Do you suck?\n")
    if suck_status.lower() == "yes":
        print("Hah, you suck, go away.")
        exit()
    elif suck_status.lower() == "no":
        print("Go away Hayley, you know you suck.")
        exit()
    else:
        print("The answer is yes, hahahaha")
        exit()

# Greeting for specific names
if name.lower() in ["bee", "bethany"]:
    print("Hey cutie, I love you.")

# Final thanks for the order
print(f"Thanks {name}, we'll have your order ready in a few moments.")
