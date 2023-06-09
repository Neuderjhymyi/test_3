'''Main file'''

hello = 'Hello, Synergy!'

def print_hello(args):
    for i in range(10):
        print(hello)
    return input("press any key to exit")


print_hello(hello)
