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

p = [ ("itay", 3), ("danny", 5), ("suzi", 1) ]
p.sort() # default sort - first item
print(p)

def getSortingItem(item):
    # item = ("itay", 3)
    return item[1]
    #item.split()[1]
p = [ ("itay", 3), ("danny", 5), ("suzi", 1) ]
p2 = ["itay hau", "benny cohen"]
p.sort(key=getSortingItem) # [3, 5, 1] -- [1, 3, 5]
p.sort(key=lambda item: item[1])
p2.sort(key=lambda item:item.split()[1])
print(p)
print(p2)

# [-4, -6, 0, 4, -2, 12, -200]
# 1. create filter using lambda to
#    get only positive numbers
# 2. create map using lamda to
#   get 1/3 of each number
# [(1,2,3), (2,3), (1,2,3,4,5), (1,)]
# sort this list by the length of each tuple:
# result = [(1,), (2,3), (1,2,3), (1,2,3,4,5)]

# Solution:
l1 = [-4, -6, 0, 4, -2, 12, -200]
print(list(filter(lambda x:x > 0, l1)))
print(list(map(lambda x:x / 3, l1)))
l2 = [(1,2,3), (2,3), (1,2,3,4,5), (1,)]
print(sorted(l2, key=lambda x:len(x)))
