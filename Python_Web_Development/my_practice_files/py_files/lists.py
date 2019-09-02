# Pythons array
# LISTS
my_list=[1,2,2,3,3,3]
my_2list=[3.4,4.5,4.6]
my_3list=['String',3,True,[1,2,3]] #string,numeral,boolean,nested array
print(my_list)
print(my_2list)
print(my_3list)
print(len(my_3list))
another_list=["a","b","c"]
print(another_list[2])
another_list[1]="FUCK YOU" # LISTS ARE MUTABLE
print(another_list)
another_list.append("APPENDED ITEM")
print(another_list)
bitch_list=[1,2,2,2]
another_list.append(bitch_list)
print(another_list)
another_list.extend(bitch_list) # adds 'bitch_list' as new values, not as a list
print(another_list)
item = another_list.pop() # 'popped' the last list item out of the list
# you can also specify the pop -> another_list.pop(3)
print(another_list)
print(item)
another_list.reverse()
print(another_list)
num_list = [1,2323,63465,5332,333]
num_list.sort() # sorts from high to low
print(num_list)
nested_list = [1,2,[3,4]]
print(nested_list[2])
print(nested_list[2][1]) #specifies the position in the second list

# MATRIX
matrix=[[1,2,3],[4,5,6],[7,8,9]]
# List Comprehension
first_col = [row[0] for row in matrix]
print(first_col)

# DICTIONARIES
my_stuff={"Key1":"Value","Key2":"Value2","Key3":{'123':[1,2,"Grab Me"]}}
print(my_stuff["Key1"])
print(my_stuff["Key3"]['123'][2])
my_stuff2 ={'lunch':'eggs',"dinner":'pussy'}
print(my_stuff2['lunch'])
my_stuff2['lunch'] = 'TURKEY BOY'
print(my_stuff2['lunch'])
my_stuff2['breakfast'] = 'bacon'
print(my_stuff2)

# TUPLES - Immutable sequences
# Booleans
# True - 1
# False - 0
#TUPLES
t=(1,2,3)
print(t[1])

# Sets - unnoredered set of unique elements
p = set()
p.add(1)
p.add(2)
p.add(2) # not added 
print(p)
