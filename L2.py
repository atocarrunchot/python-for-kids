import turtle

t = turtle.Turtle()

pnt = turtle.Screen()

pnt.bgcolor('white')

t.color('blue')

t.shape('turtle')
print( t.position())
t.penup()
t.forward(60)
t.right(90)
t.pendown()

#cuad
#version dificil
'''  
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
'''

#version facil
LADOS=4
for i in range(LADOS):
  t.forward(150)
  t.right(90)

t.penup()
t.forward(20)
t.right(90)
t.forward(20)
t.pendown()
BALETAS=4
for i in range(BALETAS):
  t.forward(50)
  t.left(90)
  
t.penup()
t.forward(60)
t.pendown()

VERTICES=4
for i in range(VERTICES):
  t.forward(50)
  t.left(90)
t.penup()
t.goto(0,70)
t.pendown()


#circle
CIRCLE=360
for i in range(CIRCLE):
  t.forward(1)
  t.right(1)

