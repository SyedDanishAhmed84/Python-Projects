import random

user_wins=0
computer_wins=0
draws=0

options=["rock", "paper" , "scissor"]

while True:
  user_input=input("rock/paper/scissor or q to Quit : ")
  if user_input == "q":
   break

  if user_input not in options:
   continue

  random_number=random.randint(0,2)
  computer_pick=options[random_number]
  print ("Computer picked",computer_pick)

  if user_input == "rock" and computer_pick == "paper":
   print ("You won!")
   user_wins=user_wins+1 
   continue

  elif user_input == "paper" and computer_pick == "scissor":
    print ("You Won!")
    user_wins=user_wins+1

  elif user_input == "scissor" and computer_pick == "paper":
    print ("You Won!")
    user_wins=user_wins+1

  elif user_input == "paper" and computer_pick == "paper":
    print ("draw")
    draws=draws+1

  elif user_input == "rock" and computer_pick == "rock":
    print ("draw")
    draws=draws+1

  elif user_input == "scissor" and computer_pick == "scissor":
   print ("draw")
   draws=draws+1

  else:
    print ("Computer Won!")
    computer_wins=computer_wins+1
    
print ("You Won",user_wins,"times")
print ("Computer Won",computer_wins,"times")
print ("draw",draws,"times")
print ("Goodbye!")

    