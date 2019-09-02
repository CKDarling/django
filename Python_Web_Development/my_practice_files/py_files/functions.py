def my_fucktion(param1='default'):
    """
    THIS IS THE DOC STRING
    """


    print("My first Pyton Function")

my_fucktion()
# using a return to assign a variable
def another_one(param1='default'):
    """
    THIS IS THE DOC STRING
    """


    return "My first Pyton Function"

result = another_one()
print(result)
# creating spooky functions

def add_num(num1,num2):
    return num1 + num2
num_sum = add_num(40,7)
string_sum=add_num("You're"," a bitch")
print(num_sum)
print(string_sum)
print(type(num_sum))# returns the variable data type
# Testing if the data types are correct for the function
def valueTest(num1,num2):
    if type(num1)==type(num2)==type(10): # ==type(10) is the data type to find
        return num1+num2
    else:
        return 'sorry, need integers'
result = valueTest('3',3)
print(result)

# filter
mylist = [1,2,3,4,5,6,7,8,10]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,mylist)
print(evens)


#lambda expression - meant to be a single run function
evens2 = filter(lambda number:number%2 == 0,mylist)
print(evens2)
