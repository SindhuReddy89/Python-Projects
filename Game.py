import time
import random
name1=input("Enter the player1:")
name2=input("Enter the player2:")
print("comp has fixed 5 number of integers in its mind")
print("you both have three turns each toguess it")
print("Ready for the game??")
nums=[]
while(len(nums)!=5):
    a=random.randint(1,10)
    while(a in nums):
         a=random.randint(1,10)
    nums.append(a)
print(nums)
player1=[]
player2=[]
s1=0
s2=0
for i in range(3):
    print("Hai {} Guess ur choice No{}.format(name1,i+1)")
    x=int(input())
    while(x in player1 or x in player2):
        print("Already chosen,so guess someother num")
        x=int(input())
    player1.append(x)
    if x in nums:
        print("-->CORRECT")
        s1=s1+1
    else:
        print("-->WRONG")
for i in range(3):
    print("Hai {} Guess ur choice No{}.format(name2,i+1)")
    x1=int(input())
    while(x1 in player1 or x1 in player2):
        print("Already chosen,so guess someother num")
        x1=int(input())
    player2.append(x1)
    if x1 in nums:
        print("-->CORRECT")
        s2=s2+1
    else:
        print("-->WRONG")
print("\n------Game summery--------")
print("Lets have summary")
print("Comp has chosen {}".format(nums))
print(f"{name1} has chosen {player1}|score{s1}")
print(f"{name2} has chosen {player2}|score{s2}")
print(f"comp's numbers were :{nums}")
if(s1>s2):
    print(f"------------>{name1} is the WINNER<------------".format(name1))        
elif(s2>s1):
    print(f"------------>{name2} is the WINNER<------------".format(name2))
else:
    print("------------>{}DRAWN<---------------")
    
