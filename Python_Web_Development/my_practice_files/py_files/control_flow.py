# indentation is extremely important in pythonself.
# There are no {} brackets, meaning that code must align when related
if 1<2:
    print('Suck Fish')
# This is a fully functioning IF statement
if 1<2:
    print('You smell')
    if 3<4:
        print('Nasty Boi')
# Nested IF statement, notice the indentation
if 4<3:
    print("thats fucking wrong")
elif 3==3:
    print("Got that elif to run")
else:
    print("You bet your ass it is wrong")
# FOR LOOPS
seq = [1,2,23,3,45]

for item in seq:
    print(item)
for item in seq:
    print('hello') # prints 5 times due to 5 values in the list
# With DICTIONARIES (THESE FUCKERS PRINT RANDOMLY EVERYTIME)
d = {"Sam":1,"kinkade":2,"John":3}
for item in d:
    print(item)
for k in d:
    print(k)
    print(d[k])
# TUPLE UNPACKING
mypairs =[(2,3),(4,5),(6,7)]
for item in mypairs:
    print(item)
# prints out each value in the tuple as requested
for tup1,tup2 in mypairs:
    print(tup1)
    print(tup2)
# WHILE LOOPS
i = 1
while i<5:
    print("i is {}".format(i))
    i = i+1
# RANGE
# 0 is beginning range, 5 is ending range
f=list(range(0,5))
print(f)
# 0 is begging range, 20 is ending range, 2 is the step-count
z = list(range(0,20,2))
print(z)

for item in range(10):
    print(item)
# LIST COMPREHENSION
x=[1,2,3,4]
out=[]
for num in x:
    out.append(num**2)
print(out)

thing=[num**2 for num in x] # does the same thing as above
print(thing)
