
import stack

hex2dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
           'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12, 'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15}

dec2hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
           11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def conv2dec(hexD, hex_string):
    """
    This will take in a hexadecimal value in string form and return
    its decimal value.
    """
    exponent = len(hex_string) - 1
    total = 0
    for char in hex_string:
        total += hexD[char] * 16 ** exponent
        exponent -= 1

    return total

def conv2hex(decD, dec_string):
    """
    This will take in a decimal value in integer form and convert and return
    its hexadecimal value.
    """
    value = dec_string
    new_stack = stack.getStack()
    while (value % 16) != 0:
        stack.push(new_stack, decD[value % 16])
        value //= 16

    final = ''
    while stack.isEmpty(new_stack) == False:
        final += str(stack.pop(new_stack))

    return final


def main():

    # Program greeting
    print('Hexadecimal Calculator')
    print('Enter your calculation in the form hex_num_1 oper hex_num_2')
    print('      where hex_num_1 and hex_num_2 are hexadecimal numbers')
    print('      and where oper is on of these operators: +,-,*,//,%')
    ans = 'y'

    while ans in 'yY':
        calculation = input('Enter calculation: ')
        split_lst = calculation.split()
        num1 = conv2dec(hex2dec, split_lst[0])
        num2 = conv2dec(hex2dec, split_lst[2])
        oper = split_lst[1]

        dec_total = 0
        if oper == '+':
            dec_total = num1 + num2
        elif oper == '-':
            dec_total = num1 - num2
        elif oper == '*':
            dec_total = num1 * num2
        elif oper == '//':
            dec_total = num1 // num2
        elif oper == '%':
            dec_total = num1 % num2

        # handling of negative results
        if dec_total < 0:
            dec_total = abs(dec_total)
            hex_total = conv2hex(dec2hex, dec_total)
            print(num1, oper, num2, '= -', hex_total)

        hex_total = conv2hex(dec2hex, dec_total)
        print(num1, oper, num2, '=', hex_total)
        ans = input('Enter another ( y or n)? ')

main()