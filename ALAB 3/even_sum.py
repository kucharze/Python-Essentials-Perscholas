sum = 0

for i in range(50):
    if i % 2 == 0:
        sum += i

print(sum)



sum2 = 0
i = 0
while i < 50:
    if i % 2 == 0:
        sum2 += i
    i += 1

print(sum2)

#both loops give the same result, but the for loop is more concise and easier to read. The while loop requires more lines of code and is less efficient.