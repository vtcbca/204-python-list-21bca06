'''WAS to print following pattern 
	1
	2 3
	5  6 7
	7  8 9 10
	11  12 13 14 
	13  14 15 16 17
	17   18  19 20 21'''

n=int(input("Enter any number:"))
no=1
for a in range(0,n):
    for b in range(0,a+1):
        print(no,end=' ')
        no=no+1
    print()
