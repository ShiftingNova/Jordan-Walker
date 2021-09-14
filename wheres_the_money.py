print("-----------------------------\n" + "----- WHERE'S THE MONEY -----\n" + "-----------------------------")
salary = int(input("What is your annual salary?\n"))
if salary <0:
    print("Must enter positive integer for salary")
    exit()
morgage = int(input("How much is your monthly mortgage or rent?\n"))
if morgage <0:
    print("Must enter positive integer for mortgage or rent")
    exit()
bills = int(input("What do you spend on bills monthly?\n"))
if bills <0:
    print("Must enter positive integer for bills")
    exit()
food = int(input("What are your weekly grocery/food expenses?\n"))
if food <0:
    print("Must enter positive integer for food")
    exit()
travel = int(input("How much do you spend on travel annually?\n"))
if travel <0:
    print("Must enter positive integer for travel")
    exit()
tax = 0.0
if salary <= 15000:
    tax = 10
elif salary <= 75000:
    tax = 20
elif salary <= 200000:
    tax = 25
else:
    tax = 30
left = salary-(morgage*12) - (bills*12) - (food*52) - (travel) - (salary * (tax / 100))
taxed = salary * (tax / 100.00)
if taxed > 75000:
    taxed == 75000.00
count = len("| mortgage/rent | $  " + str(morgage*12) + ".00" + " |  " + str(morgage*12/salary*100) + "% | " + "#" * int(morgage*12/salary*100))
print("-"*count)
print("See the financial breakdown below, based on a salary of $" + str(salary))
print("-"*count)
print("| mortgage/rent | $  " + str(morgage*12) + ".00" + " |  " + str(morgage*12/salary*100) + "% | " + "#" * int(morgage*12/salary*100))
print("|         bills | $   " + str(bills*12) + ".00" + " |   " + str(bills*12/salary*100) + "% | " + "#" * int(bills*12/salary*100))
print("|          food | $  "+str(food*52) + ".00" + " |  " + str(food*52/salary*100) + "% | " + "#" * int(food*52/salary*100))
print("|        travel | $   " + str(travel) + ".00" + " |   " + str(travel/salary*100) + "% | " + "#" * int(travel/salary*100))
print("|           tax | $  " + str(taxed) + "0 |  " + str(tax) +".0% | " + "#" * tax)
print("|         extra | $  " + str(left) +"0 |  " + str(round(left/salary*100,1)) + "% | " + "#" * int(left/salary*100))
print("-"*count)
if (salary * (tax / 100)) >= 75000:
    print(">>> TAX LIMIT REACHED <<<")
if left < 0:
    print(">>> WARNING: DEFICIT <<<")

### 
### Author: Jordan Walker
### Course: CSC 110
### Description: This helps people wee where all their money goes. I and kind of proud of line 38 I thought i was going to do it the way i normally do it but thuis way is so much better.
###              
###