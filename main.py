'''Main file'''

hello = 'Hello, Synergy!'

def print_hello(args):
    input("press any key and enter: ")
    for i in range(10):
        print(hello)
    return input("press any key and enter to exit: ")


print_hello(hello)
