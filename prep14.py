def calculate_tree_height(height, year):
    total = height
    i=0
    while i<year:
        total = total * 1.2
        i+=1

    print(round(total,4))
