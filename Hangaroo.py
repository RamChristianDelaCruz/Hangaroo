print ("                                                        Hangaroo Game")
input("Press a key to play Hangaroo: ")
secretWord = ['I', ' ', 'l','o','v','e', ' ', 'p','r','o','g','r','a','m','m','i','n','g']
secretWordBlank = ['_', ' ','_','_','_','_', ' ', '_','_','_','_','_','_','_','_','_','_','_']
x = 0
print("Guess the Phrase: ",secretWordBlank)
while secretWord != secretWordBlank:
    answer = input("Guess a character: ")
    if answer == 'I'or answer == 'i':
        secretWordBlank[0] = 'I'
        secretWordBlank[15] = 'i'
    elif answer == 'L'or answer =='l':
        secretWordBlank[2] = 'l'
    elif answer == 'O'or answer == 'o':
        secretWordBlank[3] = 'o'
        secretWordBlank[9] = 'o'
    elif answer == 'V'or answer =='v':
        secretWordBlank[4] = 'v'
    elif answer == 'E'or answer == 'e':
        secretWordBlank[5] = 'e'
    elif answer == 'P'or answer =='p':
        secretWordBlank[7] = 'p'
    elif answer == 'R'or answer == 'r':
        secretWordBlank[8] = 'r'
        secretWordBlank[11] = 'r'
    elif answer == 'A'or answer =='a':
        secretWordBlank[12] = 'a'
    elif answer == 'G'or answer == 'g':
        secretWordBlank[10] = 'g'
        secretWordBlank[17] = 'g'
    elif answer == 'M'or answer =='m':
        secretWordBlank[14] = 'm'
        secretWordBlank[13] = 'm'
    elif answer == 'I'or answer =='i':
        secretWordBlank[15] = 'i'
    elif answer == 'N'or answer =='n':
        secretWordBlank[16] = 'n'
    else:
        print("You are wrong,guess again")       
    print(secretWordBlank)
    x+=1
    if secretWord == secretWordBlank:
        print("Congrantulations! You beat the game in  ", x," Turns")