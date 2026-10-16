products = ['chips', 'soda', 'candy', 'cookies', 'water', 'sandwich']
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]
shopping_cart = []
def main_menu():
    print('\n','-' * 10, '(: smart shopping cart :)', '-' * 10, '\n')
    print('1. view avaliable products')
    print('2. add product to cart')
    print('3. remove product from cart')
    print('4. view shopping cart')
    print('5. view current total')
    print('6. checkout\n')
game = True
while game:
    main_menu()
    choice = input('enter your choice: ')
    if choice == '1':
        print('\n', '-'*10, 'avaliable products', '-'*10, '\n')
        count = 1
        for p in products:
            print(str(count), '. ', p, '    ', str(prices[count-1]), '$')
            count += 1
        input('\npress anything to continue')
    elif choice == '2':
        print('\nwhich product would you like to add?\n')
        count = 1
        for p in products:
            print(str(count), f'. {p}')
            count += 1 
        valid = True
        while valid:
            add = int(input('\nenter product number: '))
            if add < 1 or add > count - 1:
                print(f'please enter a valid number between 1 and {count - 1}')
            else:
                added = products[add-1]
                shopping_cart.append(added)
                print(f'added {added} to cart')
                valid = False
        input('\npress anything to continue')
    elif choice == '3':
        if len(shopping_cart) == 0:
            print('\nyour shopping cart is empty')
            print('there is nothing to remove')
        else:
            print('\n', '-'*10, 'your cart', '-'*10, '\n')
            count = 1
            for item in shopping_cart:
                print(str(count), '. ', item)
                count += 1
            valid = True
            while valid:
                remove = int(input('\nwhat item would you like to remove\nenter item number:'))
                if remove < 1 or remove > count - 1:
                    print(f'please enter a valid number between 1 and {count - 1}')
                else:
                    removed = shopping_cart.pop(remove - 1)
                    print(f'removed {removed} from the cart')
                    valid = False
            input('\npress anything to continue')
    elif choice == '4':
        print('\n', '-'*10, 'your cart', '-'*10, '\n')
        count = 1
        for item in shopping_cart:
            print(str(count), '. ', item, '    ', str(prices[count-1]), '$')
            count += 1
        total_items = len(shopping_cart)
        print(f'you have {total_items} total items')
        input('\npress anything to continue')
    elif choice == '5':
        print('\n', '-'*10, 'current total', '-'*10, '\n')
        total_price = 0
        for item in shopping_cart:
            location = products.index(item)
            print(f'{item}      {prices[location]}$')
            total_price += prices[location]
        print(f'\ntotal price is {total_price}$')
        input('\npress anything to continue')
    elif choice == '6':
        print('\n', '-'*10, 'checkout', '-'*10, '\n')
        total_price = 0
        for item in shopping_cart:
            location = products.index(item)
            total_price += prices[location]
        print(f'subtotal: ${total_price}')
        discountp_ = 0
        if total_price >= 10 and total_price < 20:
            discountp_ = 5
        elif total_price >= 20 and total_price < 40:
            discountp_ = 10
        elif total_price >= 40:
            discountp_ = 15
        print(f'discount: {discountp_}%')
        amount_saved = (discountp_ / 100) * total_price
        print(f'amount saved: ${amount_saved}')
        final_total = total_price - amount_saved
        print(f'\nFinal Total: ${final_total}')
        if total_price == 0:
            print('wow you bought nothing thanks for wasting my time')
        game = False


    