# this one is like your scripts with argv
def print_two(*args):
    for i in args:
        print(i)
 #    print("arg1: {}, arg2: {}".format(lhm1, lhm2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(co1, com2):
    print("arg1: {}, arg2: {}".format(co1, com2))

# this just takes one argument
def print_one(lhm1):
    print("arg1: {}".format(lhm1))

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw","dsdad","sasdad")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
