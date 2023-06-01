from tkinter import *
import turtle, time, random
def işlemler(x):
    
    if x==0:
        pencere = turtle.Screen()
        pencere.setup(width=1000,height=600)
        pencere.title('Lets catch TURTLEE')
        pencere.bgcolor('grey')
        pencere.bgpic('bgcolor2.gif')
        pencere.tracer(2)

        pencere.register_shape('marioegg.gif')

        oyuncu_b = turtle.Turtle()
        oyuncu_b.penup()
        oyuncu_b.speed(0)
        oyuncu_b.color('purple')
        oyuncu_b.shape('marioegg.gif')
        oyuncu_b.shapesize(3)
        oyuncu_b.goto(500,0)


        oyuncu_a = turtle.Turtle()
        oyuncu_a.penup()
        oyuncu_a.speed(0)
        oyuncu_a.color('dark green')
        oyuncu_a.shape('marioegg.gif')
        oyuncu_a.goto(-500,0)
        oyuncu_a.shapesize(3)


        score_a=0
        score_b=0

        yazıPuan_a = turtle.Turtle()
        yazıPuan_a.speed(0)
        yazıPuan_a.color('white')
        yazıPuan_a.penup()
        yazıPuan_a.hideturtle()
        yazıPuan_a.goto(-250,200)
        yazıPuan_a.write('Player A: {}'.format(score_a), align='center', font=('impact',24,'normal'))

        yazıPuan_b = turtle.Turtle()
        yazıPuan_b.speed(0)
        yazıPuan_b.color('white')
        yazıPuan_b.penup()
        yazıPuan_b.hideturtle()
        yazıPuan_b.goto(250,200)
        yazıPuan_b.write('Player B: {}'.format(score_b), align='center', font=('impact',24,'normal'))


        speed = 2

        def turnLeft():
            oyuncu_b.left(30)
        def turnRight():
            oyuncu_b.right(30)
        def turnA():
            oyuncu_a.left(30)
        def turnD():
            oyuncu_a.right(30)


        h2 = turtle.Turtle()
        h2.speed(0)
        h2.color('yellow')
        h2.penup()
        h2.goto(0,-200)
        h2.hideturtle()
    
        pencere.listen()
        pencere.onkey(turnLeft,'Left')
        pencere.onkey(turnRight,'Right')
        pencere.onkey(turnA,'a')
        pencere.onkey(turnD,'d')

        maxHedef = 5
        hedefler_a =[]
        hedefler_b =[]
        for i in range(maxHedef):
            hedefler_a.append(turtle.Turtle())
            hedefler_a[i].penup()
            hedefler_a[i].color('blue')
            hedefler_a[i].shape('turtle')
            hedefler_a[i].speed(0)
            hedefler_a[i].setposition(random.randint(-500,0),random.randint(-300,300))

        for i in range(maxHedef):
            hedefler_b.append(turtle.Turtle())
            hedefler_b[i].penup()
            hedefler_b[i].color('orange')
            hedefler_b[i].shape('turtle')
            hedefler_b[i].speed(0)
            hedefler_b[i].setposition(random.randint(0,500),random.randint(-300,300))

        while(True):
    
            oyuncu_b.forward(speed)
            oyuncu_a.forward(speed)
    
            if oyuncu_b.xcor()>500 or oyuncu_b.xcor()<0:
                oyuncu_b.right(180)
            if oyuncu_b.ycor()>300 or oyuncu_b.ycor()<-300:
                oyuncu_b.right(180)
            if oyuncu_a.xcor()<-500 or oyuncu_a.xcor()>0:
                oyuncu_a.right(180)
            if oyuncu_a.ycor()>300 or oyuncu_a.ycor()<-300:
                oyuncu_a.right(180)
        
    
   
            if hedefler_a[0].xcor()<-500 or hedefler_a[0].xcor()>0:
                hedefler_a[0].right(random.randint(150,250))
            if hedefler_a[0].ycor()<-300 or hedefler_a[0].ycor()>300:
                hedefler_a[0].right(180)
    
            if hedefler_a[1].xcor()<-500 or hedefler_a[1].xcor()>0:
                hedefler_a[1].right(random.randint(150,250))
            if hedefler_a[1].ycor()<-300 or hedefler_a[1].ycor()>300:
                hedefler_a[1].right(180)
    
            if hedefler_a[2].xcor()<-500 or hedefler_a[2].xcor()>0:
                hedefler_a[2].right(random.randint(150,250))
            if hedefler_a[2].ycor()<-300 or hedefler_a[2].ycor()>300:
                hedefler_a[2].right(180)
    
    
            if hedefler_a[3].xcor()<-500 or hedefler_a[3].xcor()>0:
                hedefler_a[3].right(random.randint(150,250))
            if hedefler_a[3].ycor()<-300 or hedefler_a[3].ycor()>300:
                hedefler_a[3].right(180)
        
    
            if hedefler_a[4].xcor()<-500 or hedefler_a[4].xcor()>0:
                hedefler_a[4].right(random.randint(150,250))
            if hedefler_a[4].ycor()<-300 or hedefler_a[4].ycor()>300:
                hedefler_a[4].right(180)

            if hedefler_b[0].xcor()>500 or hedefler_b[0].xcor()<0:
                hedefler_b[0].right(random.randint(150,250))
            if hedefler_b[0].ycor()>300 or hedefler_b[0].ycor()<-300:
                hedefler_b[0].right(180)
    
            if hedefler_b[1].xcor()>500 or hedefler_b[1].xcor()<0:
                hedefler_b[1].right(random.randint(150,250))
            if hedefler_b[1].ycor()>300 or hedefler_b[1].ycor()<-300:
                hedefler_b[1].right(180)
    
            if hedefler_b[2].xcor()>500 or hedefler_b[2].xcor()<0:
                hedefler_b[2].right(random.randint(150,250))
            if hedefler_b[2].ycor()>300 or hedefler_b[2].ycor()<-300:
                hedefler_b[2].right(180)
    
            if hedefler_b[3].xcor()>500 or hedefler_b[3].xcor()<0:
                hedefler_b[3].right(random.randint(150,250))
            if hedefler_b[3].ycor()>300 or hedefler_b[3].ycor()<-300:
                hedefler_b[3].right(180)
    
            if hedefler_b[4].xcor()>500 or hedefler_b[4].xcor()<0:
                hedefler_b[4].right(random.randint(150,250))
            if hedefler_b[4].ycor()>300 or hedefler_b[4].ycor()<-300:
                hedefler_b[4].right(180)
    
    
            for i in range(maxHedef):
                hedefler_a[i].forward(1)
                if oyuncu_a.distance(hedefler_a[i])<40:
                    hedefler_a[i].setposition(random.randint(-500,0),random.randint(-300,300))
                    score_a = score_a + 1
                    yazıPuan_a.clear()
                    yazıPuan_a.write('Player A: {}'.format(score_a), align='center', font=('impact',24,'normal'))
            
            for i in range(maxHedef):
                hedefler_b[i].forward(1)
                if oyuncu_b.distance(hedefler_b[i])<40:
                    hedefler_b[i].setposition(random.randint(0,500),random.randint(-300,300))
                    score_b = score_b + 1
                    yazıPuan_b.clear()
                    yazıPuan_b.write('Player B: {}'.format(score_b), align='center', font=('impact',24,'normal'))
    
            if (score_a==10) or (score_b==10):
                pencere.clear()
                pencere.bgpic('congrats2.gif')
                if score_a==10:
                    h2.clear()
                    h2.write('Player A you won', align='center',font=('impact', 30))
                    break
                elif score_b==10:
                    h2.clear()
                    h2.write('Player B you won', align='center',font=('impact', 30))
                    break   
                
    
    
    
    if x==1:
        pencere = turtle.Screen()
        pencere.title('Lets play PINPOONN!! :)')
        pencere.bgcolor('grey')
        pencere.bgpic('view.gif')
        pencere.setup(width=800,height=600)
        pencere.tracer(0)

        racket_a = turtle.Turtle()
        racket_a.speed(0)
        racket_a.shape('square')
        racket_a.color('purple')
        racket_a.penup()
        racket_a.goto(-350,0)
        racket_a.shapesize(5,1)

        racket_b = turtle.Turtle()
        racket_b.speed(0)
        racket_b.shape('square')
        racket_b.color('purple')
        racket_b.penup()
        racket_b.goto(350,0)
        racket_b.shapesize(5,1)

        pencere.register_shape('yıldız.gif')

        ball=turtle.Turtle()
        ball.speed(0)
        ball.color('darkred')
        ball.shape('yıldız.gif')
        ball.penup()
        ball.dx = 0.30
        ball.dy = 0.30

        h1 = turtle.Turtle()
        h1.speed(0)
        h1.color('yellow')
        h1.penup()
        h1.goto(0,260)
        h1.write("Player A:0     Player B:0", align='center',font=('impact', 24)) 
        h1.hideturtle()
        
        h2 = turtle.Turtle()
        h2.speed(0)
        h2.color('yellow')
        h2.penup()
        h2.goto(0,-200)
        h2.hideturtle()

        puan_a = 0
        puan_b = 0

        def racket_a_up():
            y=racket_a.ycor()
            y=y+20
            racket_a.sety(y)
        def racket_a_down():
            y=racket_a.ycor()
            y=y-20
            racket_a.sety(y)
        def racket_b_up():
            y=racket_b.ycor()
            y=y+20
            racket_b.sety(y)
        def racket_b_down():
            y=racket_b.ycor()
            y=y-20
            racket_b.sety(y)

        durum = False
        def change():
            global durum
            if durum == True:
                durum=False
            else:
                durum=True
    
        pencere.listen()
        pencere.onkeypress(racket_a_up, 'w')
        pencere.onkeypress(racket_a_down, 's')
        pencere.onkeypress(racket_b_up, 'Up')
        pencere.onkeypress(racket_b_down, 'Down')
        pencere.onkeypress(change, 'space')


        while (True):
            pencere.update()
            if not durum:
                ball.setx(ball.xcor() + ball.dx)
                ball.sety(ball.ycor() + ball.dy)
    
                if ball.ycor()>290 or ball.ycor()<-290:
                    ball.dy = ball.dy * -1
    
                if ball.xcor()>390:
                    ball.goto(0,0)
                    ball.dx = ball.dx * -1
                    puan_a = puan_a+1
                    h1.clear()
                    h1.write("Player A:{}     Player B:{}".format(puan_a,puan_b), align='center',font=('impact', 24)) 
        
                if ball.xcor()<-390:
                    ball.goto(0,0)
                    ball.dx = ball.dx * -1
                    puan_b = puan_b+1
                    h1.clear()
                    h1.write("Player A:{}     Player B:{}".format(puan_a,puan_b), align='center',font=('impact', 24)) 

        
                if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<racket_b.ycor()+60 and ball.ycor()>racket_b.ycor()-60):
                    ball.setx(340)
                    ball.dx = ball.dx * -1
        
                if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<racket_a.ycor()+60 and ball.ycor()>racket_a.ycor()-60):
                    ball.setx(-340)
                    ball.dx = ball.dx * -1
    
                if (puan_a==5) or (puan_b==5):
                    pencere.clear()
                    pencere.bgpic('gameover_pinpon.gif')
                    if puan_a==5:
                        h2.clear()
                        h2.write('Congratulations player A you won', align='center',font=('impact', 30))
                        break
                    elif puan_b==5:
                        h2.clear()
                        h2.write('Congratulations player B you won', align='center',font=('impact', 30))
                        break
    


pencere=Tk()
pencere.geometry("400x250")
pencere.title("LET'S PLAY:)")


label=Label(pencere,font="impact 25 bold",fg="dark green",text="LET'S PLAY GAME!")
label.pack()
label.place(x=85,y=20)

label=Label(pencere,font="arial 15 bold",fg="dark green",text="Which one do you want to play?")
label.pack()
label.place(x=50,y=100)

butonlar = []

for i in range(2):
    butonlar.append(Button(font="arial 15 bold",bg="dark grey",fg="dark green",width=12,command=lambda x=i:işlemler(x)))

index=0

butonlar[0]['text']="C TURTLE"
butonlar[1]['text']="PINPON"



for j in range(2):
    butonlar[index].place(x=50+160*j,y=150)
    index+=1

pencere.mainloop()