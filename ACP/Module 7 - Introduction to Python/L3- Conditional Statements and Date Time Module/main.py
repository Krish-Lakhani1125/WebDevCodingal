import datetime

current_time = datetime.datetime.now()


grade = 60

if grade >=90:
    print("You have an A!")
elif grade >=80:
    print("You have a B!")
elif grade >=70:
    print("Oh No! You have a C")
elif grade <70:
    print("Oh No! You are failing")

print("Your grade as of", current_time, "is:", grade)

