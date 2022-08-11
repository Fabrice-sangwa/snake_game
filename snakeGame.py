#importation des modules 
import turtle
import random
import time


delay = 0.1 

#les scores 
score = 0
meilleur_score = 0


#configuration de l'écran 

win = turtle.Screen()
win.title("JEU DE SERPENT")
win.bgcolor("darkseagreen")
win.setup(width=600, height=600)
win.tracer(0)

#le serpent 

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


#Nourriture 

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)



segments = []

#Tableau des scores 

win_score = turtle.Turtle()
win_score.speed(0)
win_score.shape("square")
win_score.color("black")
win_score.penup()
win_score.hideturtle()
win_score.goto(0, 260)
win_score.write("Score : 0 Meilleur Score : 0", align="center", font=("ds-digital", 20, "normal"))


#les fonctions 

#les fonctions d'orientation 

def go_up():
    if head.direction != "down":
        head.direction = "up"
        
def go_down():
    if head.direction != "up":
        head.direction = "down"
        
def go_left():
    if head.direction != "right":
        head.direction = "left"
        
def go_right():
    if head.direction != "left":
        head.direction = "right"
        
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x  = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
#liaison au clavier

win.listen()
win.onkeypress(go_up, "u")
win.onkeypress(go_down, "n")
win.onkeypress(go_left, "g")
win.onkeypress(go_right, "k")


#boucle de fonctionnement 

while True:
    win.update()
    
    #verification de collision avec le bord
    
    if head.xcor() > 290 or head.xcor() < -290  or head.ycor() > 290 or head.ycor() <-290: 
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        
        #cacher le segment du corps 
        
        for segment in segments:
            segment.goto(1000, 1000) #en dehors du tableau
            
        #effacer le segment
        segments.clear()
        
        #restaurer le score 
        score = 0
        
        #restaurer le delais
        delay = 0.1
        
        win_score.clear()
        win_score.write("Score  : {} Meilleur Score {}".format(score, meilleur_score), align="center", font=("ds-digital", 20, "normal") )       

    #verification de la collision avec le repas
    if head.distance(food) < 20 : 
        
        #deplacement de la nouriture vers une autre place 
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        #ajout de la longueur du serpent 
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)
        
        #racourcir le delais 
        delay -= 0.001
        
        #incrementation du score
        score += 10
        
        if score > meilleur_score:
            meilleur_score = score
            
        win_score.clear()
        win_score.write("Score  : {} Meilleur Score {}".format(score, meilleur_score), align="center", font=("ds-digital", 20, "normal"))
    
    
    #deplacer le serpent dans l'ordre inversion 
    for index in range(len(segments)-1,0,-1,):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)     
            
    #deplacer  le serpent de 0 à la tete
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    
    
    #vérifier la collision avec le corps 
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #le segment 
            
            for segemnt in segments : 
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
         
            #adaptation du score
            
            win_score.clear()
            win_score.write("Score  : {} Meilleur Score {}".format(score, meilleur_score), align="center", font=("ds-digital", 20, "normal"))
        head.clear()
    time.sleep(delay)
win.mainloop()
    
    