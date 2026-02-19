## function calling
def find_max_profit(price):
    minPrice = float('inf')
    maxProfit = 0

    for i in range(len(price)):
        if price[i] < minPrice:
            minPrice = price[i]
        elif price[i] - minPrice > maxProfit:
            maxProfit = price[i] - minPrice
    return maxProfit

## Driver Code
price = [7,1,5,3,6,4]
max_profit_value = find_max_profit(price)
print("The maximum profit of the stock is:",max_profit_value)