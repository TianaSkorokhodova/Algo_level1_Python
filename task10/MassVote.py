def MassVote(N, Votes) :

    maximum = max (Votes)

    if Votes.count(maximum) == 1 :
    
        if Votes == [0] or ( maximum / sum(Votes) > 0.5 ) :
        
            return "majority winner " + str (Votes.index(maximum) + 1)
        
        else :
        
            return "minority winner " + str (Votes.index(maximum) + 1)
        
    else :
        
        return "no winner" 
