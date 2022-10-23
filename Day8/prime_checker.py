#Write your code below this line 👇
def prime_checker(number):
    flag=False
    for i in range(2,n-1):
        if(n%i==0):
            flag=True
            break
        else:  
            flag=False
    if(flag==True):
        print(f"It's not a prime number.")
    else:
        print(f"It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
