n = int(input('Type a number, and its factorial will be printed: '))

if n < 0:
    raise ValueError('You must enter a non negative integer')

fact = 1

for i in range(2, n + 1):
    fact *= i

print(fact)