import turtle

window = turtle.Screen()
window.bgcolor("black")

#Dessin citrouille
citrouille = turtle.Turtle()
citrouille.color("orange")
citrouille.dot(200)

#Utilisation crayon
crayonNoir = turtle.Turtle()
crayonNoir.color("black")

#Base
crayonNoir.penup()
crayonNoir.setposition(-200,-110)
crayonNoir.pensize(60)
crayonNoir.pendown()
crayonNoir.forward(400)
crayonNoir.pensize(2)

crayonNoir.color("yellow")

#Oeil
def oeil(origine, orientation):
    crayonNoir.penup()
    crayonNoir.setheading(0)
    crayonNoir.setposition(origine)
    crayonNoir.pendown()
    crayonNoir.begin_fill()
    crayonNoir.forward(orientation * 40)
    crayonNoir.setheading(orientation * 115)
    crayonNoir.forward(orientation * 40)
    crayonNoir.end_fill()

oeil((-50,20),1)
oeil((50,20),-1)

def bouche(nombreDent):
    for n in range(nombreDent):
        crayonNoir.forward(15)
        crayonNoir.right(90)
        crayonNoir.forward(15)
        crayonNoir.left(90)

crayonNoir.penup()
crayonNoir.setposition(-50,-30)
crayonNoir.setheading(45)
crayonNoir.pendown()
crayonNoir.pensize(1)
crayonNoir.begin_fill()

bouche(5)

crayonNoir.setheading(180)
crayonNoir.forward(10)
crayonNoir.setheading(225)

bouche(4)

crayonNoir.end_fill()

#Nez
crayonNoir.penup()
crayonNoir.setposition(0,0)
crayonNoir.setheading(90)
crayonNoir.shape("triangle")
crayonNoir.stamp()

#texte
texte = turtle.Turtle()
texte.color("orange")
texte.penup()
texte.sety(175)
texte.write('Halloween',font=('Arial', 40, 'bold') , align="center")
texte.hideturtle()


turtle.done()
