from collections import Counter
import math
def get_prime_factors(number):
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i
    if number > 2:
        prime_factors.append(int(number))

    return prime_factors
x = get_prime_factors(800)
y = get_prime_factors(1200)
print(x)
print(y)
#print(Counter(x))
#print(Counter(y))
c = dict(Counter(x)) #variables to save counter for a
d = dict(Counter(y)) #variables to save counter for b

result = []
for key in sorted(set(c.keys()).union(set(d.keys()))):
    exp = max(c.get(key, 0), d.get(key, 0))
    for i in range(exp):
        result.append(key)
print(result)

mul = 1
for i in result:
    mul = mul*i

print(mul)

