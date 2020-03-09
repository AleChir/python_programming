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
print("\n1)---------------------------------------------------")
print(f"{a} + {b} = {res1}")
print(f"{a} - {b} = {res2}")
print(f"{a} * {b} = {res3}")
print(f"{a} ** {b} = {res4}")
print(f"{a} / {b} = {res5}")
print(f"{a}! = {res6}")
print(f"ln({a}) = {res7}")

print("\n2)---------------------------------------------------")
rad = 2.5
area = math.pi * (rad ** 2)

print(f"area = π * (r^2) = {area} ")
print(f"cos(π) = {math.cos(math.pi)}")
print(f"e = {math.e}")
print(f"∞ = {math.inf}")
print(f"'Not a Number' = {math.nan}")

print("\n3)---------------------------------------------------")
z1 = complex(1.0, 1.0)
z1_pol = cmath.polar(z1)
print(f"z={z1}; |z| = {z1_pol[0]} , phase(z) = {z1_pol[1]} ")

# For a complete list of math functions and constants read:
# https://docs.python.org/3/library/math.html
# https://docs.python.org/3/library/cmath.html

print("\n4)---------------------------------------------------")
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

print("\n5)---------------------------------------------------")
# monte-carlo estimation of pi
inside = 0

for step in range(100000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x ** 2 + y ** 2) < 1:
        inside += 1

pi_est = float(4 * inside / 100000)
print(f"π estimation = {pi_est} ; error = {math.pi - pi_est}")

print("\n6)---------------------------------------------------")
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

# WARNING: The pseudo-random generators of the random module should not be used
# for security purposes. For security or cryptographic uses, see the 'secrets' module.
# Complete reference at https://docs.python.org/3/library/random.html

# STRINGS ----------------------------------------------------------------------------------

S = 'Spam'

print(f"STRING = {S}, LENGTH = {len(S)}")
print(f"S[0] = {S[0]}, S[1] = {S[1]}, S[2] = {S[2]}, S[3] = {S[3]}")
print(f"S[-1] = {S[-1]}, S[-2] = {S[-2]}, S[-3] = {S[-3]}, S[-4] = {S[-4]}")

print("\n7)---------------------------------------------------")
#   Strings type objects are immutable. The following assignment would rise an exception:
#   S = 'spam'
#   S[0] = 'E'
#   The correct way to perform this operation is:
#   S = 'E' + S[1:]

name = input("Enter your name (3-20 char):")

while len(name) > 20 or len(name) < 3:
    name = input("Enter a valid name:")

surname = input("Enter your surname (3-20 char):")

while len(surname) > 20 or len(surname) < 3:
    surname = input("Enter a valid surname:")

name_up = name.upper()
name_double = name * 2
name_surname = name + surname
nickname = name[:3] + '_' + surname[:3]
surname_middle = surname[1:-1]

print(f"NAME = {name}\nSURNAME = {surname}")
print(f"NAME * 2 = {name_double}")
print(f"NAME + SURNAME = {name_surname}")
print(f"SURNAME MIDDLE = {surname_middle}")
print(f"NICKNAME = {nickname}")

print("\n8)---------------------------------------------------")
phone_num = '+39 011 13987456'
country_code = phone_num[:3]
prefix = phone_num[4:7]
num = phone_num[8:]
print(f"PHONE NUMBER: {phone_num}")
print(f"COUNTRY CODE: {country_code}")
print(f"PREFIX: {prefix}")
print(f"NUMBER: {num}")

print("\n9)---------------------------------------------------")
fields = ['NAME', 'SURNAME', 'AGE', 'JOB']
profile1 = 'John, Smith, 45, Plumber'
profile2 = 'Alice, Wonder, 32, Engineer'
profile3 = 'Mario, Rossi, 65, Musician'
p1_lst = profile1.split(',')
p2_lst = profile2.split(',')
p3_lst = profile3.split(',')
database = [p1_lst, p2_lst, p3_lst]
print(database)

for record in database:
    print('_________________')
    for f, v in zip(fields, record):
        print(f"{f} = {v.lstrip()}")  # lstrip()/rstrip() methods remove whitespaces on left/right of the string

print("\n10)---------------------------------------------------")
code1 = 'MRT558966544'
code2 = 'AHL-987_1554_44#'
print(code1, code1.isalnum(), code1.replace('MRT', 'HKL'))
print(code2, code2.isalnum(), code2[code2.find('-'):])

print("\n11)---------------------------------------------------")
import re

path = 'usr/home/desktop/notes.txt'
path_lst = re.split('[/.]', path)
print(path, '-->', path_lst)
filename, extension = path_lst[-2:]
print(f"FILENAME: {filename}\tEXTENSION: .{extension}")

# STRINGS ----------------------------------------------------------------------------------
