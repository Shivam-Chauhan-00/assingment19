from re import S


print("program to multiply of all numbers in the lsit")
def multiplylist(x):
    s=1
    for e in x:
        s=e*s

    print("the multiply of lsit is",s)

l1=[1,2,3,4,5,]
multiplylist(l1)