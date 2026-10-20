products = ['chips', 'soda', 'candy', 'cookies', 'water', 'sandwich']
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]   

shopping_cart = []

def main_menu():
    print('\ne p i c    s h o p\n')
    print('1. view avaliable products')
    print('2. add product to cart')
    print('3. remove product from cart')
    print('4. view shopping cart')
    print('5. view current total')
    print('6. check out')

def display_products():
    print('')
    counter = 1
    for p in products:
        index = products.index(p)
        price = prices[index]
        print(counter, f'. {p}', f'     ${price}')
        counter += 1
    input('\npress anything to continue')

def add_product():
    print('\nwhich product would you like to add\n')
    counter = 1
    for p in products:
        print(counter, f'. {p}')
        counter += 1
    validating = True
    while validating:
        item = int(input('\nenter product number: '))
        if item < 1 or item > counter - 1:
            print(f'\ninvalid product\nplease choose a number between 1 and {counter - 1}')
        else:
            item_add = products[item - 1]
            shopping_cart.append(item_add)
            print(f'added {item_add} to the shopping cart')
            validating = False
    input('\npress anything to continue')

def remove_product():
    if len(shopping_cart) == 0:
        print('\nyou have nothing in your cart to remove')
        input('\npress anything to continue')
    else:
        print('\ny o u r    c a r t\n')
        counter = 1
        for i in shopping_cart:
            print(counter, f'. {i}')
            counter += 1
        print('\nwhich item would you like to remove?')
        validating = True
        while validating:
            item = int(input('enter item number: '))
            if item < 1 or item > counter - 1:
                print(f'\ninvalid number\nplease enter a number between 1 and {counter - 1}')
            else:
                item_remove = item - 1
                shopping_cart.pop(item_remove)
                print(shopping_cart)
                validating = False
        input('press anything to continue')

        
def display_cart():
    print('')
    print('\ny o u r    c a r t\n')
    counter = 1
    for i in shopping_cart:
        print(counter, f'. {i}')
        counter += 1
def display_total():
    pass
def check_out():
    pass

in_store = True
while in_store:
    main_menu()
    action = input('\nwhat would you like to do? ')
    if action == '1':
        display_products()
    elif action == '2':
        add_product()
    elif action == '3':
        remove_product()
    elif action == '4':
        display_cart()
    elif action == '5':
        display_total()
    elif action == '6':
        check_out()
    elif action == '10':
        in_store = False
