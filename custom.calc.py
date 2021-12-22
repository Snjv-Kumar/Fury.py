n1=int(input("enter first number"))
k=input("select the operator:+,_,%,/,* ")
n2=int(input("enter the second number"))
d=(555)
c=(77)
e=(4)
if n1==45 and n2==3 and k=='*':
    print(d)
elif n1==56 and n2==9 and k=='+':
    print(c)
elif n1==56 and n2==6 and k=='/':
    print(e)
elif n1>=0 and n2>=0 and k=="*":
    mul=(n1*n2)
    print(mul)
elif n1>=0 and n2>=0 and k=='+':
    add=(n1+n2)
    print(add)
elif n1>=0 and n2>=0 and k=="/":
    div=(n1/n2)
    print(div)
elif n1>=0 and n2>=0 and k=="-":
    min=(n1-n2)
    print(min)
elif n1>=0 and n2>=0 and k=="%":
    per=(n1%n2)
    print(per)

else:
    print("Error:please enter valid inputs")

