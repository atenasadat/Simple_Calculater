from operators_fun import *
import operators_fun as of


def two_operand_operations(a, operators, opr):
    b = float(input('Please enter b number\n'))
    print('---------------')
    for c in operators:
        if operators[c] == opr:
            if opr == '+':
                print(of.add(a, b))
            elif opr == '-':
                print(of.sub(a, b))
            elif opr == '*':
                print(of.mul(a, b))
            elif opr == '/':
                print(of.divide(a, b))
            elif opr == 'l':
                print(of.log(a, b))
            break


def one_operand_operations(a, operators, opr):
    print('---------------')
    for c in operators:
        if operators[c] == opr:
            if opr == 's':
                print(of.sin(a))
            elif opr == 'c':
                print(of.cos(a))
            elif opr == 'e':
                print(of.exp(a))
            elif opr == '!':
                print(of.factorial(a))
            elif opr == 'r':
                print(of.radical(a))
            break


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

    while True:
        print('Please enter the operator. Use the list below:')
        for c2 in command_2operand:
            print(c2, ' : ', command_2operand[c2])
        for c1 in command_1operand:
            print(c1, ' : ', command_1operand[c1])
        opr = input()
        if opr in command_2operand.values():
            two_operand_operations(a, command_2operand, opr)
            break
        elif opr in command_1operand.values():
            one_operand_operations(a, command_1operand, opr)
            break
        else:
            print("NO VALID INPUT!")


while True:
    a = input('Please enter a number. (Type "exit" to finish.)\n')
    if a != 'exit':
        a = float(a)
        ui(a)
        print('\n\n\n\n')
    else:
        break
