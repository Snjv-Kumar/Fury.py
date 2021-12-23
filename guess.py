n=18
k=1
print("number of guess is 5")
while (k<=5):
    j=int(input("guess the number"))
    if j<n:
        print("please select high number")
    elif j>n:
         print("print select low number")
    else:
        print("you won")
        print("you won it in :",k,"chances")
        break
    print(5-k,"no.of guess left")
    k+=1
if k>5:
    print("you are out of chances")