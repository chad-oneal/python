import random

print('Lets generate a random whole number!')

start = int(input('Enter the lower range: '))

print('This number must be higher than the lower range')
stop = int(input('Enter the upper range: '))

n = random.randrange(start, stop)

print('Your random number is', n)
