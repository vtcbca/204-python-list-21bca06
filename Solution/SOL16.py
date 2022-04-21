'''Write a script to enter any word and check it is palindrom or not.

	Eg: naman

	naman is palindrom word.'''

s=input("Enter any string:")
c=s
c=s[: : -1]
if(c==s):
    print("{} is pallingdrom word.".format(s))
else:
    print(" {} is not pallingdrom word.".format(s))
