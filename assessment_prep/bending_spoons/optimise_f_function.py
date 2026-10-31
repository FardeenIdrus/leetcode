def f_eff(A,B):

    n = max(len(A), len(B))
    
    # Read a trit, treating anything past the end
    # of a list as 0.
    def trit(L, i):
        return L[i] if i< len(L) else 0

# Scan from the most significant trit down and find
# the first position where A and B disagree
    
    j = -1
    for i in range(n-1, -1, -1):
        if trit(A,i) != trit(B,i):
            j = i
            break
    
    if j == -1:
        return list(A)
    
    # Above position j, A and B are identical, 
    # every number in the
    # range hast hose same trits and the minimum keeps them
    res = [0] *n 
    
    for i in range(j+1, n):
        res[i] = trit(A,i)
    # At position j the trit only ever runs from A's value up to B's
    # so thesmallest it reaches is A's values.    
    
    res[j] = trit(A,j)
    
    # Below the position j everything is 0: the range contains the number made
    # of the shared top trits, A's trits at j plus one, and zero underneath,
    # which is still within [a,b] and drags every lower trit down to 0
    
    return res

# Test cases
# example from the question
assert f_eff([2,0,1], [1,1,1]) == [0,0,1]
assert f_eff([2,0,1], [2,0,1]) == [2,0,1]
# a==b, single number
assert f_eff([1,1],[2,1]) == [1,1]

assert f_eff([], [2]) == [0]

assert f_eff([1], [1,0,1]) == [0,0,0]
print("test pass")
        
    
    