from multiply import multiply
from subtraction import subtraction
from addition import add_numbers
from division import division


def main():
    end_point = True
    # This is make sure that input is integer
    first_number = input('Enter first number: ')
    second_number = input('Enter second number: ')
    while end_point:
        x = input('\nWhat do you want to do with your numbers? \n '
                  '1: Add \n '
                  '2: Subtract \n '
                  '3: Multiply \n '
                  '4: Divide \n'
                  '5: Exit the program \n'
                  'Your choice : ')
        if x == '1':
            print("The sum is: %d" % add_numbers(first_number, second_number))
        elif x == '2':
            print('{:s} - {:s} = {:d} '
                  .format(first_number, second_number,
                          subtraction(first_number, second_number)))
        elif x == '3':
            print(multiply(first_number, second_number))
        elif x == '4':
            print(divison(first_number, second_number))
        elif x == '5':
            print('Thanks for using the software. Have a good day.')
            end_point = False
        else:
            print('Cannot understand the answer, please try again\n')


main()
