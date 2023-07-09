string_test = '54321'
substring_test = '123'
print(string_test)
print(substring_test)

string = list(string_test)
substring = list(substring_test)

contained = False  

for i in range (len(string_test) - len(substring_test) + 1):
    if substring[0] == string[i]: 
        contained = True   
        for j in range (1, len(substring_test)):
            if substring[j] != string[i + j]: 
                contained = False
                break
    if contained:
        break
            
if contained == False:
    print("It is not a substring.")
else: 
    print("It is a substring.")
