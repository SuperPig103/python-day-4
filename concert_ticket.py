age = input("What is your age? ")
age = int(age)

if age < 13:
    print("$8")
elif age > 65:
    print("$10")
else:
    print("$1")