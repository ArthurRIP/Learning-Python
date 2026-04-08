import random


flag=False
Tries_Count=0
GEN_NUM = random.randint(1,100)
print("try to guess the number between 1 to 100")
while not flag:
    try:
        IN_NUM = int(input())
    except:
        print("write a fucking you fucking trash to you whole family")
        IN_NUM = int(input())
    if IN_NUM > GEN_NUM:
        print("number is greater then generated numebr, pls try again")
        Tries_Count=Tries_Count+1
    elif IN_NUM < GEN_NUM:
        print("number is samller then the generated number, pls try again")
        Tries_Count=Tries_Count+1
    else:
        print("bravo you guess in",Tries_Count,"tries, now fuckk off")