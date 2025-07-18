from ShoppingCart import ShoppingCart
from Product import Product

def print_menu():
    user_input = ''
    cart = ShoppingCart()

    while user_input != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item details')
        print('i - Output items\' description')
        print('o - Output shopping cart')
        print('q - Quit')

        while True:
            try:
                user_input = input('Choose an option: ').strip().lower()

                if len(user_input) != 1:
                    raise Exception
                elif user_input not in ('a', 'r', 'c', 'i', 'o', 'q'):
                    raise Exception
                break
            except Exception:
                print('Please enter a valid option from the menu.')

        if user_input == 'a':
            item = Product()

            while True:
                try:
                    temp_name = input('Please enter the name of the product: ')

                    if len(temp_name) == 0:
                        raise Exception
                    break
                except Exception:
                    print('Please enter a name.')

            while True:
                try:
                    temp_quantity = int(input('Please enter how many of the product you want to purchase: ')).strip()

                    if temp_quantity <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print('Please enter a number greater then zero.')

            while True:
                try:
                    temp_cost = int(input('Please enter the cost of the product: '))

                    if temp_cost <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print('Please enter a number greater than zero')
            while True:
                try:
                    temp_description = input('Please enter a description of the product: ')

                    if len(temp_description) == 0:
                        raise Exception
                    break
                except Exception:
                    print('Please enter a description.')

            print(f'Adding {temp_name} with a quantity of {temp_quantity} with the cost of {temp_cost} and with the following description: {temp_description}...')
            cart.add_item(Product(temp_name, temp_quantity, temp_cost, temp_description))

        elif user_input == 'r':
            cart.list_items()

            while True:
                try:
                    temp = int(input('Enter the number of the item you wish to remove: ')).strip()

                    if 0 > temp > cart.get_num_items_in_cart():
                        raise Exception
                    break
                except Exception:
                    print(f'Please enter a number 1-{cart.get_num_items_in_cart()}.')

            print(f'Removing item {temp} - {cart.get_item(temp - 1).get_name()} from your cart')
            cart.remove_item(temp - 1)

        elif user_input == 'c':
            cart.list_items()

            while True:
                try:
                    temp = int(input('Enter the number you wish to change: ')).strip()

                    if 0 > temp > cart.get_num_items_in_cart():
                        raise Exception
                    break
                except Exception:
                    print(f'Please enter a number 1-{cart.get_num_items_in_cart()}')

            print(f'You chose {temp} - {cart.get_item(temp - 1).get_name()}, what would you like to change?')
            sub_input = ''
            temp_quantity = 0
            temp_cost = 0
            temp_description = ''

            while sub_input != 'f':
                print(f'q - Quantity of items (currently: {cart.get_item(temp - 1).get_quantity()})')
                print(f'c - Cost of the item (currently: {cart.get_item(temp - 1).get_cost()})')
                print(f'd - Description of the item (currently: {cart.get_item(temp - 1).get_description()}')
                print('f - Finalize changes')

                try:
                    sub_input = input('Enter option: ').strip().lower()

                    if sub_input not in ('q', 'c', 'd', 'f'):
                        raise Exception
                except Exception:
                    print('Please enter one of the options provided.')

                if sub_input == 'q':
                    while True:
                        try:
                            temp_quantity = int(input('Please enter new quantity: ').strip())

                            if temp_quantity <= 0:
                                raise ValueError
                            break
                        except ValueError:
                            print('Enter a value greater then zero.')

                elif sub_input == 'c':
                    while True:
                        try:
                            temp_cost = int(input('Please enter new cost: ').strip())

                            if temp_cost <= 0:
                                raise ValueError
                            break
                        except ValueError:
                            print('Enter a value greater than zero.')

                elif sub_input == 'd':
                    while True:
                        try:
                            temp_description = input('Enter new description')

                            if len(temp_description) == 0:
                                raise Exception
                            break
                        except Exception:
                            print('Enter something.')
                else:
                    print(f'Updating item {cart.get_item(temp - 1).get_name()}...')
                    cart.modify_item(Product(cart.get_item(temp - 1).get_name(), temp_quantity, temp_cost, temp_description))

        elif user_input == 'i':
            cart.print_descriptions()

        elif user_input == 'o':
            cart.print_total()

        else:
            print('Quiting...')
            break

def main():
    print_menu()


if __name__ == '__main__':main()