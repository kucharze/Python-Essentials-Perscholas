l = [91,32,56,48,5]

print("Original list l")
print(l)

print("Calling the sorted() function on the list l ",sorted(l))

print("Before sort() function call ",l)
l.sort()
print("After sort() function call ",l)

l.append(100)
print("After append() function call appending 100 ",l)

l.reverse()
print("After reverse() function call ",l)