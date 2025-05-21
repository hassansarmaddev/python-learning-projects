
############Below is a simple example of a while loop that counts from 1 to sum
# def sumTo(aBound):
#     """ Return the sum of 1+2+3...n """
    
#     theSum = 0
#     aNumber = 1
#     while aNumber <= aBound:
#         theSum = theSum + aNumber
#         aNumber = aNumber + 1
#     return theSum
    
# print(sumTo(4))
# print(sumTo(1000))


############ Below program that counts down from a given number to 1

# def countdown(n):
#     while n > 0:
#         print(n)
#         n -= 1 # Decreasing n each time
#     print("Blastoff!")
    
# print(countdown(5))

# #Sum of even numbers
# def sum_even_numbers(n):
#     theSum = 0
#     num = 2
#     while num <= n:
#         theSum = theSum + num
#         num = num + 2
#     return theSum
# print(sum_even_numbers(10))


############# Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.

# list1 = [8, 3, 4, 5, 6, 7, 9]

# tot = 0
# for elem in list1:
#     tot = tot + elem


# idx = 0
# accum = 0
# while idx < len(list1):
#     accum = accum + list1[idx]
#     idx = idx + 1
# print(accum)    




############ Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.

# count = 0
# eve_nums = []
# while count <= 15:
#     if count % 2 == 0:
#         eve_nums.append(count)
#     count = count + 1
    
# print(eve_nums)   


# def checkout():
#     total = 0
#     count = 0
#     moreItems = True
#     while moreItems:
#         price = float(input('Enter price of item (0 when done): '))
#         if price != 0:
#             count = count + 1
#             total = total + price
#             print('Subtotal: $', total)
#         else:
#             moreItems = False
#     average = total / count 
#     print('Total items:', count)
#     print('Total $', total)
#     print('Average price per item: $', average)
    
# checkout()

