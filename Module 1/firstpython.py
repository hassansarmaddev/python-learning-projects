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












