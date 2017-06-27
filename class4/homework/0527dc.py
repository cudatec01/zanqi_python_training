numbers = [12, 37, 5, 42, 8, 7]
def is_odd(n):
    return n % 2 == 0
even = filter(is_odd,numbers)
def is_even(n):
    return n % 2 != 0
old = filter(is_even,numbers)
print (even)
print (old)