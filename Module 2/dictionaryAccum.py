#un-ordered collection of items
# medals = {"gold": 33, "silver": 17, "bronze": 12}
# print(medals)

# inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
# del inventory["apples"]  # remove bananas from the inventory
# print(inventory)
# inventory["pears"] = 200  # update the number of pears in the inventory
# print(inventory)
# inventory["bananas"] = inventory["bananas"] + 50  # add 50 bananas to the inventory
# print(inventory)
# numItems = len(inventory)




# mydic = {"cat": 12, "dog": 6, "elephant": 3, "tiger": 5}
# mydic["mouse"] = mydic["cat"] + mydic["dog"]  # add mouse to the dictionary with value of cat + dog
# print(mydic["mouse"])


################ updating value ###############

# swimmers = {"Manuel": 12, "Sophie": 10, "Liam": 8, "Emma": 15, "phelps": 20}
# swimmers["phelps"] = swimmers["phelps"] + 5  # update phelps' score by adding 5
# print(swimmers["phelps"])  # print the updated score of phelps


########### Dictionary methods ###############

#associate values with every key

# inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
# #print(inventory['oranges'])
# for key in inventory.keys(): # iterate through the keys in the dictionary, but it will not return the list
#     print(key, "has the value", inventory[key])  # prints all the keys in the dictionary
# keys = list(inventory.keys())  # get a list of all the keys in the dictionary
# print(keys)  # print the list of keys    



#associate values with every key, get values

# inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
# print(list(inventory.values()))  # get a list of all the values in the dictionary
# print(list(inventory.items()))  # get a list of all the key-value pairs in the dictionary

# for k in inventory:
#     print("Got", k, "that maps to", inventory[k])  # iterate through the keys in the dictionary and print the key-value pairs  
    




# inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
# if 'bananas' in inventory:  # check if 'bananas' is a key in the dictionary
#     print(inventory['bananas'])  # print the value associated with the key 'bananas'
# else:   
#     print("No bananas found")
    
    

# get method


# inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}    
# print(inventory.get('bananas'))  # get the value associated with the key 'bananas'
# print(inventory.get('grapes'))  # get the value associated with the key 'grapes', the output will be as none
# print(inventory['grapes'])  # this will raise a KeyError because 'grapes' is not a key in the dictionary
# #this is the difference between .get and indexing.
# print(inventory.get('grapes', 0))  # get the value associated with the key 'grapes', if it doesn't exist, return 0 instead of raising an error


# total = 0
# mydict = {"cat": 12, "dog": 6, "elephant": 3, "tiger": 5}
# for akey in mydict:  # iterate through the keys in the dictionary
#     if len(akey) > 3:
#         total = total + mydict[akey]  # add the value associated with the key to the total if the length of the key is greater than 3
# print(total)  # print the total value of all the keys with length greater than 3
 