import sys

first = sys.argv[1]
last = sys.argv[2]

email = first.lower().replace(" ", ".") + last + "@company.com"

print("\n-----YOUR PROFILE------" )
print("Your name : " + first + last)
print("Your Email id : " + email)