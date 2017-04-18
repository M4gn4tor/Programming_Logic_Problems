# Write a program that by receiving a positive integer N
# in hexadecimal form is able to verify if this same number
# in decimal form could be read the same, backwards.
# If so, the program must return a line with the character 'S',
# otherwise, the character returned must be 'N'

aux = input("Type a hexadecimal number")
iOriginal = int(aux, 16)
sOriginal = str(iOriginal)

iReversed = [0] * len(sOriginal)

count = 0

for i in range(len(sOriginal)-1, -1, -1):
    iReversed[count] = sOriginal[i]
    count += 1

sReversed = "".join(iReversed)

if(sReversed == sOriginal):
    print('S')
else:
    print('N')

# Test

# Input:
# 1E1B9
# Expected output:
# S

# Input:
# 1E240
# Expected output:
# N