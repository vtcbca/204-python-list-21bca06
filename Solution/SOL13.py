"""WAS to enter any number to print pattern 

	* * * * *
  	  * * * *
    	    * * *
      	      * *
       	        * """
n=int(input("Enter any number="))
i=1
while i<=n:
    j=n
    while j>=i:
        print("*",end=" ")
        j=j-1
    print()
    i=i+1
