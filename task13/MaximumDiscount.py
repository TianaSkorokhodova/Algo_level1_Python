def MaximumDiscount (N, price):

    for i in range (len(price) - 1) :
        for j in range (len(price) - i - 1) :
            if price[j] < price[j+1] :
                change = price[j]
                price[j] = price[j+1]
                price[j+1] = change           

    arrsOfPrices = []
    size = 3
    while len(price) > size:
        a = price[:size]
        arrsOfPrices.append(a)
        price = price[size:]
    arrsOfPrices.append(price)

    maxDiscount = 0
    for i in range (len (arrsOfPrices)) :
        if len(arrsOfPrices[i]) == size :
            minPrice = min(arrsOfPrices[i])
            maxDiscount += minPrice
    return maxDiscount
