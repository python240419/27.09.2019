# lambda - for nicer and shorter coding
# creating functions in-line
# don't use return keyword (automatically)
# cannot have more than 1 line

def print_hello():
    print("hello")
f1 = print_hello
print_hello()
f1()
f2 = lambda: print("hello")
f2()

def even(x):
    #zugi = x % 2 == 0
    #return zugi
    return x % 2 == 0

l1 = [1,2,3,4,5,6,7]
print(list(filter(even, l1))) # even must return bool
print(list(filter(lambda x: x % 2 == 0, l1))) # even must return bool

def mulby2(x):
    return x * 2
l1 = [1,2,3,4,5,6,7]
print(list(map(mulby2, l1)))
print(list(map(lambda x: x * 2, l1)))


