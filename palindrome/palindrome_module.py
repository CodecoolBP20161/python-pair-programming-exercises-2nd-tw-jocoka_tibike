

def palindrome(word):
    word = word.lower()
    for i, char in enumerate(word):
        if char != word[-i-1]:
            return False
        else:
            return True


def main():
    word = input("Enter text to check if it's a palindrome!: ")
    if palindrome(word):
        print("Palindrome")
    else:
        print("Not a palindrome")


if __name__ == '__main__':
    main()
