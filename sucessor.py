
def sucessor(trits):
    
    # copy so the input isn't mutated
    result = list(trits)
    i = 0
    # carry: every trailing 2 becomes 0 and pushes the carry left
    
    while i < len(result) and result[i] == 2:
        result[i] = 0
        i+=1
    if i== len(result):
        # all trits were 2 or the list was empty
        result.append(1)
    # new most-significant trit
    else:
        result[i] +=1
    
    return result

print(sucessor([2,0,1]))
print(sucessor([2,1,0]))
        

    
    