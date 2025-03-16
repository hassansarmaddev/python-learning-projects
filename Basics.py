# x = 5
# y = 7

# def square(n):
#     return n * n
# def add(a,b):
#     return a + b

# z = add(square(y),square(x))
# print(z)

#############2.13. Updating Variables#############

# x = 6
# print(x)
# x += 3
# print(x)
# x -= 1
# print(x)


#############Our First Turtle Program#############


# import turtle
# import tkinter
# a = turtle.Screen()
# b = turtle.Turtle()
# b.forward(500)
# b.left(100)
# b.forward(120)
# b.left(90)

# turtle.done()


# import turtle
# import tkinter
# window = turtle.Screen()
# hassan = turtle.Turtle()

# def repeat_movement():
#     hassan.right(45)
#     hassan.forward(75)
#     hassan.left(90)
#     hassan.forward(150)
#     window.ontimer(repeat_movement, 1000)
    
# repeat_movement()
# turtle.done()

# import turtle
# import tkinter
# user_input_bg = input("Enter desired backgroupd color: ")
# wn = turtle.Screen()             # Set up the window and its attributes
# wn.bgcolor(user_input_bg)        # set the window background color

# user_input_tessColor = input("Enter desired tess color: ")
# tess = turtle.Turtle()
# tess.color(user_input_tessColor)

# user_input_tessSize =   int(input("Enter desired tess size: ")) 
# tess.pensize(3)                 # set the width of her pen

# tess.forward(50)
# tess.left(120)
# tess.forward(50)

# wn.exitonclick()                # wait for a user click on the canvas


# import turtle
# import tkinter
# wn = turtle.Screen()
# tess = turtle.Turtle()

# wn.bgcolor("lightgreen")        # set the window background color
# tess.color("blue")              # make tess blue

# tess.pensize(5)


# import turtle
# import tkinter
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# elan = turtle.Turtle()
# distance = 50
# for _ in range(10):
#     elan.forward(distance)
#     elan.right(90)
#     distance = distance + 10
# wn.exitonclick()

# import turtle
# import tkinter
# print(turtle.getshapes())
# alex = turtle.Turtle()
# wn = turtle.screen()
# alex.shape("turtle")
# alex.penup()
# for size in range(10):
#     alex.forward(50)
#     alex.stamp()
#     alex.forward(-50)
#     alex.right(36)
    
# wn.exitonclick()

# for a in range(100):
#     print("We like Python's turtles!")


# import turtle
# import tkinter
# wn = turtle.screen()
# a = turtle.Turtle()

# for x in range(5):
#     a.forward(50)
#     a.right(72)

    
# wn.exitonclick()

# import random as mixer

# for _ in range(10):
#     print(mixer.randint(1, 10))


# num1 = input ('Enter first number: ')
# num2 = input ('Enter second number: ')

# sum = num1 + num2

# print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))                # The sum of 1 and 2 is 12                      cd ~/Download

# for _ in range(100):
#     print("We like Python's turtles!")



# Equilateral Triangle	3	120°
# Square	4	90°
# Pentagon	5	72°
# Hexagon	6	60°
# Heptagon (7 sides)	7	~51.43°
# Octagon	8	45°
# Nonagon (9 sides)	9	~40°
# Decagon (10 sides)	10	36°



# Draw quilateral triangle

# import turtle
# import tkinter
# wn = turtle.Screen()
# eqtri = turtle.Turtle()
# sq = turtle.Turtle()
# hexa = turtle.Turtle()
# octa = turtle.Turtle()
# for _ in range (8):
#     eqtri.left(120)    
#     eqtri.forward(100)
#     sq.left(90)
#     sq.forward(100)
#     hexa.left(60)
#     hexa.forward(100)
#     octa.left(45)
#     octa.forward(100)
    
    
# wn.exitonclick()

