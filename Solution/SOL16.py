'''Write a script to enter any word and check it is palindrom or not.

	Eg: naman

	naman is palindrom word.'''

s=input("Enter any string:")
c=s
c=s[: : -1]
if(c==s):
    print("{} is palindrome word.".format(s))
else:
    print(" {} is not palindrome word.".format(s))
