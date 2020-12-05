#Luke Mackay,November 30th,2020
import random

print("What is your name?")
name_input = input()
secretNumber = random.randrange(1,101)
guess_number = 0
num_of_tries = 0
limited_tries = 7
game_over = False

is_valid_input = False
while is_valid_input == False:
  print ("choose a difficulty:\n medium is 1 to 100 \n hard is 1 to 1000")
  difficulty = input()
  if difficulty == 'hard':
    secretNumber = random.randrange(1,1001)
    limited_tries = 9
    is_valid_input = True
  elif difficulty == 'medium':
    is_valid_input = True
  else:
    print ("pick 'medium' or 'hard' please")


print ("welcome",name_input,"you have",limited_tries,"tries, you got this!")

while game_over == False:
  guess_input = "NONE"
  while guess_input.isdigit() == False:
    if limited_tries == num_of_tries:
      game_over= True
    print ("guess the secret number")
    guess_input = input()
    if guess_input.isdigit() == False:
      print ("Excuse me, try again")
    
  guess_number = int(guess_input)
  num_of_tries = num_of_tries + 1
  
  if limited_tries < num_of_tries:
    game_over = True
    print ("YOU USED",limited_tries,"TRIES")
    print("you did not get the number HOW? im dissapointed",name_input)

  elif guess_number < secretNumber:
    print("too low try again!",name_input)
  elif guess_number > secretNumber:
    print("too high try again!",name_input)
  elif guess_number == secretNumber:
    print("you got the number!!!")
    game_over = True
    print ("it took you",num_of_tries,"tries",name_input)

print ("GAME OVER")
  