# import turtle
# import tkinter
# wn = turtle.Screen()
# star  = turtle.Turtle()
# #angle = 144
# angle = 2*(180-(360/5))
# for _ in range(5):
#     star.forward(500)
#     star.right(angle)
# wn.exitonclick()



# import turtle
# wn = turtle.Screen()
# e_tri = turtle.Turtle()
# sq = turtle.Turtle()
# hexa = turtle.Turtle()
# octa = turtle.Turtle()
# for x in range(8):
#     e_tri.left(120)
#     e_tri.forward(50)
#     sq.left(90)
#     sq.forward(50)
#     hexa.left(60)
#     hexa.forward(50)
#     octa.left(45)
#     octa.forward(50)
# wn.exitonclick()
# import turtle
# import tkinter
# wn = turtle.Screen()

# tri=turtle.Turtle()
# tri.up()
# tri.forward(50)
# tri.down()

# sq=turtle.Turtle()
# sq.up()
# sq.forward(-100)
# sq.down()

# hexa=turtle.Turtle()
# hexa.up()
# hexa.forward(200)
# hexa.down()

# octa=turtle.Turtle()
# octa.up()
# octa.forward(300)
# octa.right(90)
# octa.forward(70)
# octa.down()

# tri.color("red")
# sq.color("blue")
# hexa.color("pink")
# octa.color("purple")


# for _ in range (3):
#     tri.forward(50)
#     tri.left(120)
# for _ in range (4):
#     sq.forward(50)
#     sq.right(90)
# for _ in range (6):
#     hexa.forward(40)
#     hexa.left(60)
# for _ in range(8):
#     octa.forward(50)
#     octa.right(45)
# wn.exitonclick()


# import turtle
# wn = turtle.Screen()

# # defining all variables for Turtle() class
# eq = turtle.Turtle()
# sq = turtle.Turtle()
# hexa = turtle.Turtle()
# octa = turtle.Turtle()

# # imagine you have a pen in your hand and paper your pen is in the air thats penup() 
# # and you move the distance of the pen to some value and then put the pendown() 
# # these will mark the spot of the turtles "arrows" as starting positions
# # <variable>.forward(somevalue) will set the position where to mark the next marker.

# eq.penup()
# eq.setposition(-150 , 0)
# eq.pendown()

# sq.penup()
# sq.setposition(-70 , 0)
# sq.pendown()

# hexa.penup()
# hexa.setposition(0 , 0)
# hexa.pendown()

# octa.penup()
# octa.setposition(100 , 0)
# octa.pendown()

# #lets define angles the formula is angle = 360/number_of_sides"

# eq_angle = 360/3
# sq_angle = 360/4
# hexa_angle = 360/6
# octa_angle = 360/8
# tur_dist = 30

# for _ in range(3):
#     eq.forward(tur_dist)
#     eq.right(eq_angle)
    
# for _ in range(4):
#     sq.forward(tur_dist)
#     sq.right(sq_angle)

# for _ in range(6):
#     hexa.forward(tur_dist)
#     hexa.right(hexa_angle)
    
# for _ in range(8):
#     octa.forward(tur_dist)
#     octa.right(octa_angle)
    
# wn.exitonclick()

# import turtle
# import tkinter
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")

# hassan_line = turtle.Turtle()
# hassan = turtle.Turtle()

# hassan.shape("turtle")
# hassan.penup()

# # hassan_line.forward(20)
# for size in range(10):
#     hassan.forward(100)
#     # hassan.penup()    
#     # hassan.pendown()
#     hassan.stamp()    
#     hassan.forward(-100)
#     hassan.right(36)
#     hassan_line.forward(20)
    
#############Strings, Lists, and Tuples#############

# a = "hello"
# b = "world"
# c = a + ' ' + b
# print(c)

# line_1a = "Cebcbe"
# d = len(line_1a)
# print(d)

# a = "Python Programming"
# print("Length of the string is: ", len(a))

# numbers = [5, 10, 15, 20, 25]
# print(type(numbers))
# print("Length of the list is: ", len(numbers))

