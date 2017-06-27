# -*- coding: UTF-8 -*-
numbers = [12, 37, 5, 42, 8, 7]
even = []
old = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        old.append(number)
print even
print old
