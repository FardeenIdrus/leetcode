
def tritwise_min(A, B):
        
    # Beyond the shorter list one operand is implicitly 0, so the min there is
    # 0
    # Trailing zeros are not important, so stop at the shorter length

    return [min(a,b) for a,b in zip(A,B)]

print(tritwise_min([1,0,2], [1,1,1]))
print(tritwise_min([2,1],[0,2,1]))