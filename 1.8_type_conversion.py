x=5             #integer
y=12.5          #float
z="Hello"       #string

x=x*y           #operating float with integer gives float

# the above is called implicit type conversion
# which means type is converted internally

age=input("What is your age ? ")
print (type(age))
age=int(age)                     # type conversion explicit
print (age, type(int(age)))      # we can also write as this
print (type(age))

# the above code is called explicit conversion
# which means type is converted externally with extra lines of code and seperate finction

print (age, type(float(age)))    # float conversion  
print (age, str(int(age)))       # str conversion   

#name
name=input("What is your name ? ")
print(name, type(str(name)))

print(type(x))
print(type(y))
print(type(z))