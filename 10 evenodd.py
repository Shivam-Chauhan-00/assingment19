print("program to check weather a given number is even or odd by function")
def evenodd(x):
    if x%2==1:
        print("the number is odd")
    else:
        print("the number is even")



n=int(input("enter the number: "))
evenodd(n)