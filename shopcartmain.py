import shopcartmod as scmod

def shopping_cart_program():
    shop_cart = {}
    scmod.greet_user()
    quit_program = False
    while True:
        print('\n')
        print('                     MAIN MENU:')
        print('----------------------------------------------------------')
        scmod.show_instructions()
        user_choice = input("Please choose an option: ")
        while True:    
            if user_choice.lower() == 'show' or user_choice.lower() == 's':
                print('\n')
                print('Item     :     Price')
                print('---------------------')
                for k,v in shop_cart.items():
                    print(f" {k} : ${v:.2f}")
                print('---------------------')
                print(f"# of items: {len(shop_cart.keys())}")
                print(f"Subtotal: ${(sum(shop_cart.values())):.2f}")
                next_step = input("Press 'Q' to QUIT or ANY other key to return to the main menu: ")
                if next_step.lower() == 'q':
                    quit_program = True
                    break
                else:
                    break
            elif user_choice.lower() == 'add' or user_choice.lower() == 'a':
                print('\n')
                item = input("Which item would you like to place in your shopping cart? ")
                price = float(input("Please enter the price amount in dollars and cents (ex: 0.99, 3.49, 11.55, etc.) "))
                shop_cart[item.title()] = price
                print(f"You have successfully added {item.title()} (${price:.2f})to your shopping cart!")
                print('\n')
                scmod.instructions_add(shop_cart)
                break
            elif user_choice.lower() == 'del' or user_choice.lower() == 'd':
                print('\n')
                item = input('Which item would you like to remove from your cart? ')
                del shop_cart[item.title()]
                print('\n')
                print(f"You have successfully removed the item '{item.title()}' from your cart!")
                print('\n')
                scmod.instructions_del(shop_cart)
                break
            elif user_choice.lower() == 'quit' or user_choice.lower() == 'q':
                quit_program = True
                break
            else:
                print("You have entered an invalid entry.")
                print('\n')
                continue
        if quit_program:
            print('Here is your shopping cart from this session:')
            print('---------------------------')
            for k,v in shop_cart.items():
                print(f" {k} : ${v:.2f}")
            print('---------------------------')
            print(f"You have {len(shop_cart.keys())} items in your cart, for a subtotal of ${sum(shop_cart.values()):.2f}")
            print('See you next time!')
            break
shopping_cart_program()