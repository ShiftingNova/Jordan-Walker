side = int(input("USS Arizona outer width:\n"))
inner = int(input("USS Arizona inner width:\n"))
height = int(input("USS Arizona tower height:\n"))
print(("                     "+ " " * side +"|" + " " * (inner*2) + "|\n")*int(((side+inner)/7))+("              " + " " * side + "    |##$" + " " * (inner*2) + "$##|" + ("\n                 " + " "*side + "   ##" + " " * (inner*2) + "##") * height))
print("               " + " " * side +  "   #..#" + " " * (inner*2) + "#..#")
print("           "+ " " * side + "\----. #..#" + "." * (inner*2) + "#..# .----/")
print("     " +" "* side + "\ ***|_|    |#..#"+ "-#" * (inner) + "#..#|    |_|*** /")
print(".____" + "_" * side + "_|____          _" + "." * (inner*2) + "_          ____|_"+"_" * side + "..")
print("`---." + "     "+" "*(side*2) + "        " + " "*(inner*2) + "                      --\.")
print("<<#\___________________________" + "_" * (side*2) + "_____"+"_" * (inner*2) + "________\ ")

#Jordan Walker CSC110 2021
