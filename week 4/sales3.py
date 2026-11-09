days=int(input("Number Of Days: "))
total=0
greater_day=0
less_day=0
if days<=0:
    print("ERROR")
    days=int(input("Number Of Days: "))
else:
    for i in range(days):
        i+=1
        sales=int(input(f"Sales For Day{i}: "))
        if sales<0:
            print("error, sales cannot be negative")
            sales=int(input("Sales For Day{i}: "))
        elif sales>10000:
            total+=sales
            greater_day+=1
            
        else:
            total+=sales
            less_day+=1
            pass
average=total/i
print(f"Total Sales: NGN{total:.2F}")
print(f" Average Daily Sales: NGN{average:.2F}")
print(f

        
