# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
# d = {}
# for x in L:
#     if x in d:
#         print(d[x])
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
# for x in d.keys():
#     print("{}: {}".format(x, d[x]))

# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

# d = {}
# for x in L:
#     if x in d:
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
# print(d.keys())
# y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
# print(y)
# for k in y:
#     print("{} appears {} times".format(k, d[k]))




# fruits = ['peach', 'kiwia', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
# new_order = sorted(fruits)
# print(new_order)  # Print sorted list
# new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
# print(new_order)
# # new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
# # for fruit in new_order:
# #     print(fruit)



# states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
#           "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
#           "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

# print("--- Breaking down the lambda key ---")
# for state_key in states:
#     print(f"Processing Key: '{state_key}'")

#     # 1. Get the value (the list of cities)
#     value_list = states[state_key]
#     print(f"  1. states['{state_key}'] is: {value_list}")

#     # 2. Get the first city from that list
#     first_city = value_list[0]
#     print(f"  2. The first city (at index 0) is: '{first_city}'")

#     # 3. Get the length of that first city's name
#     length_of_first_city = len(first_city)
#     print(f"  3. The length of '{first_city}' is: {length_of_first_city}")
#     print("-" * 20) # Separator for clarity



# stock = [("phone", "$410.50", 20), ("mug", "$10.99", 100), ("headphone", "$199.99", 5)]
# print(sorted(stock, key=lambda item: item[1]))  # Sort by price


animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)
print(animals_sorted)