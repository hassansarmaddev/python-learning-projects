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
