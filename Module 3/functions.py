#################### Returning Values ####################
# def square(x):
#     y = x * x
#     return y
# toSquare = 10
# result = square(toSquare)  # call the function and pass the value to it
# print("The square of", toSquare, "is", result)  # print the result of the function call


#################### ex of return statement ####################

# def loger_than_five(list_of_names):
#     for name in list_of_names:
#         if len(name) > 5:
#             return True
        
#         return False  # return False if no name is longer than 5 characters
# list1 = ["John", "Samantha", "Michael", "Sarah"]
# list2 = ["John", "Sam", "Mike", "Sarah"]

# print(loger_than_five(list1))  # True, because "Samantha" and "Michael" are longer than 5 characters

# print(loger_than_five(list2))  # False, because no name is longer than 5 characters    

# def square(x):
#     print("square")
#     return x*x

# def g(y):
#     print("g")
#     return y + 3

# print(square(g(2)))

# def mult(x):
#     return x + 10
    
# def addit(y):
#     result_with_mult = y * mult(y)
#     return result_with_mult

# print(mult(5))
# print(addit(4))

#################### test-cases-for-functions ####################
#assert checks if its true or false, if false it will raise an error

# def square(x):
#     return x * x

# assert square(0) == 0, "Test case 3 failed"
# assert square(2) == 4, "Test case 1 failed"
# assert square(3) == 9, "Test case 2 failed"

# assert square(-2) == 5, "Test case 4 failed"
# assert square(1.5) == 2.25, "Test case 5 failed"

# def update_counts(letters, counts_d):
#     for c in letters:
#         counts_d[c] = 1
#         if c in counts_d:
            


# counts = {"a": 3, "b": 2, "c": 1}


#################### return value tests ####################

# def add(a,b):
#     return a + b
# print(add(5,3))  # returns 8

# def test_add():
#     assert add(5,3) == 8, "Test case 1 failed"
#     assert add(-1,1) == 0, "Test case 2 failed"
#     assert add(0,0) == 0, "Test case 3 failed"
#     assert add(2.5,3.5) == 6.0, "Test case 4 failed"
#     assert add(-2,-3) == -5, "Test case 5 failed"

# print(test_add())  # run the test cases for the add function

# def add(a):
#     return a + 2
# a = 5
# print(add(a))

#################### tuple packing ####################

# def circleInfo(r):
#     """ Returns the area and circumference of a circle given its radius """
#     c = 2 * 3.14 * r  # circumference
#     a = 3.14 * r * r  # area
#     return(c, a)  # return both values as a tuple

# print(circleInfo(5))  # call the function and print the result




#4. Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.

# lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
# t_check = [lst_tups[0][2], lst_tups[1][2], lst_tups[2][2], lst_tups[3][2], lst_tups[4][2], lst_tups[5][2]]


# 5. Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.

# tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
# seconds = []
# for tp in tups:
#     seconds.append(tp[1])
    
# print(seconds)    

