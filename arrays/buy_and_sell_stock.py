def buyandsell(prices):
    buy=0
    sell=0
    left=0
    right=1   
    max_profit=0 
    while right<len(prices):
        if prices[right]<prices[left]:
            left=right
        else:
            profit=prices[right]-prices[left]
            if profit>max_profit:
                max_profit=profit
                buy=left
                sell=right
        right+=1
    return f"The buy day is: {buy+1}, The sell day is: {sell+1},The total profit is: {max_profit}"



prices = [7, 1, 5, 3, 6, 4]
print(buyandsell(prices))