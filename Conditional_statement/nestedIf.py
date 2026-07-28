age = int(input("Enter your age : "))

if age>=18:
    license = input("Do you have licence? : ")
    if license=="yes":
        print("You can drive")
    else:
        print("nee to take licence")    
else:
    print("You are too young to drive")    