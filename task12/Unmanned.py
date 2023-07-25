def Unmanned (L, N, track) :
    
    travelTime = 0   
    prevLight = 0

    for i in range (N) :  
        if track[i][0] > L:
            break
            
        travelTime += track[i][0] - prevLight
        prevLight = track[i][0]

        fullCycle = track[i][1] + track[i][2] 

        if fullCycle != 0 : 
            a = travelTime % fullCycle
            redTime = track[i][1] - a

            if (redTime < 0):
                redTime = 0

            travelTime += redTime                                      
    
    
    travelTime += L

    travelTime -= prevLight

    return travelTime 
