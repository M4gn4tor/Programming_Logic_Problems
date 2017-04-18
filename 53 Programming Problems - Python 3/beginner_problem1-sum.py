# Run a program that's able to ask the user a number N
# (1 < N < 1000) and read N integers. After reading
# the last number, it must result:
# - On the first line: sum of N numbers in decimal base
# - On the second line: hexadecimal sum of even numbers
# - On the third line: octal sum of odd numbers

size_n = 0
while not 1 < int(size_n) < 1000:
    size_n = int(input('Type how many numbers will be inserted'))
_sum = 0
size_n = int(size_n)
n = [0] * size_n

for i in range(size_n):
    n[i] = int(input('Type a number'))
    _sum += n[i]

print("Decimal {sum}".format(sum=_sum))

# Test

# Input:
# 3
# 1
# 2
# 3
# Expected output:
# 6
# 2
# 4

# Input:
# 10
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# Expected output:
# 45
# 14
# 31
