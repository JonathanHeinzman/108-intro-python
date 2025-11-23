from catalog import catalog # import your catalog list

# Global shopping cart list
cart = []

def print_header(text):
    print("-------------------")
    print(text)
    print("-------------------")

def print_menu():
    print("Menu")
    print(" 1. - View Catalog")
    print(" 2. - Search Product")
    print(" 3. - View Cart")
    print(" 4. - Clear Your Cart")
    # Add more features
    print(" Q - Quit")

def print_catalog():
    print_header("- Our Catalog -")
    for prod in catalog:
        print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')

    answer = input("type ID to add (N to close):")
    if answer.lower == "n": 
        return
    else:
        add_product_to_cart(answer)
    
def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True 
            cart.append(prod) # add ptoduct to the cart
            print(f'{prod["title"]} added to your cart.')
            break

        if not found:
            print("This item is not in our catalog")
        print("------------------------\n")


def search_product():
    found = False
    print_header("- Search Product: -")
    text = input("search text: ")
    for prod in catalog:

        if text in prod["title"]:
            found = True
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
            choice = input("Do you want to add this to your cart? Y for Yes or N for No: ")
            if choice == "Y":
                add_product_to_cart(prod["id"])
                break
    if not found:
        print("Error: Item not found")




def view_cart():
    print_header("- View Cart -")

    if not cart:
        print("Your car is Empty.")
    else:
        for prod in cart:
            print("These items in your cart:")
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
        cart_total()
        print("------------------------\n")

def cart_total():
    total = 0
    for prod in cart:
        total += prod["price"]
    print(f"Cart Total: ${total}")

def clear_cart():
    for prod in cart:
        choice = input("Are you sure you want to clear your cart? Y/N: ")
        if choice == "Y":
            cart.clear()
            print("Your cart has been cleared, it is now empty.")
            break



# MAIN PROGRAM LOOP
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to J's Products!")
    print_menu()

    option = input("Choose an option: ")

    if option == "1":
        #print("view catalog")
        print_catalog()
    elif option == "2":
        #print("search product")
        search_product()
    elif option == "3":
        #print("view cart")
        view_cart()
        
    # Add other features
    elif option == "4":
        clear_cart()
    elif option == "q" or option == "Q":
        print("Good Bye!")
        break
    else:
        print("** ERROR: Invalid Option!")
        print("------------------------\n")

