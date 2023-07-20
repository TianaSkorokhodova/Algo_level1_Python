def BigMinus (s1, s2) :
    sBigger = s1
    sSmaller = s2

    if len (s1) < len (s2) :
        sBigger = s2
        sSmaller = s1
    elif len (s1) == len (s2) :
        for i in range (len (s1)) :
            if s1[i] > s2[i] :
                sBigger = s1
                sSmaller = s2
                break
            elif s1[i] < s2[i] :
                sBigger = s2
                sSmaller = s1
                break

    sResultReversed = ""

    borrow = 0    

    for i in range (len (sBigger)) :
        minus = 0
        if i < len (sSmaller):
            minus = int(sSmaller[len(sSmaller) - 1 - i])

        subtraction = int(sBigger[len(sBigger) - 1 - i]) - minus - borrow

        if subtraction < 0 :
            subtraction += 10
            borrow = 1
        else :
            borrow = 0

        sResultReversed += str (subtraction)

    sResult = sResultReversed[::-1]

    for i in range (len(sResult) - 1) :

        if int(sResult[0]) == 0 :
            sResult = sResult[1:]  

    return sResult 
