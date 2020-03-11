############################################################################################
# NUMBERS ----------------------------------------------------------------------------------
############################################################################################

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

############################################################################################
# STRINGS ----------------------------------------------------------------------------------
############################################################################################

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

############################################################################################
# LISTS ------------------------------------------------------------------------------------
############################################################################################

print("\n12)---------------------------------------------------")
prof = ['Mark', 'Smith', 48, 35500]
print(f"prof = {prof}\t type = {type(prof)}\t len = {len(prof)}")

prof[0] = 'John'  # lists are mutable collections of objects supporting in-place changes
prof + ['Plumber']  # + and * operators do not change the original list, if not specified
print(f"prof = {prof}\t type = {type(prof)}\t len = {len(prof)}")

prof.append('Plumber')  # the 'append' and 'pop' method changes the original list
print(f"prof = {prof}\t type = {type(prof)}\t len = {len(prof)}")
prof.pop()
print(f"prof = {prof}\t type = {type(prof)}\t len = {len(prof)}")

print("\n13)---------------------------------------------------")
cities = ['Rome', 'London', 'Paris', 'New York', 'Amsterdam', 'Buenos Aires']
print(cities)
cities.sort()
print(cities)
cities.reverse()
print(cities)

print("\n14)---------------------------------------------------")

hess = [[12.1, 4.2, 3.3],
        [4.2, 8.3, 41.2],
        [3.3, 41.2, 7.9]]

fxy = hess[0][1]
fxz = hess[0][2]
fyx = hess[1][0]
fyz = hess[1][2]
fzx = hess[2][0]
fzy = hess[2][1]

for line in range(len(hess)):
    print(hess[line])

# for line in hess:
#   print(line)

if fxy == fyx and fxz == fzx and fyz == fzy:
    print(f"The matrix is symmetric")

print("\n15)---------------------------------------------------")

M = [[5, 2, 1],
     [6, 9, 7],
     [4, 0, 3]]

col0 = [row[0] for row in M]  # list comprehension
col1 = [row[1] for row in M]
col2 = [row[2] for row in M]

M_t = [col0,
       col1,
       col2]

print("\nM =")
for line in M:  # iteration on a list
    print(line)

print("\nM_t =")
for line in M_t:
    print(line)

diag = [M[i][i] for i in range(len(M))]
print(f"\ndiagonal elements :\t{diag}")

# extracts even numbers from the first column
even = [row[0] for row in M if row[0] % 2 == 0]
print(f"\neven elements in the first column :\t{even}")

# squared elements of the second column
squared = [row[1] ** 2 for row in M]
print(f"\nsquared elements of the second column:\t{squared}")

print("\n16)---------------------------------------------------")
val_square_cube = [[x, x ** 2, x ** 3] for x in range(5)]
print(val_square_cube)

print("\n17)---------------------------------------------------")
mtx = [[0.5, 3.6, 1.7],
       [6.7, 9.5, 7.8],
       [8.9, 0.9, 5.7],
       [3.6, 0.5, 1.7]]

sum_gen = (sum(row) for row in mtx)  # enclosing a comprehension statements in "()" create a generator
print(sum_gen)
print(next(sum_gen))
print(next(sum_gen))
print(next(sum_gen))
print(next(sum_gen))
# print(next(sum_gen))
# calling next() out of bounds will rise a StopIteration exception

sum_list = list(map(sum, mtx))
print(sum_list)
# the map(func, seq) built-in calls "func" on each item in "seq". Equivalent to:
# sum_list = []
# for item in mtx:
#   sum_l.append(sum(item))
# print(sum_l)

sum_set = {sum(row) for row in mtx}
print(sum_set)
sum_dict = {i: sum(mtx[i]) for i in range(len(mtx))}
print(sum_dict)
# comprehension syntax can also be used yo create sets and dictionaries
