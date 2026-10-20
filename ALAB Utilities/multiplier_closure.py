def make_multiplier(n):
    """Return a function that multiplies by n."""
    def multiplier(x):
        return x * n
    return multiplier


times3 = make_multiplier(3)
print(times3(5))  # Output: 15

times10 = make_multiplier(10)
print(times10(3))  # Output: 30