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
    codes = get_customer_codes()

    # display customer codes
    for i, name in enumerate(codes):
        print(f'{name:<9}{codes[name]:<8}', end='')
        # add a new line every second customer code
        if i % 2 != 0:
            print()


if __name__ == '__main__':
    main()
