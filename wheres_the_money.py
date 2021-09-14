print("-----------------------------\n" + "----- WHERE'S THE MONEY -----\n" + "-----------------------------")
salary = int(input("What is your annual salary?\n"))
if salary <0:
    print("Must enter positive integer for salary.")
    exit()
morgage = int(input("How much is your monthly mortgage or rent?\n"))
if morgage <0:
    print("Must enter positive integer for mortgage or rent.")
    exit()
bills = int(input("What do you spend on bills monthly?\n"))
if bills <0:
    print("Must enter positive integer for bills.")
    exit()
food = int(input("What are your weekly grocery/food expenses?\n"))
if food <0:
    print("Must enter positive integer for food.")
    exit()
travel = int(input("How much do you spend on travel annually?\n\n"))
if travel <0:
    print("Must enter positive integer for travel.")
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
count = len("| mortgage/rent | $  " + str(format(morgage*12,'9,.2f')) + " |  " + str(round(morgage*12/salary*100,1) )+ "% | " + "#" * int(morgage*12/salary*100))
print("-"*count)
print("See the financial breakdown below, based on a salary of $" + str(salary))
print("-"*count)
print("| mortgage/rent | $  " + str(format(morgage*12,'9,.2f')) + " |  " + str(round(morgage*12/salary*100,1) )+ "% | " + "#" * int(morgage*12/salary*100))
print("|         bills | $  " + str(format(bills*12,'9,.2f')) + " |   " + str(round(bills*12/salary*100,1)) + "% | " + "#" * int(bills*12/salary*100))
print("|          food | $  "+str(format(food*52,'9,.2f')) + " |  " + str(round(food*52/salary*100,1)) + "% | " + "#" * int(food*52/salary*100))
print("|        travel | $  " + str(format(travel,'9,.2f')) + " |   " + str(round(travel/salary*100,1)) + "% | " + "#" * int(travel/salary*100))
print("|           tax | $  " + str(format(taxed,'9,.2f')) + " |  " + str(round(tax,2)) +".0% | " + "#" * tax)
print("|         extra | $  " + str(format(left,'9,.2f')) +" |  " + str(round(left/salary*100,1)) + "% | " + "#" * int(left/salary*100))
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
