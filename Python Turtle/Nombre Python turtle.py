import turtle 

for i in range(12):  
    for colors in ["black", "gray","white"]:  
        turtle.color(colors) 
        turtle.speed(0) 
        turtle.circle(140)  
        turtle.left(10)  

#Letra J
tortuga=turtle.Turtle()
tortuga.pensize(15)
tortuga.color("black")
tortuga.shape('turtle')
tortuga.speed(5)
tortuga.penup()
tortuga.goto(-260,0)
tortuga.pendown()
tortuga.right(0)
tortuga.forward(80)
tortuga.left(270)
tortuga.forward(150)
tortuga.circle(-50,180)

#Letra O
tortuga.color("gray")
tortuga.penup()
tortuga.goto(-150,-120)
tortuga.pendown()
tortuga.speed(5)
tortuga.right(0)
tortuga.circle(-70)

#Letra A
tortuga.color("black")
tortuga.penup()
tortuga.goto(10,-190)
tortuga.pendown()
tortuga.speed(5)
tortuga.right(20)
tortuga.forward(160)
tortuga.right(-40)
tortuga.forward(-160)
tortuga.penup()
tortuga.goto(40,-120)
tortuga.pendown()
tortuga.right(110)
tortuga.forward(50)

#Letra N
tortuga.color("gray")
tortuga.penup()
tortuga.goto(150,-190)
tortuga.pendown()
tortuga.speed(5)
tortuga.lt(90)
tortuga.fd(140)
tortuga.rt(145)
tortuga.fd(170)
tortuga.lt(145)
tortuga.fd(160)
