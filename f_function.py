from tritwise_min import tritwise_min
from sucessor import sucessor 
from leq_bending_spoons import leq

def f(A,B):
# The running minimum starts at A, since a is included
# in the range
    acc = list(A)
    
#curr walks through every integer from a up to b
    cur = list(A)
# cur never goes past b, so "b<= cur" is only true
# once cur has reached b.
# Using leq rather than == avoids trailing zero issues
    while not leq(B, cur):
        # next integer in the  range
        cur = sucessor(cur)
        # fold it into the running minimum 
        acc = tritwise_min(acc, cur)
    
    return acc
print(f([2,0,1],[1,1,1]) == [0,0,1])