# s = "python rocks"
# print(s[3])



# fruit = "Banana"
# print(len(fruit))

# fuit = 'Banana'
# print(len(fuit))

# alist = ["hello", 2.0, 5]
# print(len(alist))
# print(len(alist[0]))

# a=[10, 20, 30] 
# print(a[-1: ])
# s = 'python'
# print(len(s))
# print(s[0])
# print(s[0],s[len(s)-2])
# print(s[-1])
# print(s[4])
#print(s[0:2])

# myList = ["one", 2.0, [1,],"two", "three"]
# print(myList[1])
# print(len(myList))
# print(s[0],s[len(s)-2])
# print(myList[-1])


# my_list = [6, 20, 5, 6, 30]
# print(my_list[0], my_list[1], my_list[-1], my_list[-2], 1 + my_list[2])

# my_list = [1, 2, 3, "hassan", 4.0]
# my_list[2] = 5
# print(my_list)
# #my_list[3] = 7
# my_list[4] = 'zain'
# ext_string = my_list[3]
# slice_char = ext_string[0:2] # includes everything withing the range defined
# ext_char = ext_string[1]

# print(ext_char, slice_char, my_list)

# #tuples

# my_list = (1, 2, 3, "hassan", 4.0)
# #my_list[2] = 5
# #my_list[3] = 7
# #my_list[4] = 'zain'
# ext_string = my_list[3]
# slice_char = ext_string[0:2] # includes everything withing the range defined
# ext_char = ext_string[1]

# print(ext_char, slice_char, my_list)

# let = "z"
# let_two = "p"
# c = let_two + let
# m = c*5
# print(m)
# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
# last = sports[-3:]
# print(last)

# by = "You are"
# az = "doing a great "
# io = "job"
# qy = "keep it up!"
# message = by + " " + az + io + ", " + qy
# print(message)

# ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
# new = ls[2:4]
# print(new)

# l = ['w', '7', 0, 9]
# m = l[1]
# print(type(m))

# b = "My, what a lovely day"
# x = b.split(',')
# print(x)
# z = "".join(x)
# print(z)
# y = z.split()
# print(y)
# a = "".join(y)
# print(type(a))

# song = "The rain in Spain..."
# print(song.split())

# str1 = "OH THE PLACES YOU'LL GO"
# output = str1.split()
# print(output)

# by = "You are"
# az = "doing a great "
# io = "job"
# qy = "keep it up!"
# # concatinating with + and it also have , requires to be included
# message = [by+az+io+qy]
# print(message)



#############Iterations#############
#############forLoop#############

# for name in ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
#     print("Hi", name, "Please come to my party on Saturday!")



# a = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
# for x in a[0:3]:
#     print(x)    #here for loop will print string

# import turtle
# import tkinter
# wn = turtle.Screen()
# alex = turtle.Turtle()
# # alex.forward(50)
# # alex.left(90)
# # alex.forward(50)

# for i in [0, 1, 2, 3]:
#     alex.forward(50)
#     alex.left(90)
#     alex.forward(50)
    
# wn.exitonclick()

# ls = [100]
# print(type(ls))
# for i in ls:
#     print('X')

# a = ["Zuri", "Joseph", "Zain", "Zara", "Zainab", "Zainab"]

# for i in a:
#     print(i.count('Z'))

# b = " ".join(a)
# print(b)
# for i in a:
    
# c = b.count('z')
# print(c)

# import turtle
# import tkinter
# wn = turtle.Screen()
# alex = turtle.Turtle()

# a = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

# for i in a[:4]:
#     alex.color(i)
#     alex.forward(100)
#     alex.left(90)
    
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# alex = turtle. Turtle()

# for i in [0,1,2,3]:
#     alex.forward(50)
#     alex.left(90)
    
# wn.exitonclick()


# import turtle
# wn = turtle.Screen()
# alex = turtle.Turtle()

