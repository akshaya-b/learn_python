a={1,5,6,7,4,5,6,7}
print(a) #set is unordered non duplicate collection of values
#print(a[2]) #throws TypeError: 'set' object is not subscriptable as it is unordered collection.
b=set((2,5,6,2,4,6,8))
print(b)
c=set([3,5,6,4,5,6,3])
print(c)

print(b.union(c)) #or b|c: returns all the values in both set
print(b & c) #or b.intersection(c): returns common value in both set
print(b-c)
print(c.difference(b))
print(a ^ b) #prints the value that is not common for both the sets
