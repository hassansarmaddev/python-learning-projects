#sort can be done on list, sorted can be done on strings, lists, tuples, etc.

# L1 = [5, 2, 9, 1, 5, 6]
# L2 = ["Cherry", "Apple", "Blueberry", "Banana"]

# L1.sort()
# print(L1)
# L2.sort()
# print(L2)



# L1 = ["Cherry", "Apple", "Blueberry", "Banana"]
# L2 = [5, 2, 9, 1, 5, 6]
# # L3 = sorted(L1)
# # L4 = sorted(L2)
# # print(sorted(L1))
# # print(L3)
# # print(L4)
# L3 = L2.sort()


# numbers = [5, 2, 9, 1, 5, 6]
# numbers.sort()
# print("Sorted numbers:", numbers)

#####################################################################################


# L2 = ["Cherry", "Apple", "Blueberry"]

# L3 = sorted(L2)
# print(L3)
# print(sorted(L2))
# print(L2) # unchanged

# print("----")

# L2.sort()
# print(L2)
# print(L2.sort())  #return value is None






#####################################################################################




L1 = [1, 7, 3, 9, 2]


def absolute(x):
    if x >=0:
        return x
    else:
        return -x
print(absolute(-5))
print(absolute(-119))


for y in L1:
    print(absolute(y))
    
    
    
    
#pass the absolute function to sorted in order to specify that we want the items sorted in order of their absolute value, 
# rather than in order of their actual value.


L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))


'''1. You will be sorting the following list by each element’s second letter, a to z. 
Create a function to use when sorting, called second_let. 
It will take a string as input and return the second letter of that string. 
Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
'''

# ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

# def second_let(s):
#     return s[1]

# sorted_by_second_let = sorted(ex_lst, key=second_let)
# print(sorted_by_second_let)

'''2. Below, we have provided a list of strings called nums. 
Write a function called last_char that takes a string as input, and returns only its last character. 
Use this function to sort the list nums by the last digit of each number, 
from highest to lowest, and save this as a new list called nums_sorted.'''



# nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

# def last_char(s):
#     return s[-1]

# nums_sorted = sorted(nums, key=last_char, reverse=True)

# # print(nums_sorted)
    
'''3. Below, we have provided a list of strings called nums.'''

L = ['E', 'A', 'C', 'B', 'D']

d = {}
for x in L:
    if x in d:
        d[x] += 1
    else:
        
        