# for i in [0,1,2,3]:
#     alex.forward(50)
#     alex.left(90)
    
# wn.exitonclick()

# import image
# from PIL import Image
# img = image.Image(r"C:\Users\hassa\Downloads\amazing_mountain_landscape_2-wallpaper-3840x1600.jpg")
# p = img.getPixel(0, 0)
# print(img.getWidth(), img.getHeight(), img.getPixel(0, 0), p.getRed(), p.getGreen(), p.getBlue())

# p = img.getPixel(30,100)


########################################################

# w = range(10)

# tot = 0
# print("***** Before the For Loop ******")
# for num in w:
#     print("***** A New Loop Iteration ******")
#     print("Value of num:", num)
#     tot += num
#     print("Value of tot:", tot)
# print("***** End of For Loop *****")
# print("Final total:", tot)



########################################Booleans and Conditionals########################################

########################################

# Booleans are true or false

# print(False)
# print(type(False))
# print(type(True))

########################################

# print(5 == 6)
# print(5 == 5)
# print(5 != 6)
# print(5 < 6)
# print(5 > 6)
# print(5 <= 6)
# print(5 >= 6)

########################################

# literal : true, flase
# comparison:
    # L == R
    # L != R
    # L < R
    # L > R
    # L <= R
    # L >= R
# logical:
#   left and right both should be boolean to meet these conditions
    # not
    # and
    # or
# AND: "Both must be true."
# OR: "At least one must be true."
    
    
# x = 5
# print(x>0 and x<10)

# n = 25
# print(n%2 == 0 or n%3 == 0)

# python higher precedence
#   parenthesis
#   exponentiation
#  multiplication, division, remainder
# addition, subtraction
# comparison operators
# not
# and
# or
# assignment operators



########################################



# print('p' in 'apple')
# print('apple' in 'apple')
# print('' in 'a')
# print('' in 'apple')
# print('x' not in 'apple')


# print("a" in ["apple", "absolutely", "application", "nope", "a"])
# print('hello world')


########################################

# assert type(9//5) == int
# assert type(9.0//5) == int

# Think of assert as a way to "assert" that a condition must hold true for the program to continue.
# If the condition fails, it signals an issue in your program logic (or assumptions) and halts execution.



########################################


# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# first_type = type(lst[0])
# print(first_type)
# for item in lst:
#     assert type(item) == first_type
    
# lst2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 17]
# first_type = type(lst2[0])
# for item in lst2:
#     assert type(item) == first_type


########################################


# import turtle
# import tkinter
# wn = turtle.Screen()
# amy = turtle.Turtle()
# amy.pencolor("Pink")
# amy.forward(50)
# if amy.pencolor() == "Pink":
#     amy.right(60)
#     amy.forward(100)
# else:
#     amy.left(60)
#     amy.forward(100)

# kenji = turtle.Turtle()
# kenji.forward(60)
# if kenji.pencolor() == "Pink":
#     kenji.right(60)
#     kenji.forward(100)
# else:
#     kenji.left(60)
#     kenji.forward(100)

# wn.exitonclick()


########################################


# import turtle
# import tkinter
# wn = turtle.Screen()

# amy = turtle.Turtle()
# amy.pencolor("Pink")
# amy.right(170)

# colors = ["Purple", "Black", "Orange", "Pink", "Orange", "Yellow", "Purple", "Orange", "Pink", "Pink", "Orange", "Yellow", "Purple", "Orange", "Purple", "Yellow", "Orange", "Pink", "Orange", "Purple", "Purple", "Yellow", "Orange", "Pink", "Orange", "Yellow", "Purple", "Yellow"]


# for color in colors:
#     if amy.pencolor() == "Purple":
#         amy.forward(50)
#         amy.speed(1)
#         amy.right(59)
#     elif amy.pencolor() == "Black":
#         amy.forward(65)
#         amy.left(98)
#     elif amy.pencolor() == "Orange":
#         amy.forward(30)
#         amy.left(60)
#     elif amy.pencolor() == "Pink":
#         amy.forward(50)
#         amy.right(57)

