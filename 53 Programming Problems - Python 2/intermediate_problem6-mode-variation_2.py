# Mode is the group of most frequent numbers in a sample. For example, in the
# sample (1,2,3,3,3,4,4,4,4,5) the mode is {4}, in the sample
# (1,1,1,2,2,2,3,4,5,5,6) the mode is {1, 2}
# Write a program that's able to calculate the mode of a sample of K numbers.
# The input will be an undefined quantity of K elements, one per line.
# The output will be the mode elements of K, in ascending order, one per line.
# K will have as elements integers between 0 and 256, as 0 means end of input.

# Variation 2:
# K will have as elements strings without blank spaces, with less than 50
# characters. And the chain "0" (no quotes) means the end of input.

strings = []
n = ""
print "Type a string per line with less than 50 characters and no blank spaces"
while n != "0":
    n = raw_input()
    if len(n) < 50 and " " not in n and n != "0":
        strings.append(n)
print strings
# max_count = max((integers.count(x)) for x in set(integers))
# print "Mode(s):"
# for x in sorted(set(integers)):
#     if integers.count(x) == max_count:
#         print x

