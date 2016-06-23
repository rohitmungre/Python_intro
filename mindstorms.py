import turtle

def draw_square(some_turtle):    
    count = 0
    while count <= 3:
        some_turtle.forward(100)
        some_turtle.right(90)
        count = count +1        

def draw_circle(some_turtle):
    some_turtle.circle(100) 

def paint():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(1,36):
        draw_square(brad)
        brad.right(10)
    
#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("blue")
#    angie.speed(1)
    
#    draw_circle(angie)

    window.exitonclick()

paint()
