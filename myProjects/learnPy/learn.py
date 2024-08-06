def main():
    name = input('What\'s your name? ')
    hello()
    hello(name)


def hello(to="World") :
    print('Hello,', to)


main()