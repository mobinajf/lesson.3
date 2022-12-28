import math

def moadele_daraje2():
    a=int(input("please enter a:"))
    b=int(input("please enter b:"))
    c=int(input("PLease enter c:"))
    delta=(b**2)-(4*a*c)
    if delta==0:
        x=(-b/2*a)
        print("moadele_daraje2 has one answer:",x)
    elif delta>0:
        x1=(-b+math.sqrt(delta)/a*2)
        x2=(-b-math.sqrt(delta)/2*a)
        print("The answers of the moadele_daraje2:",x1,"&",x2)
    elif delta<0:
        print("moadele_daraje2 has no answer")

moadele_daraje2()    