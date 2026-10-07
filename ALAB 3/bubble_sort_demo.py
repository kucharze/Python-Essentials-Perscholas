l = [64, 25, 12, 22, 11]

print("Original list l")
print(l)

for i in range(len(l)):
    swapped = False
    for j in range(0, len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            swapped = True
            
    print("List after the", i+1, "iteration")
    print(l)
    if not swapped:
        break

print("List after bubble sort")
print(l)