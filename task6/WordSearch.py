def WordSearch(length, s, subs):
    
    position = 0  

    sPhrases = []   

    lastSpacePosition = -1  

    firstPosition = 0

    while position < len(s):
    
        if s[position] == " ":
        
            lastSpacePosition = position
        
        
        if position - firstPosition == length + 1:    
        
            if lastSpacePosition == -1:
        
                sPhrases.append(s[firstPosition:position - 1])
            
                firstPosition = position - 1
            
                position -= 1
            
            else: 
                sPhrases.append(s[firstPosition:lastSpacePosition])
            
                firstPosition = lastSpacePosition + 1
            
                position = lastSpacePosition + 1
            
                lastSpacePosition = -1
            
        position += 1
    
    if position > firstPosition:
    
        sPhrases.append(s[firstPosition:position])
    
        
    result = []
        
    for i in range (len(sPhrases)):
    
        if subs in sPhrases[i].split():
        
            result.append(1)
        
        else:
        
            result.append(0)
        
    return result
