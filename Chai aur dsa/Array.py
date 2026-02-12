# import array as arr

# val = arr.array('i',[1,2,3,4,5,6])


from array import *
# val = array('i',[1, 2, 3, 4, 5, 6])

# # print(val)

# for i in range(0, len(val)):
#     print(val[i], end=" ")

# print("\n")

# for x in val:
#     print(x, end=",")


# print("\n")

# print(val.typecode)

# reverse an array
# val.reverse()
# for i in range(0, len(val)):
#     print(val[i], end=" ")




# insert element at a specific index
# val.insert(2, 13) 

# # insert element at last
# val.append(25)

# # change element at specific index
# val[1] = 32

# for i in range(0, len(val)):
#     print(val[i], end=" ")





# this is hard copy
# copyArray1 = array(val.typecode, (x for x in val))
# for i in range(0, len(copyArray1)):
#     print(copyArray1[i], end=" ")

# print("\n")

# # this is just memory reference
# copyArray2 = val

# for i in range(0, len(copyArray2)):
#     print(copyArray2[i], end=" ")

# print("\n")

# val.insert(0,25)
# for i in range(0, len(copyArray2)):
#     print(copyArray2[i], end=" ")




# Both are correct, but the best choice is passing the array directly.

# ✅ Generator Expression
# copyArray1 = array(val.typecode, (x for x in val))
# - Uses less memory
# - Produces elements one by one
# - Good for very large data

# ❌ List Comprehension
# copyArray1 = array(val.typecode, [x for x in val])
# - Creates a temporary list first
# - Uses extra memory
# - Unnecessary step when just copying

# 🔥 Best and Cleanest Way
# copyArray1 = array(val.typecode, val)
# - No generator
# - No temporary list
# - Faster and more Pythonic

# 🧠 Quick Rule:
# Need transformation? → Use list comprehension
# Just copying? → Pass the iterable directly


# # deleting element from array

# print("\nBefore deletion")
# for x in copyArray1:
#     print(x, end=" ")

# # delete by index , here 2 is the index
# # copyArray1.pop(2) 

# # index na dile eta stack er moto kaj korbe last element ta delete korbe
# # copyArray1.pop() 

# # delte by value, 5 is the value 
# copyArray1.remove(5)

# print("\nAfter deletion")
# for x in copyArray1:
#     print(x, end=" ")

# sliced_array = copyArray1[start_indx : end_index]
# start_index kichu na dile 0 hoy ar end_index kuchu na dile last index hoy

# print("\n")

# for x in copyArray1:
#     print(x, end=" ")

# print("\n")

# # sliced_array = copyArray1[3 : 6] # start index theke end index er age obdi
# # sliced_array = copyArray1[2 : -3] # end theke last 3 te element ke baad diye debe

# sliced_array = copyArray1[::1] # normal order
# sliced_array = copyArray1[::-1] # reversed order

# for x in sliced_array:
#     print(x, end=" ")

# # Slicing with negative step

# sliced_array = copyArray1[3:6:-1]

# Syntax → array[start : stop : step]

# Here:
# start = 3
# stop = 6
# step = -1 (move backwards)

# ⚠️ Important Rule:
# When step is NEGATIVE,
# start should be GREATER than stop.
# Because we are moving from right → left.

# In this case:
# 3 < 6  ❌
# So Python cannot move backwards from index 3 to 6.

# 👉 Result will be an EMPTY array.

# print(sliced_array)   # array('i')

# # ✅ Correct Reverse Example:
# sliced_array = copyArray1[6:3:-1]
# Starts at index 6 → goes back until just before index 3


# take user input
# arr = array('i', [])

# n = int(input("Enter a n: "))

# for i in range(0, n):
#     arr.append(int(input("Enter array element: ")))

# for x in arr:
#     print(x, end=" ")

arr = array('i',[2,4,5])
print(arr.index(4)) # find index of an element