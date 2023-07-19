def PrintingCosts (Line) :

    theSum = 0

    for i in range (len (Line)):

        if Line[i] == " ":
            theSum += 0

        elif Line[i] == "'" or Line[i] == "`" :  
            theSum += 3 

        elif Line[i] == ".":
            theSum += 4

        elif Line[i] == '"':
            theSum += 6

        elif Line[i] == "," or Line[i] == "-" or Line[i] == "^" :  
            theSum += 7 

        elif Line[i] == ":" or Line[i] == "_" :  
            theSum += 8

        elif Line[i] == "~" or Line[i] == "!" :  
            theSum += 9

        elif Line[i] == ">" or Line[i] == "/" or Line[i] == "<" or Line[i] == "\\" :
            theSum += 10

        elif Line[i] == ";":
            theSum += 11

        elif Line[i] == "(" or Line[i] == "|" or Line[i] == ")" :  
            theSum += 12 

        elif Line[i] == "v" or Line[i] == "r" or Line[i] == "x" or Line[i] == "+":  
            theSum += 13 

        elif Line[i] == "Y" or Line[i] == "=" :  
            theSum += 14

        elif Line[i] == "?" or Line[i] == "i" :  
            theSum += 15

        elif Line[i] == "L" or Line[i] == "T" or Line[i] == "l" or Line[i] == "7":  
            theSum += 16

        elif Line[i] == "t" or Line[i] == "c" or Line[i] == "u" or Line[i] == "*":  
            theSum += 17

        elif Line[i] == "J" or Line[i] == "n" or Line[i] == "]" or Line[i] == "{" or Line[i] == "X" or Line[i] == "}" or Line[i] == "f" or Line[i] == "I" or Line[i] == "[":
            theSum += 18

        elif Line[i] == "V" or Line[i] == "z" or Line[i] == "w" or Line[i] == "1":
            theSum += 19

        elif Line[i] == "o" or Line[i] == "F" or Line[i] == "j" or Line[i] == "C":
            theSum += 20

        elif Line[i] == "h" or Line[i] == "K" or Line[i] == "4" or Line[i] == "k" or Line[i] == "s":
            theSum += 21

        elif Line[i] == "2" or Line[i] == "0" or Line[i] == "Z" or Line[i] == "%" or Line[i] == "m" : 
            theSum += 22

        elif Line[i] == "&" or Line[i] == "#" or Line[i] == "A" or Line[i] == "y" :
            theSum += 24

        elif Line[i] == "b" or Line[i] == "d" or Line[i] == "p" or Line[i] == "G" or Line[i] == "S" or Line[i] == "q" or Line[i] == "H" or Line[i] == "N":
            theSum += 25

        elif Line[i] == "D" or Line[i] == "9" or Line[i] == "E" or Line[i] == "W" or Line[i] == "6" or Line[i] == "O":
            theSum += 26

        elif Line[i] == "5":
            theSum += 27

        elif Line[i] == "R" or Line[i] == "M" :  
            theSum += 28

        elif Line[i] == "$" or Line[i] == "B" :  
            theSum += 29

        elif Line[i] == "g":
            theSum += 30

        elif Line[i] == "Q":
            theSum += 31

        elif Line[i] == "@":
            theSum += 32

        else:
            theSum += 23

    return theSum
