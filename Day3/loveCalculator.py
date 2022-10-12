# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name  = name1 + name2
name = name.upper()
total = 0
love = 0

#true = 0
# love =0
# t = name.count('T')
# r = name.count('R')
# u = name.count('U')
# e = name.count('E')

# true = t+r+u+e 

# l = name.count('L')
# o = name.count('O')
# v = name.count('V')
# e = name.count('E')

# love = l+o+v+e
# score = int(str(true)+str(love))

for i in range(len(name)):
    if name[i] =='T' or name[i] == 'R' or name[i] == 'U' or name[i] =='E':
        total+=1
    if name[i]=='L' or name[i] == 'O' or name[i] == 'V' or name[i]=='E':
        love +=1
score = int(str(total)+str(love))
if(score < 10 or score > 90):
    print(f'Your score is {score}, you go together like coke and mentos.')
elif(score >= 40 and score <= 50):
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')

#print(f'Your score is {str(total)+str(love)}.')
        
    
