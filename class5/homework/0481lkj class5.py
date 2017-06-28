def my_abs(number):
    if number > 0:
        return (number + 10)
    if number == 0:
        return 0
    if number < 0:
        return (number - 10)

print my_abs(2)
print my_abs(-1)
print my_abs(0)
