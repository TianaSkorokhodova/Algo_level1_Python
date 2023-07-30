def ShopOLAP(N, items):
    listItems = []   
    additional = []
    result = []

    items.sort() 

    for i in range (N) :
        listItems.append(items[i].split())  

    additional.append(listItems[0])  

    for i in range (1, N) :
        lastItem = additional[len(additional) - 1]
        if lastItem[0] == listItems[i][0]:
            updatedValue = str(int(lastItem[1]) + int(listItems[i][1]))
            additional[len(additional) - 1] = [listItems[i][0], updatedValue]
        else:
            additional.append(listItems[i])       

    result = sorted(additional, key=lambda x: x[1], reverse=True) 

    for i in range (len(result)):
        result[i] = ' '.join(result[i])

    return result
