""" Return a string value
    Return the lest number of coins with coin denomination from largest to smallest
    coins: a list of coins denomination that a branch has
    val: exchange amount 
"""
def get_min_coin(coins, val):
    coins.sort(reverse=True)

    if val < 0:
        return "-1 (insufficient coins available for exchange)"
    max_val = val + 1
    min_coins = [(max_val, None)] * (val + 1)
    min_coins[0] = (0, None)
    for coin in coins:
        for v in range(coin, val + 1):
            min_coins[v] = min((1 + min_coins[v - coin][0], coin), min_coins[v])

    if min_coins[-1][1] is None:
        return "-1 (insufficient coins available for exchange)"
    else:
        answer = []
        while 0 < val:
            answer.append(min_coins[val][1]) 
            val -= min_coins[val][1]
        
        answer.sort(reverse=True)
        answer_string = str(len(answer)) + " (" + " + ".join(map(str,answer)) + ")"
        return answer_string


print(get_min_coin([1, 5, 7, 9, 11], 25))
print(get_min_coin([1, 5, 7, 9, 11], 14))
print(get_min_coin( [7, 9], 20))