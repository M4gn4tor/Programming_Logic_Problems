# Write a program that's able to ask an integer N 
# number from the user (1<N<1000) and read N integers.
# After reading the last number, the program must inform,
# with one decimal point, the mean between the N numbers
# that are in the closed interval -1000 and 1000
size = 0

while not 1 < size < 1000:
    size = input("Type the number of repetitions\n")
n = [0] * size
for i in range(size):
    aux = input("Type a number\n")
    if -1000 <= aux <= 1000:
        n[i] = aux

print sum(n)

# Test

# Input:
# 2
# 3
# 4
# Expected output:
# 3.5

# Input:
# 3
# 3
# 1001
# 4
# Expected output:
# 3.5

# Input:
# 3
# 3
# -1999
# 3
# Expected output:
# 3.0
