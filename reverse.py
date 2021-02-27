def rev(a):
    rev=0
    rem=0
    while(a!=0):
        rem=a%10
        rev=(rev*10)+rem
        a=a//10
    return rev
a=int(input("enter a number"))
result=rev(a)
print(result)