import random
usr = 0
cmp = 0
time = input("Enter a how many rounds  want to play")
for i in time:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if(usr != 2 or cmp != 2):
      if user_action == computer_action:
          print(f"Both players selected {user_action}. It's a tie!")
      elif user_action == "rock":
          if computer_action == "scissors":
              usr += 1
              print("Rock smashes scissors! You win!")
              if(usr == 2):
                print("you win")
                break
          else:
              cmp += 1
              print("Paper covers rock! You lose.")
              if(cmp == 2):
                print("you are a loser")
                break
      elif user_action == "paper":
          if computer_action == "rock":
              usr += 1
              print("Paper covers rock! You win!")
              if(usr == 2):
                print("you win")
                break
          else:
              cmp += 1
              print("Scissors cuts paper! You lose.")
              if(cmp == 2):
                print("you are a loser")
                break
      elif user_action == "scissors":
          if computer_action == "paper":
              usr += 1
              print("Scissors cuts paper! You win!")
              if(usr == 2):
                print("you win")
                break
          else:
              cmp += 1
              print("Rock smashes scissors! You lose.")
              if(cmp == 2):
                print("you are a loser")
                break