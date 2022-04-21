# WAS to enter any number and check number is armstrong number or not.
no=int(input("Enter any number:"))
sum=0
temp=no
while(no>0):
    x=no%10
    y=x*x*x
    sum=sum+y
    n=no//10
if(temp==sum):
    print("{} is an armstrong number".format(temp))
else:
    print("{} is not an armstrong number".format(temp))
    
