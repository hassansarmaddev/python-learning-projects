# nested1 = [['a', 'b', 'c'],['d','e'],['f','g','h']]
# nested1[0].append('z')
# print(nested1)
# nested1[1].append('x')
# print(nested1)
# print(len(nested1))
# for i in nested1:
#     print(i)
    
# y = nested1[1]
# print(y)
# print(y[0])
# print([10,20,30][1])
# print(nested1[1][0])



# nested1 = [['a', 'b', 'c'],['d','e'],['f','g','h']]
# nested1[1] = [1,2,3,]
# print(nested1)
# nested1[1][0] = 100
# print(nested1)


# animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]
# print(animals[1][0])


'''✅ Use the right methods for each: append() for lists, update()/keys()/values()/items() for dicts.
'''

# animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]
# print(animals[1][0])
# animals[1][0]='unicorn'
# print(animals)

# y = animals[0].append('auni')
# print(animals)        
# print(y)

'''✅ More pratice examples with nested lists.'''


animals = [['cat', 'dog'], ['horse', 'cow'], ['lion', 'tiger']]
print(animals[0])
print(animals[1])
animals[2][0]='panther'
print(animals)
animals[0].append('mouse')
print(animals)
animals[0].insert(0, 'elephant')
print(animals)

for i in animals:
    for a in i:
        print(a)                
        
        
        
        
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'],['Kristen', 'Wiig', 1973]]
last_names = []

for entertainer in info:
    last_names.append(entertainer[1])
    print(last_names)
                          

info = [['Tina', 'Turner', 'hassan', 'singer'], ['Matt', 'Damon', 'zain', 'actor'],['Kristen', 'Wiig', 'nugh']]
t_strings = []

for lst in info:
    #print(lst)
    for word in lst:
        if 't' in word:
            t_strings.append(word)
print(t_strings)            
        #print(word)                                                      
        
        

'''2. Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains every person’s last name, and save that list as last_names.
'''

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = []
for lst in info:
    print(lst[1])
    last_names.append(lst[1])
print(last_names)    


'''3. Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.
'''

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings=[]
for lst in L:
    for wrd in lst:
        if 'b' in wrd:
            b_strings.append(wrd)
print(b_strings) 