# Write a program that's able to identify the most frequent word in a string
# of characters.
# The input will be a string of characters of no more than 1000 characters.
# The output the most frequent letter, followed by the with two floating points.
# You must differentiate lowercase from uppercase letters.
# Any other character that's not between A and Z must be dismissed in both the
# percentage calc and the counting. The output must be in lowercase letters.
_string = ''
# Read until it have a valid input
while _string == '':
    _string = input("Type a string\n")

dict_char = {}

# Include letters and its occurencies in a dictionary
for _ in _string:
    if _.isalpha():
        if tuple(_) in dict_char.keys():
            dict_char[tuple(_)] += 1
        else:
            dict_char[tuple(_)] = 1

# Identify the maximum number of occurencies
max_count = max([v for k, v in dict_char.items()])
# Count how many items there are in the original string, including only A to Z
count = sum([v for k, v in dict_char.items()])
# Displays the results
for k, v in dict_char.items():
    if v == max_count:
        print("{} {:.2f}%".format(k[0], (max_count / float(count) * 100)))

# Test
# Input:
# aabc
# Expected output:
# a 50.00%

# Input:
# aabcc
# Expected output:
# a 40.00%
# c 40.00%

# Input:
#  asl;dzc]ewa;d]sd.vcxhkjasdfa]]bkjolnnopuibuiopjl;
# Expected output:
# a 9.76%
# d 9.76%
