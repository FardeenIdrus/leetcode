def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(2)
print(mydoubler(1))
mytripler = myfunc(3)
print(mytripler(1))

numbers = [1,2,3,4]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)

oddnumbers = [1,2,3,4,5,6,7,8,9]
odd = list(map(lambda x: x%2 !=0, oddnumbers))
print(odd)

students = [("emily", 25), ('Tobias', 22), ("Linus", 28)]
sorted_students = sorted(students, key = lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key = lambda x: len(x))
print(sorted(words ))