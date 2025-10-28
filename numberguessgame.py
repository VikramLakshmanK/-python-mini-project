import random
opt=input("START/END").lower()
c=input("WANT HINT(yes/no)").lower()
count=0
a=random.randint(1,100)
if c=="yes": 
    print(f"lower limit-{a-10} AND upper limit-{a+10}")  
else:
    pass    
while opt =="start":
    b=int(input("Guess the number between(1-100)"))
    if b==a:
        print("you Guessed Correct value")
        print(f"You guessed corrent number in {count} attempt")
        break
    elif b<a:
        count=count+1
        print("The value is too low")
    elif(b>a):
        print("The value is too high")
        count=count+1
    else:
        print("invalid")
else:
    print("Thank you \u263A")  
             
                
