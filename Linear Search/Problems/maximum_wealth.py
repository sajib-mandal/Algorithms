# 1672. Richest Customer Wealth

def maximum_wealth(accounts):
    richest = 0
    for i in range(len(accounts)):
        total = 0
        for j in range(len(accounts[i])):
            total += accounts[i][j]
        if total > richest:
            richest = total
    return richest




print(maximum_wealth([[1, 2, 3],[3, 2, 1]])) # 6
print(maximum_wealth([[1, 5],[7, 3],[3, 5]])) # 10
