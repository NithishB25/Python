#and
'''mark = 70
att = 100
if mark>=55 and att>=70:
    print("allowed")
else:
    print("not allowed")

 '''
#or
'''mark = 20
att = 100
if mark>=55 or att>=70:
    print("allowed")
else:
    print("not allowed")
'''
# and,or

ord_amo = int(input("enter your amount : "))
day = input("enter the day of order :")
memb = input("enter your plan : ")
if (ord_amo>=1000 and day in ["sat","sun"]) or memb =='platinum':
    print("20% discount")
else:
    print("discount not found")
