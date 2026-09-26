MENU = {
    "muffin": 3.50,
    "tea": 2.00,
    "coffee": 1.50,
    "water": 1.00,
    "juice": 2.50,
    "soda": 3.00,
    "beer": 5.00,
    "wine": 8.00,
    "cocktail": 10.00,
    "alcohol": 15.00,
    "food": 10.00,
    "drink": 5.00,
    "snack": 2.50,
}

def show_menu():
    for item, price in MENU.items():
        print(f"{item}: ${price:.2f}")


# show_menu()

def choose_item():

    shopping_cart = {}

    while True:

        item = input("What would you like? ").strip().lower()

        if item not in MENU:
            print("Please select an item from the menu.")
        else:
            print(f"You selected {item}, which costs: ${MENU[item]}")

            shopping_cart[item] = MENU[item]
            
            another_item = input("Would you like another item? y/n ").lower()

            if another_item == "y":
                continue
            else:
                break
        

    return shopping_cart

# choose_item()

def parse_command(user_text):

    parts = user_text.strip().lower().split()

    if not parts:
        return ("invalid", "type a command")

    command = parts[0]

    if command in ("menu", "quit", "cart", "checkout"):
        return command
    
    if command in ("add", "remove"):
        if len(parts) != 2:
            return ("invalid", f"{command} needs an item")
        return (command, parts[1])
    
    return ("invalid", "unknown command")


# Step 5
cart = []

def add_to_cart(cart, name):
    
    if name in MENU:
        cart.append(name)
    else:
        print("Invalid item")
        
    return cart

def remove_from_cart(cart, name):

    if name in cart:
        cart.remove(name)
    else:
        print("Item is not in the cart")

    return cart

def cart_total(cart):

    sum = 0

    for i in cart:
        sum += MENU[i]

    return sum

def show_cart(cart):
    for item in cart:
        print(item)
    print(f"Total: ${cart_total(cart):.2f}")

