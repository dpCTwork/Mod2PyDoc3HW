
def greet_user():
    user_name = input("What is your name? ")
    print('\n')
    print(f'Welcome to the Shopping Cart Program, {user_name}!')
    print('This program will allow you to add items to your shopping cart.')
    print('----------------------------------------------------------')

def show_instructions():
    print("Type 'SHOW' or 'S' to show current items in your shopping cart")
    print("Type 'ADD or 'A' to add another item to cart")
    print("Type 'DEL' or 'D' to remove an item from cart")
    print("OR to quit this program: Type 'QUIT' or 'Q'")
    print('\n')

def instructions_add(shop_cart):
    while True:
        print("Would you like to add another item to your cart?")
        add_or_nah = input("Press 'Y' to proceed or 'N' to go to the main menu: ")
        if add_or_nah.lower() == 'y':
            print('\n')
            item = input("Which item would you like to place in your shopping cart? ")
            price = float(input("Please enter the price amount in dollars and cents (ex: x.xx) "))
            shop_cart[item.title()] = price
            print(f"You have successfully added {item.title()} (${price:.2f}) to your shopping cart!")
            print('\n')
            continue
        elif add_or_nah.lower() == 'n':
            break
        else:
            print("INVALID ENTRY. PLEASE PRESS 'Y' OR 'N'.")
            print('\n')
            continue

def instructions_del(shop_cart):
    while True:
        print("Would you like to remove another item from your cart?")
        del_or_nah = input("Type 'Y' to proceed or 'N' to go to the main menu: ")
        if del_or_nah.lower() == 'y':
            print('\n')
            item = input("Which item would you like to remove from your shopping cart? ")
            if item.title() in shop_cart:
                del shop_cart[item.title()]
                print('\n')
                print(f'You have successfully removed {item.title()} from your cart!')
                print('\n')
                continue
            else:
                print('\n')
                print("You do not have this item in your cart. Please check your spelling and try again")
                print('\n')
                continue        
        elif del_or_nah.lower() == 'n':
            break
        else:
            print("INVALID ENTRY. PLEASE PRESS 'Y' OR 'N'.")
            print('\n')
            continue