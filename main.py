from operators_fun import *
import operators_fun as of


def two_operand_operations(a, operators, opr):
    b = float(input('Please enter b number\n'))
    print('---------------','\n',of.add(a, b))


def one_operand_operations(a, operators, opr):
    pass


def ui(a):
    command_2operand = {'add': '+',
                        'sub': '-',
                        'mul': '*',
                        'divide': '/',
                        'log': 'l',
                        }
    command_1operand = {'sin': 's',
                        'cos': 'c',
                        'exp': 'e',
                        'factorial': '!',
                        'radical': 'r'
                        }
    print('Please enter the operator. Use the list below:')
    print('add : +')
    opr = input()
    two_operand_operations(a, command_2operand, opr)



while True:
    a = input('Please enter a number. (Type "exit" to finish.)\n')
    if a != 'exit':
        a = float(a)
        ui(a)
        print('\n\n\n\n')
    else:
        break
