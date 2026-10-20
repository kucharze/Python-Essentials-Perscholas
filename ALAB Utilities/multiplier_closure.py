def make_multiplier(n):
    """Return a function that multiplies by n."""
    def multiplier(x):
        return x * n
    return multiplier