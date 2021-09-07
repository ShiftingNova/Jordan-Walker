size = input("Drink Size:\n")
type = input("Drink type:\n")
s2=0
t2 = 0
if size.lower() =="large":
    s2 = 2
else:
    s2 = 1
if type.lower() == "regular":
    t2 = 3
print("\n" +str(50*t2*s2)+" calories")
