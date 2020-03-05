# NUMBERS ----------------------------------------------------------------------------------

import cmath  # module for operations with complex numbers
import math  # module for standard math operations

a = 7
b = 2
res1 = a + b
res2 = a - b
res3 = a * b
res4 = a ** b
res5 = a / b  # Division always returns a float
res6 = math.factorial(a)
res7 = math.log(a, math.e)

print(f"{a} + {b} = {res1}")
print(f"{a} - {b} = {res2}")
print(f"{a} * {b} = {res3}")
print(f"{a} ** {b} = {res4}")
print(f"{a} / {b} = {res5}")
print(f"{a}! = {res6}")
print(f"ln({a}) = {res7}")
print("---------------------------------------------------")

rad = 2.5
area = math.pi * (rad ** 2)

print(f"area = π * (r^2) = {area} ")
print(f"cos(π) = {math.cos(math.pi)}")
print(f"e = {math.e}")
print(f"∞ = {math.inf}")
print(f"'Not a Number' = {math.nan}")
print("---------------------------------------------------")

z1 = complex(1.0, 1.0)
z1_pol = cmath.polar(z1)
print(f"z={z1}; |z| = {z1_pol[0]} , phase(z) = {z1_pol[1]} ")
print("---------------------------------------------------")

'''
For a complete list of math functions and constants read:
https://docs.python.org/3/library/math.html
https://docs.python.org/3/library/cmath.html
'''
import random  # module for random number generation and random selection

random.seed()  # initialize the random number generator

dice = [1, 2, 3, 4, 5, 6]
count = [0, 0, 0, 0, 0, 0]

for roll in range(1000):  # see 2_4 "for loops"
    face = random.choice(dice)
    count[face - 1] += 1

dice_count = [(d, c) for d, c in zip(dice, count)]  # see 2_5 "list comprehension"

for c in range(len(dice_count)):
    print(f"#{dice_count[c][0]} rolled {dice_count[c][1]} times")
print("---------------------------------------------------")

# monte-carlo estimation of pi
inside = 0

for step in range(100000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x ** 2 + y ** 2) < 1:
        inside += 1

pi_est = float(4 * inside / 100000)
print(f"π estimation = {pi_est} ; error = {math.pi - pi_est}")
print("---------------------------------------------------")

# probabilistic distributions generation
import matplotlib.pyplot as plt

samples_1 = []
samples_2 = []
samples_3 = []

for event in range(100000):
    samples_1.append(random.gauss(3, 0.5))
    samples_2.append(random.gammavariate(3, 0.5))
    samples_3.append(random.expovariate(2))

plt.hist(samples_1, color='blue', bins=100, alpha=0.5)
plt.hist(samples_2, color='red', bins=100, alpha=0.5)
plt.hist(samples_3, color='green', bins=100, alpha=0.5)

plt.xlim(0, 5)
plt.show()

'''
WARNING: The pseudo-random generators of the random module should not be used 
for security purposes. For security or cryptographic uses, see the 'secrets' module.
Complete reference at https://docs.python.org/3/library/random.html
'''
