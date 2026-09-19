import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
y = re.search(r"\bS\w+",txt)

print(x) # Returns a match object
print(y.span()) # Returns the start and end index 
print(y.group()) # Returns the actual string
print(y.string) # Returns the full original string that was searched

# When re.search() finds nothing, it returns None instead of a Match Object. 
# .group() is a method that only exists on a Match Object - it doesn't exist on NOne. So if you dont 
# check first, and you call .group() on a search that found nothing, your program crashes.
z = re.search(r"Portugal", "The rain in Spain")
if z: 
    print(z.group())
else:
    print("no match found")


# re.match() only checks the very beginning of the entire string - not each word.
# match() checks only character position 0 of the whole string

txt_2 = "rain in spain"
# Returns None
print(re.match(r"Spain", txt_2)) 
print(re.match(r"rain", txt_2))
print(re.match(r"in", txt_2))
print('test', re.findall(r"\br", txt_2))

# Matches the position at the start of a word, with nothing consumed.
print(re.search(r"\bain", "rain again"))

t = re.search(r"\br\w*", txt_2)
print(t.group())


# Makes the whole match ignore uppercase versus lowercase

print(re.findall("cat", "Cat, CAT, CAt", re.I))


# Greedy (*, +) grabs as much text as it can
# Lazy - adding "?" grabs as little as possible

print(re.findall(r"<.*>", "<a><b>"))
print(re.findall(r"<.*?>", "<a><b>"))

# Matches one or more letters, digits, or underscores in a row. "+" groups them together
test = "abc 123 abc123"
k = re.findall(r"\w+", test)
print(k)

# Without "+", each character is printed as a separate list element
j = re.findall(r"\w", test)
print(j)

tester = "#hello ##hello"
u = re.findall(r"#\w+", tester)
print(u)

txt = "The rain in Spain"
x = re.search(r"Spain",txt)
print(x.span())