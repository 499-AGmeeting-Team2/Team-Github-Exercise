from division import divison

def main():


    end_point = True
    # This is make sure that input is integer
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    while end_point:
        x = input('\nWhat do you want to do with your numbers? \n '
                  '1: Add \n '
                  '2: Subtract \n '
                  '3: Mutiply \n '
                  '4: Divide \n'
                  '5: Exit the program \n'
                  'Your choice : ')
        if x == '1':
            print('Do something')
        elif x == '2':
            print('Do something')
        elif x == '3':
            print('Do something')
        elif x == '4':
            print(divison(first_number, second_number))
        elif x == '5':
            print('Thanks for using the software. Have a good day')
            end_point = False
        else:
            print('Cannot understand the answer, please try again\n')


main()
