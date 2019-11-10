secretWord = "apple"
same = "False"
secretWordBlank = ["_","_","_","_","_"]
lettersGuessed = []
def isWordGuessed(secretWord,lettersGuessed):
   x = 'a','p','l','e' in lettersGuessed
   y = True in x

   return y
while isWordGuessed(secretWord,lettersGuessed) == False:

   answer = input("Guess a character: ") 
   lettersGuessed.append(answer)    
   if answer == 'a' or answer ==  'A':
       secretWordBlank[0] = 'a'
   elif answer == 'P' or answer ==  'p':
       secretWordBlank[1] = 'p'
       secretWordBlank[2] = 'p'
   elif answer == 'L' or answer ==  'l':
       secretWordBlank[3] = 'l'
   elif answer == 'E' or answer ==  'e':
       secretWordBlank[4] = 'e'
   print(isWordGuessed(secretWord,lettersGuessed))
   print(secretWordBlank)