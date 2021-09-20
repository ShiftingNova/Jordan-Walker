word = str(input("Enter string:\n"))
words = list(word)
open = 0
closed = 0
i = 0
while i <= len(word)-1:
    if words[i] == "(":
        open = open + 1
    elif words[i] == ")":
        closed = closed + 1
    i= i + 1
        #does i++ not exist in python or something. Pycharm says its not a thing
if open == closed:
    print("Parentheses balanced")
else:
    print("Parentheses unbalanced")
