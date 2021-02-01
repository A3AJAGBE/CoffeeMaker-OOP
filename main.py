# Imports
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instantiate the class
make_coffee = CoffeeMaker()
menu = Menu()
payment = MoneyMachine()

turn_off = False
while not turn_off:
    default = input('Do you want to make a coffee? ').lower()

    if default == 'yes':
        print('This coffee maker only makes Espresso, Latte and Cappuccino.')
        user_drink = input('What kind of coffee do you want? ').lower()
        available = menu.find_drink(user_drink)
        make_coffee.is_resource_sufficient(available)
    elif default == 'no':
        turn_off = True
        print('Okay.')
    elif default == 'off':
        turn_off = True
        print('The Coffee Maker is off.')
    elif default == 'report':
        print('Coffee Maker Report:\n ')
        print(make_coffee.report())
        print(payment.report())
    else:
        print('Invalid response.\n')



