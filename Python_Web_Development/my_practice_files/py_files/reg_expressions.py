# try:
    # f.open('SoMeShIt.txt','w') # 'r' is for read 'w' is for write
    # f.write("You smell of balls")
# except: # you can add an error type here but it can also be blank and execute if any error occurs
    # print("You suck and your error does too.")\
# instead of finally you can also have else:, which operates the same as usual
# finally: # work all of the time no matter what happens to the try statement
    # print("I work all the time bitch")
    # f.close()
import re

patterns =['term1','term2']

text = 'This is a string with term1, not not the other!'

for pattern in patterns:
    print("I'm searching for: "+pattern)
    if re.search(pattern,text):
        print("Match")
    else:
        print("No Match")
