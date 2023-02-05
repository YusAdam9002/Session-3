def fractional(a, b):
    return a/b - a//b

print(fractional(5, 2))

def is_even(num):
    return fractional(num, 2) == 0

print(is_even(2)) # True
print(is_even(3)) # False

def largest_first(a, b, c):
    return a > b and a > c

print(largest_first(1, 2, 3))
print(largest_first(3, 2, 1))

def add_multiply(a, b, c):
    return (a + b) * c

print(add_multiply(1, 2, 3)) # 9
print(add_multiply(2, 3, 4)) # 20

def concatenate_ints(a, b, c):
    return int(str(a) + str(b) + str(c))

print(concatenate_ints(1, 2, 3))

def flip_bit(num, pos):
    return num ^ (1 << pos)

print(flip_bit(5, 0))
print(flip_bit(5, 1))

def manipulate_age(sentence, number):
    age = int(sentence[5:7]) + number
    return "I am " + str(age) + " years old"

print(manipulate_age("I am 15 years old", 3))