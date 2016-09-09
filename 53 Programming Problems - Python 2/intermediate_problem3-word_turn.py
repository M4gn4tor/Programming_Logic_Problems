# For this problem consider that a chain is rotated when a quantity of
# characters N is inserted from the end to the beginning of the chain. For
# example, the possible rotations for the word 'language' are:
#
# anguagel
# nguagela
# guagelan
# uagelang
# agelangu
# gelangua
# elanguag
# language
#
# Note that even the word 'language' itself is considered as a rotation.
# Write a program that verifies if a chain S2 can be obtained from a chain S1's
# rotation.
# The program must read both the chains S1 and S2 and return 1 if S1 can be
# obtained from chain S2's rotation. Otherwise, it returns 0.

s1 = raw_input("Type chain S1: ")
s2 = raw_input("Type chain S2: ")

s2_list = list(s2)
s1_list = list(s1)

not_rotation = 1

for _ in range(len(s2)+1):
    s2_char = s2_list.pop(0)
    s2_list.append(s2_char)
    if s1_list == s2_list:
        print 1
        not_rotation = 0
        break
    else:
        continue

if not_rotation:
    print 0

# Test
# Input:
# programming
# programming
# Expected output:
# 1

# Input:
# programming
# gprogrammin
# Expected output:
# 1

# Input:
# anything
# nanythig
# Expected output:
# 0
