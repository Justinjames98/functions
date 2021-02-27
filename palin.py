def pal(a):
    temp=a
    rev=0
    while(a !=0):
        remainder=a%10
        rev=(rev*10)+remainder
        a=a//10
    if(rev==temp):
        x="is palindrome"
    else:
        x="not a palindrome"
    return x
a=int(input("enter a number"))
x=pal(a)
print(x)