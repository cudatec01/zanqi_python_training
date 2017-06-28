numbers = [12, 37, 5, 42, 8, 7]
even = []
old = []
for i in numbers:
    if i%2 ==0:
        even.append(i)
    else:
        old.append(i)
print 'even=',even
print 'old=',old