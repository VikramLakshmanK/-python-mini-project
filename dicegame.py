import random
poss=[]
def turn(option):
    if option == "yes":
        a=random.randint(1,6)
        c=random.randint(1,6)
        poss.append(a)
        poss.append(c)
        return poss
    else:
        return "Thank you Playing"
b=input("Roll the Dice? (yes/no)")    
dice=turn(b.lower())
print(dice)        