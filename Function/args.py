#args for calculation 
def add (*args):
    total = 0
    for i in args:
        total+=i
    return total
print(add(45,45,45))