
# Variables: objects containing specific values

x = 5 
# numeric/integer value is being stored in variable x
print (x)

y="We want to be great at python programming"
# string value is being stored in variable y
print (y)

x=15
print (x)
# the printed value of x shall now be 15
# as the interpretor runs from tom to bottom
# so it updates the value of x in the line 11

# similarly
x=x+15
print (x)

#types of variables
type (x) #func is used to get 'type' of variable stored value
print (type(x)) #adding print command gives us value on terminal

#similarly
print (type (y))

#anything that we need output from in the terminal, we need to use print command for it
#otherwise the values shall keep updating and being used within the program

# Rules of Assigning Variable Names
# 1- Should only be letters, numbers or underscore
# 2- Do not start with numbers
# 3- spaces are not allowed, always use underscore
# 4- do not name them as python keywords (eg print, input etc)
# 5- short and descriptive
# 6- Case Sensitive (try to use lower cases always)

fruit_basket= "mangoes","oranges"
fruit_basket2="mangoes,oranges"
print (fruit_basket)
print (fruit_basket2)

# del command is used to del variable
del fruit_basket

print (fruit_basket)
print (fruit_basket2)

# print (fruit_basket)
# NameError: name 'fruit_basket' is not defined. 
# Did you mean: 'fruit_basket2'?
#****** such error comes