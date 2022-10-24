from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
bidders={}
wanna_continue = True
while wanna_continue:
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  bidders[name]=bid
  qs = input('Are there any other biders? Type yes or no ')
  clear()
  if(qs == 'yes'):
    wanna_continue = True
  else:
    wanna_continue = False
max_val = 0

for k,v in bidders.items():
  if v > max_val:
    max_val = v
    max_key = k
print(f"Bid won by {max_key} for ${max_val}.")
