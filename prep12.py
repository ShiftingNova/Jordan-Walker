#
#Jordan Walker
#CSC110
# this function takes the average of the amount you want
#
def  average_numbers(amount):
    i = 0
    total = 0
    while i < amount:
        temp_number = int(input("Number:\n"))
        total += temp_number
        i+=1
    total = round(total/amount, 2)
    print("Average = ", total)
