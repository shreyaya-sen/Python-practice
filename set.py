collection = {
    1,2,3,4,5,"hi","how do u do"
} #if we write a value twice it wont give error but will not print it twice
print(type(collection))
print(collection)
print(len(collection))
#when we use empty 
# with intension of set still
#  the type will be printed as dict
empty ={}
print(type(empty))

#sets are mutable but set elements are immutable
collection.add(2)
collection.add(78)
collection.add(56)
collection.add("shreya")
collection.remove("hi")

print(collection)
#cant add together (1,2,3,4) as set is immutable ie hashable 
print(len(collection))
collection.clear()
print(len(collection))
collect = {
   "4four","5five","hi45","how do u do"
}
print(collect.pop())
print(collect.pop())
collect = {
   "4four","5five","hi45","how do u do"
}
collection = {
    1,2,3,4,5,"hi","how do u do"
}
print(collection.union(collect)) 
print(collection.intersection(collect))

