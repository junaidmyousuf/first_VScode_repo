
# loops are very important as most work is done on them in python

# while loops

x=0
while (x<=5):
    print(x)
    x=x+1           # if not this increment the value shall remain the same for infintiy


# for loop

for x in range(5,10):
    print (x)


# How do you use loops in a program
# lets say we have an array (array is known as a dataset having values in it)

days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]

for d in days:
    if(d=="fri"):break      # loop stops when it reaches "fri" in array
    if (d=="fri"):continue  # skips the string "fri" in the array
    print (d) 
