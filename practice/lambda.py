
def myfunc(n):
    return lambda a: a**n

myquadripler = myfunc(4)
print(myquadripler(11))

numbers = [1,2,3,4,5]
doubled = list(map(lambda x: x*2, numbers))

print(doubled)

odd_numbers = list(filter(lambda x: x%2!= 0, numbers))

print(odd_numbers)

string = ["zac"]

print(sorted(string))