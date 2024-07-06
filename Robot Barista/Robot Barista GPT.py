# Define the menu using a dictionary
menu = {
    "beans": 4,
    "rice": 3,
    "chicken": 5,
    "kangaroo": 6
}

# Function to display the menu
def display_menu():
    print("Hi, welcome to the Robot Barista. Please take a look at our menu and tell us what you would like to order?\n")
    for item, price in menu.items():
        print(f"{item.capitalize()} = ${price}")

# Function to get valid order
def get_order():
    while True:
        order = input("\nWhat would you like to order?\n").strip().lower()
        if order in menu:
            return order
        else:
            print("Pick something off the menu!")

# Function to get valid quantity
def get_quantity():
    while True:
        try:
            quantity = int(input("How many would you like?\n"))
            if 1 <= quantity <= 6:
                return quantity
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")

# Function to get customer's name
def get_name():
    while True:
        name = input("\nWhat is your name?\n").strip()
        if name:
            return name
        else:
            print("Please tell me your name.")

# Function for specific interactions based on name
def interact_based_on_name(name):
    if name.lower() == "hayley":
        suck_status = input("Do you suck?\n").strip().lower()
        if suck_status == "yes":
            print("Hah, you suck, go away.")
            exit()
        elif suck_status == "no":
            print("Go away Hayley, you know you suck.")
            exit()
        else:
            print("The answer is yes, hahahaha")
            exit()
    elif name.lower() in ["bee", "bethany"]:
        print("Hey cutie, I love you.")

# Main program logic
def main():
    display_menu()
    order = get_order()
    price = menu[order]

    quantity = get_quantity()
    total = quantity * price

    name = get_name()
    interact_based_on_name(name)

    print(f"\nThanks {name}, your total is ${total}. We'll have your order ready in a few moments.")

if __name__ == "__main__":
    main()
