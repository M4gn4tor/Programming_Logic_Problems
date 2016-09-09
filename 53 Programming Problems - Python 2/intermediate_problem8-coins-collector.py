# Coins Collector

# A coins collector aims to collect as many different coins as possible (quality
# or value are not important).
# Write a program that, receiving an array A with the value of the coins and an
# array C with the coins that the collector owns, inform the maximum of
# different coins that the collector can get.
# Consider that the collector can only get money to buy new coins if he sells
# the coins that he owns.

# The A array input will be as follows:
# - A first line with a Na integer (1<=Na<=100) identifying the quantity of
# elements of A.
# - Na lines with Ka integers (1<=Ka<=50). Each element Ka represents the value
# of each coin which its name is the K position starting from zero (see
# example).

# The C array input will be as follows:
# - A first line with a Nc integer (1<=Nc<=Na).
# - Nc lines with Kc integers (0<=Kc<=Ka-1). Each element Kc represents the name
# of a coin that the collector owns.

Na = 0
while not 1 <= Na <= 100:
    Na = input("Type quantity of existent coins: ")

print("Type its values: ")
coin_prices = []
Ka = 0
while Ka < Na:
    aux = input()
    if 1 <= aux and aux <= 50:
        coin_prices.append(aux)
        Ka += 1

Nc = 0
while not 1 <= Nc <= Na:
    Nc = input("Type quantity of coins the collector owns: ")

Kc = 0
coins_owned = []
while Kc < Nc:
    aux = input()
    if 0 <= Kc and Kc <= Ka-1:
        coins_owned.append(aux)
        Kc += 1

total_money = 0
for i in range(len(coins_owned)):
    total_money += coin_prices[coins_owned[i]]

# Order prices
possible_coins = 0
for i in sorted(coin_prices):
    if 0 <= total_money - i:
        total_money -= i
        possible_coins += 1
    else:
        break

print "Possible coins: %d" % possible_coins
