
#functions are commands that perform some tasks in python
# eg print() function is used to give output on terminal


# We can also define customized functions for our purposes
# for example


# print("We are learnin python")
# print("We are learnin python")
# print("We are learnin python")
# print("We are learnin python")
# print("We are learnin python")
# print("We are learnin python")
# print("We are learnin python")

# now the above function is printing multiple lines of code
# with the same error 'learnin' instead of 'learning'
# therefore we are going to define a fucntion to rectify this

#'def finction_name()' command is used to define

# method 1

def print_codanics():
    print("We are learnin python")
    print("We are learnin python")
    print("We are learnin python")
    print("We are learnin python")
    print("We are learnin python")
    print("We are learnin python")
    print("We are learnin python")

# print_codanics()


# # method 2

def print_codanics():
    text="We are learning python easily"
    print(text)
    print(text)
    print(text)

print_codanics()

# method 3

def print_codanics(text):
    print (text)
    print (text)
    print (text)

print_codanics("We are learning python in detail easily")

# method 4 
# defining a function with if, elif and else statements

def school_calculator(age,):
    if age==5:
        print ("Zara can join the school")
    elif age>5:
        print("Zara should go to higher school")
    else:
        print("Zara is still a baby")


# so now to use the above code snippet easily
# we have defined the function school_calculator
# now to calculate the answer, we shall put the value of variable in the brackets of the fucntion
# eg school_calculator(2)

school_calculator(5)
school_calculator(10)
school_calculator(2)


# method 5
# function defined by mathematical operators
# defining a function of future

def future_age(age):
    new_age=age+20
    print (new_age)
    return new_age

    
future_age(18)