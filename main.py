from ShoppingCart import ShoppingCart
from Product import Product

def print_menu():
    user_input = ''

    while user_input != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
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

def main():
    print_menu()


if __name__ == '__main__':main()