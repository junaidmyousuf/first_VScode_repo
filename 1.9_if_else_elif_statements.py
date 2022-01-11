
required_age_at_school = int (5)
zara_age = int(input("Please enter the age of zara: "))

# Now the Question is Can Zara go to school ?

if zara_age==required_age_at_school:
    print("Zara is of school joining age")
elif zara_age>=int(15):
    print("Zara needs to join college")
elif zara_age>required_age_at_school:
    print("Zara needs to be assessed for higher classes")
else: 
    print ("Zara cannot join the school")