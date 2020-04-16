# method on the top
def separator():
    print(40 * '-')

def menu():
    print(5 * '\n')
    separator()
    print('Welcome to PyCalc')
    separator()

    print('[1] - Add')
    print('[2] - Subtract')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Exit')

# instruction on the bottom

opc = ''
while(opc != 'x'):
    menu()
    opc = input('Select an option: ')
    if(opc == 'x'):
        break # break finish with the loop

    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))

    if(opc == '1'):
        res = num1 + num2
        print('Result = ' + str(res))

    elif(opc == '2'):
        res = num1 - num2
        print('Result = ' + str(res))

    elif(opc == '3'):
        res = num1 * num2
        print('Result = ' + str(res))

    elif(opc == '4'):
        if(num2 == 0):    
            print("Error: Dividing by 0 is not allowed")
        else:
            res = num1 / num2
            print('Result = ' + str(res))

    input('Press Enter to continue...')
    
    

print('Thank you!!')