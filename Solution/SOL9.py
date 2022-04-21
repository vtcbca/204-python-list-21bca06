# WAS to enter any number and print the sum of its digit.

a=int(input("Enter number:"))
sum=0
while(a!=0):
    sum=sum+a%10
    a=a//10
print("Sum of it:",sum)
