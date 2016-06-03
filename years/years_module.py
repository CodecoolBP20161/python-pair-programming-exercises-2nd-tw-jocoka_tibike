import datetime


def years(age):
    date = datetime.datetime.now()
    date.year
    birth = date.year - age + 100
    print("You will be a hundred years old in {0}, if you live long enough" .format(birth))
    es = ("You will be a hundred years old in " + str(birth) + ", if you live long enough")
    ki = int(input("How many times do you want the previous line to be written?: "))
    for i in range(ki):
        print(es)
    return birth


def main():
    name = input("What's your name?: ")
    age = int(input("How old are you?: "))
    years(age)

if __name__ == '__main__':
    main()
