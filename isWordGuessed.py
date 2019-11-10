secretWord = "apple"
lettersGuessed = []
def isWordGuessed(secretWord,lettersGuessed):
   x = 'a','p','l','e' in lettersGuessed

   y = True in x
   return y
while isWordGuessed(secretWord,lettersGuessed) == False:

   answer = input("Guess a character: ") 
   lettersGuessed.append(answer)    
   if answer == "A" or  answer == "a" or  answer == "P" or  answer == "p" or  answer == "L" or  answer == "l" or  answer == "E" or  answer == "e":
       print("correct letter")
   print(isWordGuessed(secretWord,lettersGuessed))
