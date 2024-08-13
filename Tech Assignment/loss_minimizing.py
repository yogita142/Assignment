def minimize_loss(prices):
    min_loss = float('inf')
    buy_year = sell_year = -1
    
    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            if prices[buy] > prices[sell]:
                loss = prices[buy] - prices[sell]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = buy + 1
                    sell_year = sell + 1
    
    if buy_year == -1:
        return "No loss can be made."
    else:
        return f"Buy in year {buy_year}, sell in year {sell_year}, with a minimum loss of {min_loss}"


prices = [20, 15, 7, 2, 13]
result = minimize_loss(prices)
print(result)
