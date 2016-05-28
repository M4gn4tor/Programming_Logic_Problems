# At a bar, the men receive identification cards with odd numbers and
# women receive cards with even ones.
# A showman hired to cheer up the public wants to know if there is a 
# one-to-one proportion between men and women.
# You have to write a program that verifies that:
# The program receives a number N (1<=N<=1000) with the quantity of
# distributed cards and a list with N integer positive numbers (1<=N<=500),
# each one representing the number in a card. The output must be a single
# line with 'S' if there is the proportion, or 'N' otherwise.

iNumber_of_cards = 0
while 1 <= iNumber_of_cards <= 1000:
    iNumber_of_cards = input("Type the number of cards distribuited\n")
iNumber_of_cards = [0] * iNumber_of_cards
line = ""
while not 1 <= len(line) <= 500:
    line = raw_input("Type the number of the cards distributed\n")
iNumber_of_cards = line.split()
iOdd = 0
iEven = 0

if len(iNumber_of_cards) % 2 == 0:
        for i in range(len(iNumber_of_cards)):
            if int(iNumber_of_cards[i]) % 2 == 0:
                iEven += 1
            else:
                iOdd += 1

        if iEven == iOdd:
            print "S"
        else:
            print "N"
else:
    print "N"

# Test

# Input:
# 6
# 1 2 3 4 5 6
# Expected output:
# S

# Input:
# 8
# 1 3 5 7 9 11 13 15
# Expected output:
# N

# Input:
# 4
# 1 2 3 4
# Expected output:
# S

# Input:
# 6
# 1 2 3 4 8 7
# Expected output
# S
