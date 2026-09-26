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

    while True:

        item = input("What would you like? ").strip().lower()

        if item not in MENU:
            print("Please select an item from the menu.")
        else:
            print(f"You selected {item}, which costs: ${MENU[item]}")

            return item
        
# choose_item()

def parse_command(user_text):

    parts = user_text.strip().lower().split()

    if not parts:
        return ("invalid", "type a command")

    command = parts[0]

    if command in ("menu", "quit", "cart", "checkout"):
        return (command,)
    
    if command in ("add", "remove"):
        if len(parts) != 3:
            return ("invalid", f"{command} needs an item and quantity")
        return (command, parts[1], parts[2])
    
    return ("invalid", "unknown command")


# Step 5

def add_to_cart(cart, name, quantity):

    try:
        quantity = int(quantity)

        if quantity < 1:
            print("Quantity must be at least 1")
            return
    except ValueError:
        print("Quantity must be a number")
        return

    if name not in MENU:
        print("Item is not in menu please try again.")
        return
    
    if name not in cart:
        cart[name] = quantity * MENU[name]
    elif name in cart:
        cart[name] = cart[name] + (quantity * MENU[name])

    return cart

def remove_from_cart(cart, name, quantity):

    try:
        quantity = int(quantity)

        if quantity < 1:
            print("Quantity must be at least 1")
            return
    except ValueError:
        print("Quantity must be a number")
        return

    if name not in cart:
        print("Item is not in the cart")
        return

    removal = quantity * MENU[name]
    if removal > cart[name]:
        print("Not enough of that item in the cart")
        return

    cart[name] -= removal
    if cart[name] == 0:
        del cart[name]

    return cart

def cart_total(cart):

    total = 0

    for i in cart:
        total += cart[i]

    return total

def show_cart(cart):
    for item in cart:
        count = round(cart[item] / MENU[item])
        print(f"{item} x {count}: ${cart[item]:.2f}")
    print(f"Total: ${cart_total(cart):.2f}")

def run_cafe():
    cart = {}

    while True:

        line = input("> ")
        parsed = parse_command(line)

        if parsed[0] == "invalid":
            print(parsed[1])
            continue

        if parsed[0] == "menu":
            show_menu()
        elif parsed[0] == "add":
            add_to_cart(cart, parsed[1], parsed[2])
        elif parsed[0] == "remove":
            remove_from_cart(cart, parsed[1], parsed[2])
        elif parsed[0] == "cart":
            show_cart(cart)
        elif parsed[0] == "checkout":
            print(f"Total: ${cart_total(cart):.2f}")
            break
        elif parsed[0] == "quit":
            break


run_cafe()