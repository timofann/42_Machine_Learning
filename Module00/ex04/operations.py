import argparse

usage_string = """\
python operations.py <number1> <number2>
Example:
    python operations.py 10 3
"""


def parse():
    parser = argparse.ArgumentParser(usage=usage_string)
    parser.add_argument('number1', type=int)
    parser.add_argument('number2', type=int)
    args = parser.parse_args()
    return args.number1, args.number2


if __name__ == '__main__':
    number1, number2 = parse()
    print(f'Sum:         {number1 + number2}')
    print(f'Difference:  {number1 - number2}')
    print(f'Product:     {number1 * number2}')
    print(f'Quotient:    {number1 / number2 if number2 else "ERROR (div by zero)"}')
    print(f'Remainder:   {number1 % number2 if number2 else "ERROR (modulo by zero)"}')
