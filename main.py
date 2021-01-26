############### Blackjack Project #####################
import random
from replit import clear
from art import logo

def deal_card():
 cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 return random.choice(cards)

def calculate_score(card_list):
  card_list_sum = sum(card_list)
  if 11 in card_list and 10 in card_list and len(card_list) == 2:
    return 0
  if 11 in card_list and card_list_sum > 21 :
     card_list.remove(11)
     card_list.append(1)
     return card_list_sum

def compare(user_score,ai_score):
  if ai_score == user_score:
    print("a draw")
  elif user_score >21 and ai_score > 21 :
    print ("you lose")
  elif ai_score == 0 :
    print ("you lose, Dealer has blackjack")
  elif user_score == 0 :
    print ("That's a blackjack ,you win")
  elif  ai_score > 21  :
    print ("you win")
  elif user_score >21  :
    print ("you lose")
  elif  ai_score > user_score :
    print ("you lose")
  else :
    print ("You Win")
   
def blackjack() :
  print(logo)

  user_cards = []
  computer_cards = []
  game_off = False
  for num_of_cards in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  
  while not game_off:
    ai_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
  
    print(f"Your cards : {user_cards},current score : {user_score}")
    print(f"Dealer's first card : {computer_cards[0]}")

    if user_score ==0 or ai_score ==0 or user_score >21 :
     game_off = True 
  
    else :

      choice = input("Do you want to draw another card 'y'or 'n' ").lower()
      if choice == 'y':
       user_cards.append(deal_card())
       user_score = calculate_score(user_cards)
      else : 
         game_off = True 

  while ai_score !=0 and ai_score < 17 :
    computer_cards.append(deal_card())
    ai_score = calculate_score(computer_cards)

  print(f"Your final hand : {user_cards},final score : {user_score}")
  print(f"Dealer's final hand : {computer_cards}, dealers score : {ai_score}")
  compare(user_score,ai_score)
   
  restart = input("Do you want to restart 'y' or 'no' ").lower()
  if restart == 'y':
    clear()
    blackjack()
      
start =input("Do you want to play a game of Blackjack Type 'y' or 'n'  ").lower()
if start == 'y':
  blackjack()
    