#     amy.pencolor(color)

# wn.exitonclick()

########################################

# x = 15
# if x % 2 == 0:
#     print(x, "is even")
# else:
#     print(x, "is odd") 


########################################

#accumulator pattern

# phrase = "what a wonderful day to program"
# tot = 0
# for char in phrase:
#     if char != " ":
#         tot = tot + 1
# print(tot)        

#no. of vowels in a string

# s = "what if we went to the zoo"
# x = 0
# for i in s:
#     if i in ['a', 'e', 'i', 'o', 'u']:
#         x += 1
# print(x)    



#max value accumulation, find the largest things in the list of numbers 

# nums = [9, 3, 8, 11, 5, 29, 2]

# x = nums[0]
# for a in nums:
#     if a > x:
#         x = a
# print(x)

# 






#Exam
# rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.


# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
# lst_rf = rainfall_mi.split(',')
# print(lst_rf) #making it a list

# rm = 0

# for rf in lst_rf:
#     rf_float = float(rf) #make it float
#     print(rf_float)
#     if rf_float > 3.0:
#         rm = rm + 1
# num_rainy_months = rm

# print(num_rainy_months)






######################################## MUTATABLITY ########################################

# fruit = ["banana", "apple", "cherry"]
# print(fruit)

# fruit[0] = "pear"
# fruit[-1] = "orange"
# print(fruit)



# #modify the items in the list
# alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# alist[1:3] = ['x', 'y']
# print(alist)



# #delete the items in the list

# blist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# blist[1:3] = []
# print(blist)




########################################

# #lets see about strings
# #we cannot do this. Strings are immutable
# greeting = "Hello, world!"
# greeting[0] = 'J'
# print(greeting)


# #how to make it jello world

# greeting = "Hello, world!"
# print(greeting[2:-1])
# newGreeting = 'J' + greeting[1:]
# print(newGreeting)
# print(greeting)

# full_name = "john doe"
# first_name = full_name[:4].capitalize()
# last_name = full_name[5:].capitalize()

# print(first_name, last_name)
   
   
# tasks = ["email Frank", "call Sarah", "meet with Zach"]
# task.append("call Sarah")
# task.remove("email Frank")
# task[tasks]   


# phrase = "many  moons"
# phrase_expanded = phrase + " and many stars"
# phrase_larger = phrase_expanded + " litter"

# x = [1, 2, 3, 4, 5]
# # y = x
# # print(x)
# x = x.append(6)
# print(x)

# a = "hola"
# a = a.replace("h", "H")
# print(a)




########################################List Element Deletion########################################

# a =['one', 'two', 'three']
# del a[1]
# print(a)

# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# del alist[1:5]
# print(alist)

# w = ['a', 'b', 'c', 'd', 'e', 'f']
# x = ['z']
# x = w
# print(x)

# a = [81,82,83]
# b = a[:]
# print(a)
# print(b)
# print(a == b)
# print(a is b)

# b[0] = 5
# print(a)
# print(b)

# alist = [4,2,8,6,5]
# blist = alist * 2
# blist[3] = 999
# print(alist)





########################################METHODS ON LIST########################################

# append, insert, count, index, reverse, sort, remove, pop
# append(), insert(), remove(), reverse(), sort() modify the list in place and do not return anything, 
# so you cannot assign their results.
# count() and index() return values but do not modify the list, 
# so you must assign their results if you need them later.
# pop() both modifies the list and returns a value, so you can assign it.


#create empty list
mylist = []
# mylist.append(5)    #add 5 to the end of the list
# print(mylist)
# mylist.append(27)
# print(mylist)
# mylist.append(3)
# print(mylist)
# mylist.append(12)
# print(mylist)

# mylist.insert(1, 12)    #add 12 at index 1
# print(mylist)
# cnt = mylist.count(12)    #count the number of 12s in the list
# print(cnt)

