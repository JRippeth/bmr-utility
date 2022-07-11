import os


def get_customer_codes() -> dict[str: str]:
    """Returns a dictionary mapping names to codes"""
    with open('codes.csv', 'r') as file:
        lines = file.readlines()

    codes = {}
    for line in lines:
        name, code = line.strip('\n').replace('"', '').split(',')
        codes[name] = code

    return codes


def main():
    customers = get_customer_codes()

    # display customer codes
    for i, name in enumerate(customers):
        print(f'{name:<9}{customers[name]:<8}', end='')
        # add a new line every second customer code
        if i % 2 != 0:
            print()

    # validate customer name
    name = input('\n\nEnter the customer name: ')
    while name not in customers.keys():
        name = input('Invalid name - Please re-enter: ').upper()

    # validate order prefix
    prefix = input('(C)ancel or (B)ackorder: ').upper()
    while prefix not in ['C', 'B']:
        prefix = input('Invalid order type - Please re-enter: ').upper()


if __name__ == '__main__':
    main()
