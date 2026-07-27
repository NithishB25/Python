amount = int(input("Enter your amount:"))

tax = amount *0.18
total = amount + tax

if total>1000:
    discount = amount*0.8
    total-=discount
    print(total)