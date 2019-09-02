# Strings

'hello'
"hello"
"You're a bitch" # using both quotation types

# indexing
my_string ='abcdefg'
print(my_string[2])
# SLICING
# Beginning
print(my_string[2:])
print(my_string[:3]) # loads up to but not including index 3
print(my_string[2:5])
#Step Size
print(my_string[::2]) # Grabs every other letter
# Strings are immutable. You cannot redifine a string using an array alteration
# METHODS
# Upper
x = my_string.upper()
print(x)
# Lower
y=my_string.lower()
print(y)
w=my_string.capitalize()
print(w)
my_string2="suck Ass"
s=my_string2.split()
print(s)
s2=my_string2.split('u') # splits on e and removes it
print(s2)
s3=my_string2.split('s') # multi-split bitch
print(s3)
# Print Formatting
f = "Insert this lil bitch: {}".format("SUCK ME OFF")
print(f)
t="Insert one: {} Insert Two: {}".format("BIG","AsS")
print(t)
d="Insert one: {U} Insert Two: {R}".format(R="BIG",U="AsS")
print(d)
