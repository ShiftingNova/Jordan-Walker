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
taxed = salary * (tax / 100.00)
if taxed > 75000:
    taxed = 75000.00
left = salary - (morgage * 12) - (bills * 12) - (food * 52) - travel - taxed
count = 0
Mcount = len("| mortgage/rent | $  " + str(format(morgage*12,'9,.2f')) + " |  " + str(format(morgage*12/salary*100,'4,.1f'))+ "% | " + "#" * int(morgage*12/salary*100))
Bcount = len("|         bills | $  " + str(format(bills*12,'9,.2f')) + " |  " + str(format(bills*12/salary*100,'4,.1f')) + "% | " + "#" * int(bills*12/salary*100))
Fcount = len("|          food | $  "+str(format(food*52,'9,.2f')) + " |  " + str(format(food*52/salary*100,'4,.1f')) + "% | " + "#" * int(food*52/salary*100))
Tcount = len("|        travel | $  " + str(format(travel,'9,.2f')) + " |  " + str(format(travel/salary*100,'4,.1f')) + "% | " + "#" * int(travel/salary*100))
TAXcount = len("|           tax | $  " + str(format(taxed,'9,.2f')) + " |  " + str(format(tax,'4,.1f')) +"% | " + "#" * tax)
Ecount = len("|         extra | $ " + str(format(left,'10,.2f')) +" |  " + str(format(left/salary*100,'4,.1f')) + "% | " + "#" * int(left/salary*100))
if Mcount >= Bcount and Mcount >= Fcount and Mcount >= Tcount and Mcount >= TAXcount and Mcount >= Ecount:
    count = Mcount
if Bcount >= Mcount and Bcount >= Fcount and Bcount >= Tcount and Bcount >= TAXcount and Bcount >= Ecount:
    count = Bcount
if Fcount >= Bcount and Fcount >= Mcount and Fcount >= Tcount and Fcount >= TAXcount and Fcount >= Ecount:
    count = Fcount
if Tcount >= Bcount and Tcount >= Fcount and Tcount >= Mcount and Tcount >= TAXcount and Tcount >= Ecount:
    count = Tcount
if TAXcount >= Bcount and TAXcount >= Fcount and TAXcount >= Tcount and TAXcount >= Mcount and TAXcount >= Ecount:
    count = TAXcount
if Ecount >= Bcount and Ecount >= Fcount and Ecount >= Tcount and Ecount >= TAXcount and Ecount >= Mcount:
    count = Ecount
print("-" * count)
print("See the financial breakdown below, based on a salary of $" + str(salary))
print("-"*count)
print("| mortgage/rent | $  " + str(format(morgage*12,'9,.2f')) + " |  " + str(format(morgage*12/salary*100,'4,.1f'))+ "% | " + "#" * int(morgage*12/salary*100))
print("|         bills | $  " + str(format(bills*12,'9,.2f')) + " |  " + str(format(bills*12/salary*100,'4,.1f')) + "% | " + "#" * int(bills*12/salary*100))
print("|          food | $  "+str(format(food*52,'9,.2f')) + " |  " + str(format(food*52/salary*100,'4,.1f')) + "% | " + "#" * int(food*52/salary*100))
print("|        travel | $  " + str(format(travel,'9,.2f')) + " |  " + str(format(travel/salary*100,'4,.1f')) + "% | " + "#" * int(travel/salary*100))
print("|           tax | $  " + str(format(taxed,'9,.2f')) + " |  " + str(format(taxed/salary*100,'4,.1f')) +"% | " + "#" * int(taxed/salary*100))
print("|         extra | $ " + str(format(left,'10,.2f')) + " |  " + str(format(left/salary*100,'4,.1f')) + "% | " + "#" * int(left/salary*100))
print("-"*count)
if (salary * (tax / 100)) >= 75000:
    print(">>> TAX LIMIT REACHED <<<")
if left < 0:
    print(">>> WARNING: DEFICIT <<<")
### 
### Author: Jordan Walker
### Course: CSC 110
### Description: This helps people wee where all their money goes. 
###              
###
