# Write a program that:
# - Reads a number N
# - Read N sequencies of 5 integers each
# - Print the N sequencies, alternating the order
# between ascending and descending

# Variation 1
# Solve the same problem, but assume that the number of elements in each sequence can vary.
# Before inputing each sequence, the user informs the number of elements in the sequence.

n = 0
while not 0 < int(n) <= 1000:
    n = int(input("Type the number of sequences: "))

_list = []
size = []

for i in range(n):
    size.append(int(input("Type the number of elements in the sequence: ")))
    for _ in range(size[i]):
        _list.append(int(input()))

aux_list = []
index_element_list = 0

for i in range(len(size)):
    for j in range(size[i]):
        aux_list.append(_list[index_element_list])
        index_element_list += 1
        if j == size[i] - 1:
            if i % 2 != 0:
                print("{a}".format(a=sorted(aux_list)))
            else:
                print("{a}".format(a=sorted(aux_list, reverse=True)))
            aux_list = []

# Test