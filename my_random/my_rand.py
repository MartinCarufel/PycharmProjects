import random

number = 500000
rng_min = 1
rng_max = 2
list = []
for i in range(number):
    list.append(random.randrange(rng_min, rng_max+1, 1))

for j in range(rng_min,rng_max+1,1):
    print('Number of {:=2}: {:=5}'.format(j, list.count(j)))

