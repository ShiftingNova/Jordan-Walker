hertz = float(input("Enter CPU gigahertz:\n"))
core = float(input("Enter CPU core count:\n\n"))
if core>=20:
    print("That is a high-performance CPU.")
else:
    if hertz >= 3.2 and core >= 8:
        print("That is a high-performance CPU.")
    elif hertz >= 2.5 and core >= 6:
        print("That is a medium-performance CPU.")
    elif hertz >=2 and core >= 2:
        print("That is a low-performance CPU.")
    else:
        print("That CPU could use an upgrade.")
