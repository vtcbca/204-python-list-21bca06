'''WAP to create UDF which create 2 list Student and Address which contain student name and respected address of student.
Create new UDF which print student name with appropiate student address.'''


std=[]
add=[]
def stdad():
    for i in range(5):
        s=input("student:")
        std.append(s)
        a=input("address:")
        add.append(a)
stdad()
for i in range(5):
        print(std[i],'lives in ',add[i])
