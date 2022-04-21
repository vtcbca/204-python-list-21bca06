# WAS to enter any number and check it is palindrome number or not.

no=int(input("Enter a value="))
sum=0
temp=no
while(no>0):
    x=no%10
    sum=sum*10+x
    no=no//10
if(temp==sum):
    print("{} is a palindrome number.".format(temp))
else:
    print("{} is not a palindrome number.".format(temp))
