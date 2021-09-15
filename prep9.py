name = input("Enter factorial to calculate:\n")
sum = 1
if name.isnumeric():
    name = int(name)
    for i in range(1, name + 1):
        sum = i * sum
    print("")
    print(str(name)+" factorial = "+str(sum))
    # Jordan Walker
    # CSC 110
    # thsi was quick i dont know why i named the variavle "name" brain was tired i guess
