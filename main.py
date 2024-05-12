
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def comp_cards():
  computer_cards=[]
  total=0
  first_comp= random.choice(cards)
  computer_cards.append(first_comp)
  total=int(first_comp) 
  while total<18  :
    X=random.choice(cards)
    
    if X==11:
      if total<=10:
        X=11
      else:
        X=1
    computer_cards.append(X)
    total+=int(X)    
  print(f"computer's first card: {computer_cards[0]}") 
  return computer_cards
      
def user():
  user_cards=[]
  first_card=random.choice(cards)
  total=int(first_card) 
  second_card=random.choice(cards)
  if second_card==11:
    if total>10:
      second_card=1
  user_cards.append(first_card)
  user_cards.append(second_card)
  total+=int(second_card)
  print(f"Your cards: {user_cards}, your score is {total}.")
  decision='h'
  while decision=='h':
    decision=input("would you like to hit or stand? Type H or S\n").lower()
    if decision=='h':
      X=random.choice(cards)
      if X==11:
        if total<=10:
          X=11
        else:
          X=1
      print(X)
      total+=int(X)
      print(f'total is {total}.')
      user_cards.append(X)
      print(user_cards)
    if total>=21 :
      break
  return total 

def compare():  
  co=comp_cards()
  us=user()
  print(f"Your total is {us}")
  total_comp=0
  for i in co:
    total_comp+=int(i)
  print(f"computer's cards are {co} and total is {total_comp}")
  if total_comp>21 and us>21 or total_comp==us:
    print("It's a draw!")
  elif total_comp>21 and us<=21 or us<=21 and us>total_comp:
    print("You win!")
  elif total_comp<=21 and us>21 or total_comp<=21 and total_comp>us:
    print("computer wins!")

from art import logo
from replit import clear
#start=input("Welcome to black jack! Start a game? Type Y or N. ").lower()
#while start=='y':
start=input("Do you want to start a game? Type Y or N ").lower()
while start=='y':
  clear()
  print(logo)
  compare()
  start=input("Do you want to start a game? Type Y or N ").lower()