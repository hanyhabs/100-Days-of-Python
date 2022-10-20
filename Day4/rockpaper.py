import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = ['rock','paper','scissors']
computer = random.choice(choices)
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
print(f'computer chose {computer}')
if(user == 0 and computer == 'scissors'):
  print(f'user: {rock}')
  print(f'computer: {scissors}')
  print('You wins')
elif(user == 1 and computer == 'rock'):
  print(f'user: {paper}')
  print(f'computer: {rock}')
  print('You wins')
elif(user == 2 and computer == 'paper'):
  print(f'user: {scissors}')
  print(f'computer: {paper}')
  print('You wins')
elif(user == 0 and computer == 'paper'):
  print(f'user: {rock}')
  print(f'computer: {paper}')
  print('Computer wins')
elif(user == 1 and computer == 'scissors'):
  print(f'user: {paper}')
  print(f'computer: {scissors}')
  print('Computer wins')
elif(user == 2 and computer == 'rock'):
  print(f'user: {scissors}')
  print(f'computer: {rock}')
  print('Computer wins')
elif(user == 0 and computer == 'rock'):
  print(f'user: {rock}')
  print(f'computer: {rock}')
  print('Draw')
elif(user == 1 and computer == 'paper'):
  print(f'user: {paper}')
  print(f'computer: {paper}')
  print('Draw')
elif(user == 2 and computer == 'scissors'):
  print(f'user: {scissors}')
  print(f'computer: {scissors}')
  print('Draw')
else:
  print('Invalid input')
