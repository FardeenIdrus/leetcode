def leq(A,B):
    n = max(len(A), len(B))
    # walk from the most significant trit down; missing trits counts as 0
    
    for i in range(n-1, -1, -1):
        a = A[i] if i< len(A) else 0
        b = B[i] if i < len(B) else 0
        
    # first difference decides the whole comparison
        if a!= b:
            return a < b
    
    return True

print(leq([2,0,1], [0,1,1]))
print(leq([2,0,1,0], [2,0,1]))
print(leq([0,1,1], [2,0,1]))
        