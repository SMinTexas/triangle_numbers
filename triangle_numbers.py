# Print the first 100 triangle numbers.
# This is the triangular number sequence:
#  1, 3, 6, 10, 15, 21, 28, 36, 45 ...

def triangle_numbers(number):
    for i in range(1, number + 1):
        print("n = {0}, triangle = {1}".format(i, (i ** 2 + i)//2))

triangle_numbers(100)