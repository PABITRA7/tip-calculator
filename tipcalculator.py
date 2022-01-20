
print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $")) 

tip = float(input("What percentage tip would you like to give? 10,12 or 15? "))

numberOfPeople = float(input("How many people to split the bill? ")) 


pay = round((totalBill+(totalBill*tip/100))/numberOfPeople,2)

print(f"Each person should pay: ${pay}")



