def default():
    print("Hello")

def main():
    default()
if __name__ == '__main__':
    main()import sys
def default():
    print("Hello")


def cat():
    print(" Meow Meow")


def dog():
    print(" bhaw bhaw")

def main():
    if sys.argv[1]=='cat':
        cat()
    elif sys.argv[1]=='dog':
        dog()
    else:
        default()
if __name__ == '__main__':
    main()