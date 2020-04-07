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

#dibujar cuadrados
'''
LADOS=4
def dibujarCuadrado( lado):
  t.pendown()
  for i in range(LADOS):
    t.forward( lado )
    t.left(90)
  t.penup()
'''
#dibujarRectangulo
REPETICIONES=2
def dibujarRectangulo(largo, ancho):
  t.pendown()
  for i in range(REPETICIONES):
    t.forward(largo)
    t.left(90)
    t.forward(ancho)
    t.left(90)

#tarea   
#dibujar triangulo

#dibujar circulo

'''
dibujarCuadrado( 100)
t.goto(0,78)
dibujarCuadrado( 20)
'''
dibujarRectangulo(50, 20)
