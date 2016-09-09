# Run a program that's able to ask the user a number N
# (1 < N < 1000) and read N integers. After reading
# the last number, it must result:
# - On the first line: sum of N numbers in decimal base
# - On the second line: hexadecimal sum of even numbers
# - On the third line: octal sum of odd numbers

# Ask for the quantity of numbers to be inserted
quantity_of_numbers = 0
while quantity_of_numbers <= 1 or 1000 <= quantity_of_numbers:
    quantity_of_numbers = int(input('Type how many numbers will be inserted: '))

# Ask for the integers and sum them up
total_sum = 0
for i in range(quantity_of_numbers):
    total_sum += int(input('Type an integer : '))

# Presents the integers total sum
print("Decimal:", total_sum)
print("Hexadecimal:", hex(total_sum)[2:])
print("Octal:", oct(total_sum)[2:])
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