# ind = mylist.index(3)    #find the index of the first 3 in the list
# print(ind)

# mylist.reverse()    #reverse the list
# print(mylist)

# mylist.sort()    #sort the list
# print(mylist)
# mylist.remove(5)    #remove the first 5 from the list
# print(mylist)


# pop and count return a value



# alist = [4,2,8,6,5]
# alist.append(True)
# print(alist)


########################################

# origlist = [45,32,88]
# print("origlist:", origlist)
# print("the identifier:", id(origlist))             #id of the list before changes
# newlist = origlist + ['cat']
# print("newlist:", newlist)
# print("the identifier:", id(newlist))              #id of the list after concatentation
# origlist.append('cat')
# print("origlist:", origlist)
# print("the identifier:", id(origlist))             #id of the list after append is used



# We have previously described x += 1 as a shorthand for x = x + 1. 
# With lists, += is actually a little different. 
# In particular, origlist += [“cat”] appends “cat” to the end of the original list object.

# st = "Warmth"
# a = []


# st = "Warmth"
# a = []
# b = a + [st[0]]
# print(b)
# c = b + [st[1]]
# print(c)
# d = c + [st[2]]
# e = d + [st[3]]
# f = e + [st[4]]
# g = f + [st[5]]
# print(g)

# alist = [4,2,8,6,5]
# alist = alist + 999
# print(alist)


# ss = "Hello, World"
# print(ss.upper())

# tt = (ss.lower())

# print(ss.count("l"))

# print("****"+ss.strip()+"***")

# news = ss.replace("o", "***")
# print(news)


# print("*******************************")
# s = "python rocks"
# print(s[1]*s.index("n"))


# print("*******************************")
# s = "abcde"
# print(s[0])
# print(s.index("e"))
# print(len(s))

# print("*******************************")
# s = "hello"
# print(s[1])
# print(s[4])
# print(s[-1])
# print(s[-2])


# print("*******************************")
# s = "abcdefghijklmno"
# print(s[2:5])
# print(s[:4])
# print(s[7:])
# pritn(s[-3:])


####################string methods####################

# #upper()

# print("hello".upper())
# print("pyThon".upper())
# print("aBc123".upper())
# print("uppgercase".upper())
# print("UPPER".upper())


# #lower()

# print("HELLO".lower())
# print("heLloWorld".lower())
# print("AbC134".lower())
# print("lower".lower())


# #count()

# print("hello".count("l"))
# print("banana".count("a"))
# print("mississippi".count("ss"))
# print("python".count("z"))
# print("aaaa".count("aa"))


# #index()

# print("hello".index("l"))
# print("hassan".index("s"))
# print("zain".index("n"))
# print("programming".index("m"))
# print("programming".index("gr"))
# print("hello".index("e"))             # Output: 1
# print("python".index("th"))           # Output: 2
# print("banana".index("na"))           # Output: 2
# # print("hello".index("z"))           # Raises an error (substring not found)
# print("programming".index("m"))       # Output: 6


# #strip()
# print("  hello  ".strip())            # Output: hello
# print("  python  ".strip())           # Output: python
# print("  abc 123  ".strip())          # Output: abc 123
# print("   ".strip())                  # Output: (empty string)
# print("strip me".strip())             # Output: strip me

# #replace()
# print("hello".replace("l", "x"))      # Output: hexxo
# print("banana".replace("a", "o"))     # Output: bonono
# print("python".replace("p", "P"))     # Output: Python
# print("12345".replace("2", "two"))    # Output: 1two345
# print("aaaaa".replace("aa", "b"))     # Output: bba

#format()
# print("Hello, {}!".format("Alice"))   # Output: Hello, Alice!
# print("{} + {} = {}".format(2, 3, 5)) # Output: 2 + 3 = 5
# print("My name is {}".format("Bob"))  # Output: My name is Bob
# print("{1}, {0}".format("A", "B"))    # Output: B, A
# print("{} is {}".format("Python", "fun")) # Output: Python is fun
#print("{1}, {0}, {1}".format("A", "B"))  # Output: B, A, B



