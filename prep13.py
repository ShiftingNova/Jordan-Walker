def count_characters(sequence, letter_A, letter_B):
    i = 0
    count = 0
    while i<len(sequence):
        if(sequence[i]) == letter_A or sequence[i] == letter_B:
            count+=1
        i+=1
    print("'" + letter_A+"'"+" and '"+letter_B+"' appeared "+str(count)+ " times in the string" +sequence)
