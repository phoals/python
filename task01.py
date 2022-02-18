import sys
import string


def encrypt(str_to_work, key):
    abc = string.ascii_lowercase
    digits = '1234567890'
    str_res = []
    for item in str_to_work:
        if item.isdigit():
            index = (digits.index(item) + key) % len(digits)
            str_res.append(digits[index])
        elif item.islower():
            index = (abc.index(item) + key) % len(abc)
            str_res.append(abc[index])
        else:
            index = (abc.upper().index(item) + key) % len(abc)
            str_res.append(abc[index].upper())
    print("".join(str_res))


def decrypt(str_to_work, key):
    abc = string.ascii_lowercase
    digits = '1234567890'
    str_res = []
    for item in str_to_work:
        if item.isdigit():
            index = (digits.index(item) - key) % len(digits)
            str_res.append(digits[index])
        if item.islower():
            index = (abc.index(item) - key) % len(abc)
            str_res.append(abc[index])
        else:
            index = (abc.upper().index(item) - key) % len(abc)
            str_res.append(abc[index].upper())
    print("".join(str_res))


def main(args: list):
    if args[1] == 'e':
        encrypt(args[2], int(args[3]))
    if args[1] == 'd':
        decrypt(args[2], int(args[3]))


if __name__ == '__main__':
    main(sys.argv)