####################lsit methods####################

# #upper()
# words = ["hello", "world", "this", "is", "the", "end"]
# uppercase_words = []

# # loop through each word in the lsit
# for word in words:
#     uppercase_words.append(word.upper())
# print(uppercase_words)    


# example_two = ["uppercase", "UPPER", "aBc"]
# example_two_words = []
# for x in example_two:
#     example_two_words.append(x.upper())
# print(example_two_words)


# #lower()
# lower_words = ["HELLO", "PYTHON", "ABC123"]
# lowercase_words = []

# #loop through each word in the list
# for word in words:
#     lowercase_words.append(word.lower())
# print(lowercase_words)    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                


# # Step 1: Create a list
# fruits = ["apple", "banana", "cherry"]
# print("Original List:", fruits)  # Original List: ['apple', 'banana', 'cherry']

# # Step 2: append() - Add an item to the end of the list
# fruits.append("orange")
# print("After append('orange'):", fruits)  # After append('orange'): ['apple', 'banana', 'cherry', 'orange']

# # Step 3: extend() - Add multiple items to the end of the list
# fruits.extend(["grape", "kiwi"])
# print("After extend(['grape', 'kiwi']):", fruits)  # After extend(['grape', 'kiwi']): ['apple', 'banana', 'cherry', 'orange', 'grape', 'kiwi']

# # Step 4: insert() - Insert an item at a specific index
# fruits.insert(2, "mango")
# print("After insert(2, 'mango'):", fruits)  # After insert(2, 'mango'): ['apple', 'banana', 'mango', 'cherry', 'orange', 'grape', 'kiwi']

# # Step 5: remove() - Remove the first occurrence of an item
# fruits.remove("banana")
# print("After remove('banana'):", fruits)  # After remove('banana'): ['apple', 'mango', 'cherry', 'orange', 'grape', 'kiwi']

# # Step 6: pop() - Remove and return the item at a specific index
# popped_item = fruits.pop(3)
# print("After pop(3):", fruits)  # After pop(3): ['apple', 'mango', 'cherry', 'grape', 'kiwi']
# print("Popped Item:", popped_item)  # Popped Item: orange

# # Step 7: clear() - Remove all items from the list (commented out to avoid losing data)
# # fruits.clear()
# # print("After clear():", fruits)

# # Step 8: index() - Find the index of the first occurrence of an item
# index = fruits.index("mango")
# print("Index of 'mango':", index)  # Index of 'mango': 1

# # Step 9: count() - Count the number of occurrences of an item
# count = fruits.count("apple")
# print("Count of 'apple':", count)  # Count of 'apple': 1

# # Step 10: sort() - Sort the list in place (alphabetically)
# fruits.sort()
# print("After sort():", fruits)  # After sort(): ['apple', 'cherry', 'grape', 'kiwi', 'mango']

# # Step 11: reverse() - Reverse the order of items in the list
# fruits.reverse()
# print("After reverse():", fruits)  # After reverse(): ['mango', 'kiwi', 'grape', 'cherry', 'apple']

# # Step 12: copy() - Create a shallow copy of the list
# fruits_copy = fruits.copy()
# print("Copy of the list:", fruits_copy)  # Copy of the list: ['mango', 'kiwi', 'grape', 'cherry', 'apple']

# # Step 13: len() - Get the length of the list
# length = len(fruits)
# print("Length of the list:", length)  # Length of the list: 5

# # Step 14: in - Check if an item exists in the list
# exists = "kiwi" in fruits
# print("Is 'kiwi' in the list?", exists)  # Is 'kiwi' in the list? True

