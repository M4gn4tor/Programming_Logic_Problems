# Aliens from Yks planet compete to see who can write a
# text with teh greater number of words with N (1<=N<=10)
# characters.

# Write a program to automate the math and count how many
# words with N characters there are in the text typed.
# The program must receive a number N and a text up to 250
# characters long. The output is the quantity of words with N
# syllables that the text has.

# Note: to solve this problem you need to know that in the Yks'
# writing system a blank space is not used to separate words,
# instead, any character that's not a lowercase between a and z
# is considered a word separator.

n = 0
while not 1 <= n <= 10:
    n = input("Type the number of words: ")

line = raw_input("Text: ")
result = 0
count = 0
for i in range(len(line)):
    if line[i].islower():
        count += 1
    else:
        if count == n:
            result += 1
        count = 0

count = 0

# Verify if last word is valid if it is not a separator character
if len(line)-n > 0:
    for i in range(len(line)-n, len(line)):
        if line[i].islower():
            count += 1
    if count == n:
        result += 1

print result

# Test

# Input:
# 3
# sss.aasd.sss...
# Expected output:
# 2

# Input:
# 2
# 123123kj244141hm22242420+-xx....sadf...dfadfa..sd.
# Expected output:
# 4

# Input:
# 5
# asdfg..lk..ujjmjh...lkium
# Expected output:
# 2