#Module 3: Control Structures in Python
#Task 1: Check if a Number is Even or Odd

no=int(input("Enter a no.: "))
a=no%2
if (a==0):
    print( no , " is an even no.")
else:
    print(no , " is an odd no.\n\n\n")


#Task 2: Sum of Integers from 1 to 50 Using a Loop
sum = 0
for x in range(1,51):
    sum = sum + x ;
print("The sum of numbers from 1to 50 is: ", sum)
