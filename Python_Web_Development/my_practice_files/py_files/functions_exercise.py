x = [1,2,3,4,5,6]
# Exercise 1
def arrayCheck(nums):
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False
y=arrayCheck(x)
print(y)
# Exercise 2
def stringBits(str):
  result = ""
