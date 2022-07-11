import os


def display_codes():
    """Displays the contents of codes.csv in a fixed width, two column format"""
    with open('codes.csv', 'r') as file:
        lines = file.readlines()

    codes = []
    for line in lines:
        codes.append(line.strip('\n').replace('"', '').split(','))
    if len(codes) % 2 == 1:
        codes.append(['', ''])

    for i in range(0, len(codes), 2):
        print(f'{codes[i][0]:<9}{codes[i][1]:<8}\t{codes[i+1][0]:<9}{codes[i+1][1]:<8}')
    return codes


def main():
    display_codes()


if __name__ == '__main__':
    main()