# # Step 15: del - Delete an item at a specific index
# del fruits[1]
# print("After del fruits[1]:", fruits)  # After del fruits[1]: ['mango', 'grape', 'cherry', 'apple']

# # Step 16: List Slicing - Extract a portion of the list
# sliced_fruits = fruits[1:3]
# print("Sliced List (fruits[1:3]):", sliced_fruits)  # Sliced List (fruits[1:3]): ['grape', 'cherry']


# append(x) – Adds an item x to the end of the list.
# extend(iterable) – Extends the list by appending elements from an iterable.
# insert(i, x) – Inserts item x at index i in the list.
# remove(x) – Removes the first occurrence of item x from the list.
# pop(i) – Removes and returns the item at index i (defaults to the last item).
# clear() – Removes all elements from the list, making it empty.
# index(x) – Returns the index of the first occurrence of item x in the list.
# count(x) – Returns the number of times item x appears in the list.
# sort() – Sorts the list in ascending order (modifies in place).
# reverse() – Reverses the order of elements in the list.
# copy() – Returns a shallow copy of the list.
# len(list) – Returns the number of elements in the list.
# in – Checks if an item exists in the list (x in list returns True/False).
# del list[i] – Deletes the item at index i from the list.
# list[start:end] – Returns a sliced portion of the list from start to end-1.



# #for loop in format
# scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
# for person in scores:
#     name = person[0]
#     score = person[1]
#     print("Hello {}. Your score is {}.".format(name, score))



##########################################non-mutating methods on strings#########################################



# scores = [("Rodney Dangerfield", -1), ("marlon brando", 1)]
# for person in scores:
#     name = person[0]
#     score = person[1]
#     print("Hello {}. Your score is {}.".format(name, score))


# origPrice = float(input('Enter the original price: $'))
# discount = float(input('Enter discount percentage: '))
# newPrice = (1 - discount/100)*origPrice
# calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
# print(calculation)




##########################################f-String#########################################

# first_name = "hassan"
# last_name = "sarmad"
# score = 96.75
# print(f"Hello {first_name} {last_name}. Your score is {min(score, 60)}.")
# print(f"Hello {first_name} {last_name}. your score is {max(score, 60):.3f}.")


# s = "I saw the movie, Mary Poppins Returns, and I thought it was great."

# #all the expressions
# r_count = s.count("r")
# all_case_r_count = s.lower().count("r")
# print(all_case_r_count)
# r_precentage = all_case_r_count/len(s)*100
# print(r_precentage)

# #use mostly variables inside f-strings or format()
# first_str = f"The number of r charactres: {r_count}."
# second_str = "The percentage of r characters (upper or lower case): {:.2f}%.".format(r_precentage)
# # display
# print( first_str + " " + second_str)

# lst = ['hassn', 'zain', 'zara', 'zainab']
# lst.remove('zain')
# first_three = lst[:3]
# print(first_three)
# x = ["dogs", "cats", "birds", "reptiles"]
# print(x)
# y = x
# print(y)
# x += ["fish", "horses"]
# print(x)
# y = y + ["sheep"]
# print(y)


# sent = "The mall has excellent sales right now."
# print(sent)
# wrds = sent.split()
# print(wrds)
# wrds[1] = 'store'
# new_sent = " ".join(wrds)
# print(new_sent)


################################################The Accumulator Pattern################################################
# nums = [3, 5, 8]
# accum = []
# for w in nums: #itteration starts with first value in the list like 3
#     x = w**2    #the square of 3 for the first accum
#     accum.append(x) #
#     print(accum)    
    
    
# alist = [4,2,8,6,5]
# blist = [ ]
# for item in alist:
#    blist.append(item+5)
# print(blist)    

# lst = [3, 0, 9, 4, 1, 7]
# new_lst = []
# for i in range(len(lst)):
#     new_lst.append(lst[i]+5)
# print(new_lst)    



numbs = [5, 10, 15, 20, 25]
a = len(numbs)
print(a)
b = range(len(numbs))
print(b)