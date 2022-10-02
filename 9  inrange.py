print("program to find the number is falls in given range")
def find(s):
    if s in range(1,100,1):
        print("yes")
    else:
        print("no")


n=int(input("enter the number"))
find(n)