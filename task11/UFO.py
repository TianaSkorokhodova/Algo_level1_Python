def UFO (N, data, octal) :
    
    data10 = []
    if octal :
        base = 8
    else :     
        base = 16

    for i in range (len(data)) :
        dataStr = str (data[i])
        number = 0
    
        for j in range (len(dataStr)) :    
            number += int(dataStr[j]) * (base ** (len(dataStr) - 1 - j))
        data10.append(number)
        
    return data10  
