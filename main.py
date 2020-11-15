import turtle

#initialize screen
wn=turtle.Screen()
#screen title
wn.title("ping pong")
#screen background color
wn.bgcolor("Black")
#screen configurations
wn.setup(width=800,height=600)

# wn.tracer(0)


#paddle 1

paddle_1=turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=3,stretch_len=0.3)
paddle_1.penup()
paddle_1.goto(-350,0)

#paddle_2 

paddle_2=turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=3,stretch_len=0.3)
paddle_2.penup()
paddle_2.goto(350,0)

#Ball

Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.shapesize(stretch_wid=0.5,stretch_len=0.5)
Ball.penup()
Ball.goto(0,0)
Ball.dx=2
Ball.dy=-2


#function to move the paddle 1 up

def paddle_1_up():
    y=paddle_1.ycor()
    if y>=240:
        y=y
    else:
        y+=20

    paddle_1.sety(y)


#function to move the paddle 1 down
def paddle_1_down():
    y=paddle_1.ycor()
    if y<=-240:
        y=y
    else:
        y-=20

    paddle_1.sety(y)

#function to move the paddle 2 up

def paddle_2_up():
    y=paddle_2.ycor()
    if y>=240:
        y=y
    else:
        y+=20
    paddle_2.sety(y)


#function to move the paddle 2 down
def paddle_2_down():
    y=paddle_2.ycor()
    if y<=-240:
        y=y
    else:
        y-=20
    paddle_2.sety(y)

#keyboard listener listens for keyboard input

wn.listen()

#takes input fromkeyboard and performs action for paddle 1

wn.onkeypress(paddle_1_up,"w")
wn.onkeypress(paddle_1_down,"s")

#takes input fromkeyboard and performs action for paddle 2

wn.onkeypress(paddle_2_up,"o")
wn.onkeypress(paddle_2_down,"l")


count_2=0
count_1=0

#main game loop
while True:
    wn.update()
    
    Ball.setx( Ball.dx + Ball.xcor())
    Ball.sety( Ball.dy + Ball.ycor())

    if Ball.ycor() >=290 or Ball.ycor() <= -290:
        Ball.sety(Ball.ycor())
        Ball.dy*=-1

    if Ball.xcor() >= 390 or Ball.xcor() <= -390:
        Ball.goto(0,0)
        Ball.dx*=-1
        break
        
    if (( paddle_2.ycor()-20 <=Ball.ycor() <= paddle_2.ycor()+20) and Ball.xcor() == 340 and paddle_2.xcor()==350):
        Ball.setx(Ball.xcor())
        Ball.dx*=-1
        count_2+=1


    if (( paddle_1.ycor()-20 <=Ball.ycor() <= paddle_1.ycor()+20) and Ball.xcor() == -340 and paddle_1.xcor()==-350):
        Ball.setx(Ball.xcor())
        Ball.dx*=-1
        count_1+=1

while True:
    wn.update()
    turtle.color('green')
    style = ('Courier', 30, 'italic')
    if count_1>count_2:
        turtle.write('player 1 wins', font=style, align='right')
        turtle.write(f'|score is:{count_1}', font=style, align='left')
    elif count_1<count_2:
        turtle.write('player 2 wins', font=style, align='right')
        turtle.write(f'|score is:{count_2}', font=style, align='left')
    else:
        turtle.write('Its a tie', font=style, align='right')
        turtle.write(f'|score is:{count_1}', font=style, align='left')
    turtle.hideturtle()