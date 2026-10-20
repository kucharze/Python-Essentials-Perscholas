def gen_fibinacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        

print("Fibonacci numbers:")
for num in gen_fibinacci(10):
    # print("Inside loop")
    print(num)