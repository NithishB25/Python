#while1
'''correct = '1990'
enter = ''
while enter!=correct:
    enter = input("enter your input :")
print("access granted")    
'''

#whilw 2
'''count = 5
while count>0:
    print(f"the time is : {count}")
    count-=1
print("time is over ")
'''

# while 3
items = []
while True:
    item = input("enter the item to be added (use 'done' when i tis complete : ")
    if item.lower()=="done":
     break
    items.append(item)
print("your cart",items)

