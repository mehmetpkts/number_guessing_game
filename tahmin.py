from random import randint
print("Number guessing game")
c=5
b=randint(0,50)
while c>0:
    k=input("Dial a number between 0-50: ")
    try:
        k = int(k)
    except:
        print("PLEASE KEY NUMBER ONLY")
        continue
    if k>b:
        print("Enter a smaller number")
        c=c-1
        print("your remaining life :",c)
        continue
    elif k<b:
        print("Enter a larger number")
        c = c - 1
        print("your remaining life :", c)
        continue
    else:
        print("YOU WIN")
        break
if c==0:
    print("YOU LOSE")
    print("THE COMPUTER SELECTED NUMBER :",b)