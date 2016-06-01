import string
import random


def passwordgen():
    size = 6
    a = string.ascii_letters
    b = "#" + "!" + "@" + "$"
    c = string.digits
    d = ''.join(random.choice(a) for i in range(size))
    e = ''.join(random.choice(b))
    f = ''.join(random.choice(c))
    g = d + e + f
    print(g)
    return g


def main():
    while True:
        n = input("This is a password generator. Type n for a new random password. Type anything else to quit.")
        if n == "n":
            passwordgen()
        else:
            break
    return passwordgen()



if __name__ == '__main__':
    main()
