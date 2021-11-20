import winsound      ## Only for Windows (in-built){For background Music}
import sys
import os

#For the exe to find exact path
def resource_path(relative_path):
      base_path = getattr(sys,"_MEIPASS",os.path.dirname(os.path.abspath(__file__)))
      return os.path.join(base_path,relative_path)

## Background Music
bgmusic = resource_path('FILES\\bg_music(lite).wav')
winsound.PlaySound(bgmusic,winsound.SND_LOOP + winsound.SND_ASYNC)

## Sounds
hit = resource_path("FILES\\hit.wav")
Eat = resource_path("FILES\\Eat.wav")

## backgrounds
bg = resource_path("FILES\\bg.GIF")
bghtp = resource_path("FILES\\bghtp.GIF")
settingsbg = resource_path("FILES\\settingsbg.GIF")


import turtle # Base Module
import time
import random
import pickle  # For data encryption
from playsound import playsound    # pip install playsound

#To Save High Scores 
try:
    with open("Highscore.dat",'rb') as f :
        hs = pickle.load(f)    
except:
    hs =[0,0,0]

      
#Default Level settings :
level = "normal"
delay = 0.08
high_score = hs[1]
goal_tm = 3

# To Save the settings 
try :
    with open("Settings.dat",'rb') as z :
        sett = pickle.load(z)
except :
    sett = ["white","black","red","grey"]
    
      
#Default Settings :
headcol = sett[0]
bgcol = sett[1]
foodcol = sett[2]
tailcol = sett[3]

#To check if Input is Valid or Not

raw_headcol = "white"
raw_bgcol = "black"
raw_foodcol = "red"
raw_tailcol = "grey"

#Variables For The Wighling of the Snake

i = 0
j = 0
k = 0
m = 0

#Defining Each Option of Menu

## Defining Main Game

def Play():
    ## Settings
    global headcol 
    global bgcol
    global foodcol 
    global tailcol
    
    ## Difficulties
    global level
    global hs  
    global delay
    global high_score
    global goal_tm

    b = 1
    goal = 0
    Star_Bonus = 110
    
    # Pausing Variables
    Pgoal = 0
    pause_tm = 0
    pauseend_tm = 0
    ps = 0
    pdirect = "stop"
    
    def void(x,y):
       pass

    def bac():
        nonlocal b
        b = 4
        sc.clearscreen()
        Menu()
        
    sc = turtle.Screen()
    sc.title("Snake ssssssssss")
    sc.bgcolor(bgcol)
    sc.setup(width=700,height=650)
    sc.tracer(0)      #Turns off screen updates(Hence, program becomes fastest)    

    head = turtle.Turtle()
    head.speed(0)     
    head.up()
    head.shape("circle")
    head.color(headcol)                
    head.goto(0,0)
    head.direction = "stop"    #Not using any other Variable,kyuki fir 'nonlocal' likhna padega wherever its used; hence, OOPS helps
    head.turtlesize(1.175)
    
    food = turtle.Turtle()
    food.speed(0)     # it is the animation speed
    food.shape("circle")
    food.color(foodcol)
    food.turtlesize(0.95)
    food.up()
    food.goto(random.randint(-270,270),random.randint(-270,270))

    #Tail

    segments =[]
    score = 0
    
    #Pen

    penG = turtle.Turtle()
    penG.goto(1900,1900)
    penG.color("white")
    penG.up()
    penG.speed(0)
    penG.ht()
    penG.goto(0,180)
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.up()
    pen.hideturtle()

    #pen2 for "Restart"

    pen2 = turtle.Turtle()
    pen2.speed(0)
    pen2.color('white')
    pen2.up()
    pen2.hideturtle()

    #FUNTIONS

    def go_up():
          global goal_tm
          nonlocal ps
          nonlocal pause_tm
          nonlocal pauseend_tm
          nonlocal Pgoal

          if head.direction != "down":
              if ps == 1:
                  if pdirect != 'down' :
                    head.direction = "up"
                    ps = 0
                    pauseend_tm = time.time()
                    if pause_tm >= Pgoal and pause_tm < (goal_tm + Pgoal):
                            pau_tm = pauseend_tm - pause_tm
                            Pgoal = Pgoal + pau_tm
              else :
                  head.direction = "up"
                  
    def go_left():
           global goal_tm
           nonlocal pdirect
           nonlocal ps
           nonlocal pause_tm
           nonlocal pauseend_tm
           nonlocal Pgoal

           if head.direction != "right":
               if ps == 1:
                   if pdirect != 'right' :
                        head.direction = "left"
                        ps = 0
                        pauseend_tm = time.time()
                        if pause_tm >= Pgoal and pause_tm < (goal_tm + Pgoal):
                                pau_tm = pauseend_tm - pause_tm
                                Pgoal = Pgoal + pau_tm
               else :
                   head.direction = "left"
                   
    def go_down():
            global goal_tm
            nonlocal pdirect
            nonlocal ps
            nonlocal pause_tm
            nonlocal pauseend_tm
            nonlocal Pgoal

            if head.direction != "up":  
                if ps == 1:
                    if pdirect != 'up' :
                        head.direction = "down"
                        ps = 0
                        pauseend_tm = time.time()
                        if pause_tm >= Pgoal and pause_tm < (goal_tm + Pgoal):
                                pau_tm = pauseend_tm - pause_tm
                                Pgoal = Pgoal + pau_tm
                else :
                    head.direction = "down"
                    
    def go_right():
          global goal_tm
          nonlocal pdirect
          nonlocal ps
          nonlocal pause_tm
          nonlocal pauseend_tm
          nonlocal Pgoal

          if head.direction != "left": 
              if ps == 1 :
                    if pdirect != 'left':
                        head.direction = "right"
                        ps = 0
                        pauseend_tm = time.time()
                        if pause_tm >= Pgoal and pause_tm < (goal_tm + Pgoal):
                                pau_tm = pauseend_tm - pause_tm
                                Pgoal = Pgoal + pau_tm
              else :
                  head.direction = "right"
                  
    def Main_move():
        if head.direction == "up":
            y = head.ycor()
            x = head.xcor()
            global i
            
            if i == 0:
                head.setx(x + 3)
                i = 1
            else :
                head.setx(x - 3)
                i = 0
                
            head.sety(y + 20)
            pen2.clear()
    
        if head.direction == "down":
            y = head.ycor()
            x = head.xcor()
            global j

            if j == 0:
                head.setx(x + 3)
                j = 1
            else :
                head.setx(x - 3)
                j = 0
                
            head.sety(y - 20)
            pen2.clear()
    
        if head.direction == "left":
            x = head.xcor()
            y = head.ycor()
            global k

            if k == 0:
                head.sety(y + 3)
                k = 1
            else :
                head.sety(y - 3)
                k = 0
                
            head.setx(x - 20)
            pen2.clear()
    
        if head.direction == "right":
            x = head.xcor()
            y = head.ycor()
            global m

            if m == 0:
                head.sety(y + 3)
                m = 1
            else :
                head.sety(y - 3)
                m = 0
                
            head.setx(x + 20)
            pen2.clear()

        if head.direction =="stop" :
          pen2.goto(0,-250)              
          pen2.write("Tap P to Pause/Resume and Esc to Return",align="center",font=("courier",20,"normal"))

    def pause():
          global goal_tm
          nonlocal pdirect
          nonlocal ps
          nonlocal pause_tm
          nonlocal pauseend_tm
          nonlocal Pgoal
          
          if ps == 1 :
                if len(segments) > 0:
                        segments[-1].color(tailcol)       
                head.direction = pdirect
                pdirect = 'stop'
                ps = 0
                pauseend_tm = time.time()
                pau_tm = pauseend_tm - pause_tm
                if pause_tm >= Pgoal and pause_tm < (goal_tm + Pgoal):
                      Pgoal = Pgoal + pau_tm
          else:
                pau_tm = 0
                ps = 1
                pdirect = head.direction 
                head.direction = "stop"
                pause_tm = time.time()
          
    #Keyboard Bindings   

    sc.listen()
    sc.onkeypress(go_up,"Up")
    sc.onkeypress(go_up,"w")
    sc.onkeypress(go_up,"W")
    sc.onkeypress(go_down,"Down")
    sc.onkeypress(go_down,"s")
    sc.onkeypress(go_down,"S")
    sc.onkeypress(go_right,"Right")
    sc.onkeypress(go_right,"d")
    sc.onkeypress(go_right,"D")
    sc.onkeypress(go_left,"Left")
    sc.onkeypress(go_left,"a")
    sc.onkeypress(go_left,"A")
    sc.onkeypress(bac,"Escape")
    sc.onkeypress(pause,"p")
    sc.onkeypress(pause,"P")
    sc.onscreenclick(void)
    
    while True:
      
      ##turtle.update() shows the animation <Shows Update of every iteration on the screen>
      sc.update()    #Every second this loop runs ,it updates the screen(WITHOUT this TURTLE disappears)         
        
      #Collisions with border
          
      if head.xcor() > 335 or head.xcor() < -337 or head.ycor() > 315 or head.ycor() < -315 :
                playsound(hit,block = False)
                head.color("crimson")
                for i in segments:
                    i.color("crimson")
                turtle.update()
                time.sleep(0.25)
                head.goto(0,0)
                head.color(headcol)
                head.direction = "stop"

                #Hiding segments Since, we cant erase them

                for i in segments :
                        i.hideturtle()
                
                segments.clear()
                score = 0
            
      #Food Eating checker
            
      if head.distance(food) < 22 :
            playsound(Eat,block = False)
            x = random.randint(-270,270)
            y = random.randint(-270,270)
            food.goto(x,y)
            
            if score%50 == 0 and score != 0 and goal >= 0:
                score = score + Star_Bonus
                penG.clear()
                food.turtlesize(0.95)
                food.color(foodcol)
            else :
                 #Adding a segment
                 new_segment = turtle.Turtle()
                 new_segment.speed(0)
                 new_segment.shape("circle")
                 new_segment.color(tailcol)
                 new_segment.up()    

                 segments.append(new_segment)
                 score += 10
                 if score%50 == 0 :
                       Pgoal = time.time()

      if ps == 0 :
            goal = goal_tm - (time.time() - Pgoal)
        
      if goal > 0 and (score)%50 == 0 and score != 0 :
              food.turtlesize(1.12)
              col = ["violet","indigo","blue","lightgreen","yellow","orange"]
              food.color(random.choice(col))
              penG.clear()
              penG.write("Time Left : {}".format(round(goal,2)),align = 'center',font=("courier",15,"bold"))

      elif goal <= 0 :
              food.turtlesize(0.95)
              penG.clear()
              food.color(foodcol)

      if score == 0 :
              food.turtlesize(0.95)
              food.color(foodcol)
              penG.clear()

      #Moving the segments only when game isnt paused
      if ps == 0 :
          for index in range(len(segments)-1,0,-1):
                      x = segments[index - 1].xcor()
                      y = segments[index - 1].ycor()
                      segments[index].goto(x,y)
        
          if len(segments) > 0 :          #For The First Tail Segment
                      x = head.xcor()
                      y = head.ycor()
                      segments[0].goto(x,y)

      if score > high_score :
            if level == "hard":
                        hs[2] = score
                        high_score = hs[2]
                        with open("Highscore.dat",'wb') as f :
                                 pickle.dump(hs,f)
                                 
            elif level == "normal":
                        hs[1] = score
                        high_score = hs[1]
                        with open("Highscore.dat",'wb') as f :
                                 pickle.dump(hs,f)

            elif level == "easy" :
                        hs[0] = score
                        high_score = hs[0]
                        with open("Highscore.dat",'wb') as f :
                                 pickle.dump(hs,f)

      pen.clear()
      level_to_show = level.capitalize()
      pen.goto(0,270)
      pen.write("Level : {}".format(level_to_show),align="center",font=("courier",28,"normal"))
      pen.goto(0,230)
      pen.write("Score :{}  High Score :{}".format(score,high_score),align="center",font = ("courier",28,"normal"))

      # Snake Moves by this function :    
      Main_move()
        
      #If snake collides with itself   
      if len(segments) > 0 :
            for j in segments :
                if j.distance(head) < 14 :
                    playsound(hit,block = False)
                    head.color("crimson")
                    for i in segments:
                        i.color("crimson")
                    turtle.update()
                    time.sleep(0.25)
                    head.goto(0,0)
                    head.color(headcol)
                    head.direction = "stop"
                    
                    #Hiding the Tail
                    
                    for i in segments :
                            i.hideturtle()
                    segments.clear()   
                    score = 0
                       
      time.sleep(delay)

## Defining how to play
      
def How_To_Play():
    
     def bac(x,y):
         if x >= -370 and x <= -290 :
             if y >= 305 and y <= 345 :
                 sc2.clearscreen()
                 Menu()
   
     sc2 = turtle.Screen()
     sc2.title("How To Play")
     sc2.setup(750,700)
     sc2.bgpic(bghtp)
     sc2.bgcolor("black")

     pen4 = turtle.Turtle()
     pen4.ht()
     pen4.speed(0)
     pen4.color("black","grey")
     pen4.up()
     pen4.goto(-370,305)
     pen4.down()
     pen4.pensize(5)
     
     pen4.begin_fill()
     pen4.fd(80)
     pen4.lt(90)
     pen4.fd(40)
     pen4.lt(90)
     pen4.fd(80)
     pen4.lt(90)
     pen4.fd(40)
     pen4.end_fill()

     pen4.up()

     pen5 = turtle.Turtle()
     pen5.up()
     pen5.ht()
     pen5.speed(0)
     pen5.goto(-330,312)
     pen5.write('Back',align = 'center',font = ("courier",15,"bold"))
     
     pen3 = turtle.Turtle()
     pen3.ht()
     pen3.speed(0)
     pen3.up()
     pen3.color("white")
     
     pen3.goto(0,290)
     pen3.write("How To Play??",align='center',font=("courier",40,"underline","bold"))

     pen3.goto(-210,250)
     pen3.write("Play:",align="right",font = ("Courier",27,"underline","bold"))

     pen3.goto(11,220)
     pen3.write("Use arrow keys or W,S,A,D keys For the Movement of Your Snake",align="center",font=('courier',13,"bold"))

     pen3.goto(-28,190)
     pen3.write("Tap P To Pause/Resume your Game (Only if you Want so)",align="center",font=('courier',13,"bold"))

     pen3.goto(-3,160)
     pen3.write("Tap 'Esc' To Return To the Main Menu (Only if you Want so)",align = "center",font=('courier',13,'bold'))

     pen3.goto(-5,130)
     pen3.write(">>To increase your score rapidly,eat Star Bonus within the Time limit",align="center",font=('courier',13,"italic","bold"))
     
     pen3.goto(0,105)
     pen3.write(">>Your Current Level,Score And Highscore will be Displayed in Real Time",align = "center",font=('courier',13,"italic","bold"))

     pen3.goto(-45,60)
     pen3.write("Game Settings:",align="right",font=("courier",25,"underline","bold"))

     pen3.goto(-95,25)
     pen3.write("Click on Option That you Want To Change",align="center",font=('courier',13,"bold"))

     pen3.goto(20,-5)
     pen3.write("Enter The Changes That you Want",align = "right",font=('courier',13,"bold"))

     pen3.goto(-70,-35)
     pen3.write("Playing with default settings is recommended",align="center",font=('courier',13,"bold"))

     pen3.goto(-80,-80)
     pen3.write("Game Level:",align="right",font=("courier",27,"underline","bold"))

     pen3.goto(-110,-120)
     pen3.write("Your Current Status will be Displayed",align="center",font=('courier',13,"bold"))
     
     pen3.goto(-59,-150)
     pen3.write("There are 3 Levels : 'Easy','Normal' and 'Hard'",align="center",font=('courier',13,"bold"))

     pen3.goto(-84,-180)
     pen3.write("Choose the level on which you wanna play. ",align="center",font=('courier',13,"bold"))

     pen3.goto(-29,-210)
     pen3.write("Each Level has Its Own High Score and Bonus Last time",align="center",font=('courier',13,"bold"))

     pen3.goto(10,-285)
     pen3.color("cyan")
     pen3.write("Now you know Everything about the game\nso,just enjoy the game..........",align="center",font=("courier",20,"italic","bold"))

     turtle.onscreenclick(bac)

##Defining Settings
         
def settings():
         
     def backTO():
         turtle.clearscreen()
         Menu()

     main_sc = turtle.Screen()
     main_sc.bgcolor("black")
     main_sc.title("Settings")
     main_sc.setup(700,700)
     main_sc.bgpic(settingsbg)
     
     pen8 = turtle.Turtle()
     pen8.ht()
     pen8.speed(0)
     pen8.color("black","grey")
     pen8.up()
     pen8.goto(-345,305)
     pen8.down()
     pen8.pensize(5)
     
     pen8.begin_fill()
     pen8.fd(80)
     pen8.lt(90)
     pen8.fd(40)
     pen8.lt(90)
     pen8.fd(80)
     pen8.lt(90)
     pen8.fd(40)
     pen8.end_fill()
     
     pen8.up()

     pen9 = turtle.Turtle()
     pen9.up()
     pen9.ht()
     pen9.speed(0)
     pen9.goto(-305,312)
     pen9.write('Back',align = 'center',font = ("courier",15,"bold"))

     def ch_headcolr():

              def rawhead():
                  
                    global headcol
                    global raw_headcol
                    
                    raw_headcol = turtle.textinput("Head Colour","The color that you entered is invalid \nplease try again :")
                    if raw_headcol != None :
                          raw_headcol = raw_headcol.lower()
                          try:
                                turtle.bgcolor(raw_headcol)
                                turtle.bgcolor('black')
                                sett[0] = raw_headcol 
                                headcol = sett[0]
                                with open("Settings.dat","wb") as z :
                                     pickle.dump(sett,z)
                          except:
                                rawhead()
                                
              global headcol
              global raw_headcol
              
              raw_headcol = turtle.textinput("Head Colour","Enter the Snake's Head Colour that You want :")
              if raw_headcol != None :
                    raw_headcol = raw_headcol.lower()
                              
                    try:
                          turtle.bgcolor(raw_headcol)
                          turtle.bgcolor('black')
                          sett[0] = raw_headcol 
                          headcol = sett[0]
                          with open("Settings.dat","wb") as z :
                                     pickle.dump(sett,z)
                    
                    except:
                          rawhead()
                          
     def ch_foodcolr():

              def rawfood():
                    global foodcol
                    global raw_foodcol
                    
                    raw_foodcol = turtle.textinput("Food Colour","The color that you entered is invalid \nplease try again :")
                    if raw_foodcol != None :
                          raw_foodcol = raw_foodcol.lower()
                          try:
                                turtle.bgcolor(raw_foodcol)
                                turtle.bgcolor('black')
                                sett[2] = raw_foodcol 
                                foodcol = sett[2]
                                with open("Settings.dat","wb") as z :
                                     pickle.dump(sett,z)
                          except:
                                rawfood()
           
              global foodcol
              global raw_foodcol
              
              raw_foodcol = turtle.textinput("Food Colour","Enter the Snake's Food Colour :")
              if raw_foodcol != None :
                        raw_foodcol = raw_foodcol.lower()
                              
                        try:
                             turtle.bgcolor(raw_foodcol)
                             turtle.bgcolor('black')
                             sett[2] = raw_foodcol 
                             foodcol = sett[2]
                             with open("Settings.dat","wb") as z :
                                     pickle.dump(sett,z)
                             
                        except:
                              rawfood()
                             
     def deflt_set():
              global headcol 
              global bgcol
              global foodcol 
              global tailcol
              
              def rawdeflt_set():
                       global headcol 
                       global bgcol
                       global foodcol 
                       global tailcol
                       
                       delft = turtle.textinput("Default Settings","You Entered an invalid option \nPlease choose from 'yes' or 'No':")
                       if delft != None :
                                delft = delft.lower()
                                
                                if delft == "yes" or deflt == "y" or deflt == "Y" or deflt == "YES":
                                      sett = ["white","black","red","grey"]
      
                                      headcol = sett[0]
                                      bgcol = sett[1]
                                      foodcol = sett[2]
                                      tailcol = sett[3]
                                  
                                      with open("Settings.dat","wb") as z :
                                             pickle.dump(sett,z)
                                             
                                elif delft == "no" or deflt == "n" or deflt == "N" or deflt == "NO":
                                      pass
    
                                else:
                                    rawdeflt_set()

              deflt = turtle.textinput("Default Settings","Do You Want Default Settings \n'yes' or 'No'")
              if deflt != None :
                          deflt = deflt.lower()
                              
                          if deflt == "yes" or deflt == "y" or deflt == "Y" or deflt == "Yes":
                                  sett = ["white","black","red","grey"]
      
                                  headcol = sett[0]
                                  bgcol = sett[1]
                                  foodcol = sett[2]
                                  tailcol = sett[3]
                                  
                                  with open("Settings.dat","wb") as z :
                                         pickle.dump(sett,z)
                                         
                          elif deflt == "no" or deflt == "n" or deflt == "N" or deflt == "NO":
                                  pass

                          else:
                              rawdeflt_set()
     def ch_bgcolr():
           
              def rawbg():
                    global bgcol
                    global raw_bgcol
                    raw_bgcol = turtle.textinput("BackGround Colour","The colour You Entered is invalid \nplease try again :")
                    if raw_bgcol != None :
                                      raw_bgcol = raw_bgcol.lower()
                                          
                                      try:
                                            
                                            turtle.bgcolor(raw_bgcol)
                                            turtle.bgcolor('black')
                                            sett[1] = raw_bgcol 
                                            bgcol = sett[1]
                                            with open("Settings.dat","wb") as z :
                                                 pickle.dump(sett,z) 

                                      except:
                                            rawbg()
              global bgcol
              global raw_bgcol
              raw_bgcol = turtle.textinput("BackGround Colour","Enter Background Colour of your Choice :")
              if raw_bgcol != None :
                          raw_bgcol = raw_bgcol.lower()
                              
                          try:
                                
                                turtle.bgcolor(raw_bgcol)
                                turtle.bgcolor('black')
                                sett[1] = raw_bgcol 
                                bgcol = sett[1]
                                with open("Settings.dat","wb") as z :
                                                 pickle.dump(sett,z) 

                          except:
                                rawbg()

     def ch_tailcolr():
           
              def rawtail():
                    global tailcol
                    global raw_tailcol
                    raw_tailcol = turtle.textinput("Tail Colour","The colour You Entered is invalid \nplease try again :")
                    if raw_tailcol != None :
                          raw_tailcol = raw_tailcol.lower()
                              
                          try:
                                turtle.bgcolor(raw_tailcol)
                                turtle.bgcolor('black')
                                sett[3] = raw_tailcol 
                                tailcol = sett[3]
                                with open("Settings.dat","wb") as z :
                                                 pickle.dump(sett,z) 

                          except:
                                rawtail()

              global tailcol
              global raw_tailcol
              raw_tailcol = turtle.textinput("Tail Colour","Enter the Snake's Tail Colour :")
              if raw_tailcol != None :
                    raw_tailcol = raw_tailcol.lower()
                              
                    try:
                          turtle.bgcolor(raw_tailcol)
                          turtle.bgcolor('black')
                          sett[3] = raw_tailcol 
                          tailcol = sett[3]
                          with open("Settings.dat","wb") as z :
                                        pickle.dump(sett,z)

                    except:
                          rawtail()

     writ = turtle.Turtle()
     writ.up()
     writ.ht()
     writ.speed(0)
     writ.color("dark slate blue")

     writ.goto(0,295)
     writ.write("Settings",align = "center",font=("courier",37,"bold","underline"))
     writ.color("black")
     
     setting_bloc= turtle.Turtle()
     setting_bloc.ht()
     setting_bloc.color("black","grey")
     setting_bloc.speed(0)
     setting_bloc.up()
     setting_bloc.down()
     setting_bloc.width(5)   # or turtle.pensize(<argument>)

     def sett_bloc():
         setting_bloc.down()
         setting_bloc.begin_fill()
         setting_bloc.fd(150)
         setting_bloc.rt(90)
         setting_bloc.fd(50)
         setting_bloc.rt(90)
         setting_bloc.fd(300)
         setting_bloc.rt(90)
         setting_bloc.fd(50)
         setting_bloc.rt(90)
         setting_bloc.fd(150)
         setting_bloc.end_fill()
         
     setting_bloc.up()
     setting_bloc.goto(0,115)
     setting_bloc.down()
     
     sett_bloc()

     writ.goto(0,80)
     writ.write("Change head Colour",align="center",font=("courier",14,"bold"))
     setting_bloc.up()
     setting_bloc.goto(0,-75)
     setting_bloc.pendown()
     
     sett_bloc()
     
     writ.goto(0,-110)
     writ.write("Change Food colour",align = "center",font=("courier",14,"bold"))


     setting_bloc.up()
     setting_bloc.goto(0,20)
     setting_bloc.pendown()

     sett_bloc()

     writ.goto(0,-15)
     writ.write("Change Tail Colour",align = "center",font=("courier",14,"bold"))


     setting_bloc.up()
     setting_bloc.goto(0,-165)
     setting_bloc.pendown()

     sett_bloc()

     writ.goto(0,-200)
     writ.write("Default Settings!!",align = "center",font=("courier",14,"bold"))


     setting_bloc.up()
     setting_bloc.goto(0,205)
     setting_bloc.pendown()

     sett_bloc()

     writ.goto(0,170)
     writ.write("Change Background Colour",align = "center",font=("courier",14,"bold"))
     
     turtle.tracer(0,0)

     def settt(x,y):
         if x >= -150 and x <= 150 :
             if y >= 65 and y <= 115  :

                        ch_headcolr()
                      
             elif y >= -125 and y <= -75:

                        ch_foodcolr()
                      
             elif y >= -30 and y <= 20 :

                        ch_tailcolr()
                      
             elif y >= 155 and y <= 205  :
                                 
                        ch_bgcolr()
                      
             elif y >= -215 and y <= -165 :
                              
                        deflt_set()
                      
         if x >= -345 and x <= -265 :
                 if y >= 305 and y <= 345 :
                     
                     main_sc.clearscreen()
                     Menu()
                 
     main_sc.onscreenclick(settt)

##Defining Levels
         
def Level():
    global level
    global hs  
    global delay
    global high_score

    def bacTo():
         turtle.clearscreen()
         Menu()

    sc = turtle.Screen()
    sc.title("Levels")
    sc.setup(width=700,height=575)
    sc.bgcolor("silver")
    
    pen = turtle.Turtle()
    pen.pensize(10)
    pen.up()
    pen.speed(0)
    pen.ht()
    pen.color("black")

    penA = turtle.Turtle()
    penA.ht()
    penA.speed(0)
    penA.up()
    penA.color("black","grey")
    penA.goto(-345,245)
    penA.down()
    penA.pensize(5)
     
    penA.begin_fill()
    penA.fd(80)
    penA.lt(90)
    penA.fd(40)
    penA.lt(90)
    penA.fd(80)
    penA.lt(90)
    penA.fd(40)
    penA.end_fill()
    penA.up()

    penB = turtle.Turtle()
    penB.up()
    penB.ht()
    penB.speed(0)
    penB.goto(-305,252)
    penB.write('Back',align = 'center',font = ("courier",15,"bold"))

    pen.goto(5,170)
    pen.write("Levels & High scores",align = "center",font = ("courier",30,"underline",'bold'))

    pen.goto(-20,80)
    pen.write("High Score",align = "center",font = ("courier",24,"underline",'bold'))

    pen.goto(250,80)
    pen.write("Level",align = "center",font = ("courier",24,"underline",'bold'))

    pen.goto(-270,10)
    pen.write("Easy",align = "center",font = ("courier",24,'underline','bold'))
    pen.goto(-20,10)
    pen.write(hs[0],align = "center",font = ("courier",24,'bold'))

    pen.goto(-270,-80)
    pen.write("Normal",align = "center",font = ("courier",24,'underline','bold'))
    pen.goto(-20,-80)
    pen.write(hs[1],align = "center",font = ("courier",24,'bold'))

    pen.goto(-270,-170)
    pen.write("Hard",align = "center",font = ("courier",24,'underline','bold'))
    pen.goto(-20,-170)
    pen.write(hs[2],align = "center",font = ("courier",24,'bold'))

    def levelch(easycol,normalcol,hardcol):
        
        turtle.tracer(0)
        o= turtle.Turtle()
        o.ht()
        o.speed(0)
        o.up()
        o.width(5)
        
        level_bloc= turtle.Turtle()
        level_bloc.ht()
        level_bloc.color("black","grey")
        level_bloc.speed(0)
        level_bloc.up()
        level_bloc.down()
        level_bloc.width(5)   # or turtle.pensize(<argument>)

        def block(x,y=50):
             level_bloc.down()
             level_bloc.begin_fill()
             level_bloc.fd(x)
             level_bloc.rt(90)
             level_bloc.fd(y)
             level_bloc.rt(90)
             level_bloc.fd(x*2)
             level_bloc.rt(90)
             level_bloc.fd(y)
             level_bloc.rt(90)
             level_bloc.fd(x)
             level_bloc.end_fill()

        level_bloc.color("black",easycol)
        
        level_bloc.up()
        level_bloc.goto(250,55)
        level_bloc.down()
        
        block(60,45)

        o.goto(250,17)
        o.write("Easy",align = 'center',font= ("courier",20,"bold"))

        level_bloc.color("black",normalcol)
        
        level_bloc.up()
        level_bloc.goto(250,-35)
        level_bloc.down()
        
        block(60,45)

        o.goto(253,-74)
        o.write("Normal",align = 'center',font= ("courier",20,"bold"))

        level_bloc.color("black",hardcol)
        
        level_bloc.up()
        level_bloc.goto(250,-125)
        level_bloc.down()
        
        block(60,45)

        level_bloc.color("black","grey")
        o.goto(250,-165)
        o.write("Hard",align = 'center',font= ("courier",20,"bold"))
        
        turtle.update()
    
    if level == "normal" :        
        levelch("grey","crimson","grey")
        
    elif level == "easy" :
        levelch("crimson","grey","grey")
        
    else:
        levelch("grey","grey","crimson")
        
    def change(x,y):
        global level
        global hs  
        global delay
        global high_score
        global goal_tm
        
        turtle.tracer(0)    

        if x >= 210 and x <= 310 :
            if y >= 10 and y <= 55 :
              levelch('crimson','grey','grey')
              level = "easy"
              delay = 0.09
              goal_tm = 4
              high_score = hs[0]
              
        if x >= 210 and x <= 310 :
            if y >= -80 and y <= -35 :
              levelch('grey','crimson','grey')
              level = "normal"
              delay = 0.08
              goal_tm = 3
              high_score = hs[1]

        if x >= 210 and x <= 310 :
            if y >= -170 and y <= -125 :
              levelch('grey','grey','crimson')
              level = "hard"
              delay = 0.06
              goal_tm = 2
              high_score = hs[2]      
                
        if x >= -345 and x <= -265 :
                 if y >= 245 and y <= 285 :

                     turtle.clearscreen()  #To Exit 
                     Menu()
                 
    sc.onscreenclick(change)

##Defining Credits
        
def Credits():
     
   def baK(x,y):
      if x >= -245 and x <= -165 :
          if y >= 155 and y <= 195 :
                    Crd_sc.clearscreen()
                    Menu()

   Crd_sc = turtle.Screen()
   Crd_sc.setup(width=500,height=400)
   Crd_sc.bgcolor("light grey")
   Crd_sc.title("Credits!!")

   pen7 = turtle.Turtle()
   pen7.ht()
   pen7.speed(0)
   pen7.up()
   pen7.color("black","grey")
   pen7.goto(-245,155)
   pen7.down()
   pen7.pensize(5)

   pen7.begin_fill()
   pen7.fd(80)
   pen7.lt(90)
   pen7.fd(40)
   pen7.lt(90)
   pen7.fd(80)
   pen7.lt(90)
   pen7.fd(40)
   pen7.end_fill()

   pen7.up()

   pen6 = turtle.Turtle()
   pen6.up()
   pen6.ht()
   pen6.speed(0)
   pen6.goto(-205,162)
   pen6.write('Back',align = 'center',font = ("courier",15,"bold"))

   wrt = turtle.Turtle()
   wrt.ht()
   wrt.speed(0)
   wrt.up()

   turtle.onscreenclick(baK)

   wrt.goto(0,140)
   wrt.write("Credits",align = "center",font=("courier",30,"underline","bold"))

   wrt.goto(0,70)
   wrt.write("Name : Siddhartha Varshney",align = "center",font=("courier",18,"italic","bold"))

   wrt.goto(0,10)
   wrt.write("Vellore Institute of Technology",align = "center",font=("courier",15,"italic","bold"))

   wrt.goto(0,-50)
   wrt.write("RegNo : 20MID0186",align = "center",font=("courier",18,"italic","bold"))

   wrt.goto(0,-130)
   wrt.color("purple")
   wrt.write("Thanks For Playing!!!",align = "center",font=("courier",28,"italic","bold"))
     
def Menu():
   main_sc = turtle.Screen()
   main_sc.bgcolor("white")
   main_sc.setup(700,700)
   main_sc.title("Main Menu")
   main_sc.bgcolor("black")
   main_sc.bgpic(bg)

   writ = turtle.Turtle()
   writ.up()
   writ.ht()
   writ.speed(0)
   writ.color("dark slate blue")

   writ.goto(0,295)
   writ.write("Snake Game",align = "center",font=("courier",34,"bold",'underline'))
   writ.color("black")

   main_bloc= turtle.Turtle()
   main_bloc.ht()
   main_bloc.color("black","grey")
   main_bloc.speed(0)
   main_bloc.up()
   main_bloc.down()
   main_bloc.width(5)   # or turtle.pensize(<argument>)

   def bloc():
      main_bloc.down()
      main_bloc.begin_fill()
      main_bloc.fd(100)
      main_bloc.rt(90)
      main_bloc.fd(50)
      main_bloc.rt(90)
      main_bloc.fd(200)
      main_bloc.rt(90)
      main_bloc.fd(50)
      main_bloc.rt(90)
      main_bloc.fd(100)
      main_bloc.end_fill()

   main_bloc.up()
   main_bloc.goto(0,105)
   main_bloc.down()

   bloc()

   writ.goto(0,70)
   writ.write("Play",align="center",font=("courier",14,"bold"))

   main_bloc.up()
   main_bloc.goto(0,-85)
   main_bloc.down()

   bloc()

   writ.goto(0,-120)
   writ.write("How To Play",align = "center",font=("courier",14,"bold"))


   main_bloc.up()
   main_bloc.goto(0,10)
   main_bloc.down()

   bloc()

   writ.goto(0,-25)
   writ.write("Settings",align = "center",font=("courier",14,"bold"))


   main_bloc.up()
   main_bloc.goto(0,-175)
   main_bloc.pendown()

   bloc()

   writ.goto(0,-210)
   writ.write("Credits",align = "center",font=("courier",14,"bold"))


   main_bloc.up()
   main_bloc.goto(0,195)
   main_bloc.down()

   bloc()

   writ.goto(0,160)
   writ.write("Levels",align = "center",font=("courier",14,"bold"))

   main_bloc.up()
   main_bloc.goto(0,-175)
   main_bloc.down()

   ###Finding the coordinates of the Click on The Main Menu

   def coor(x,y):
      
     if x >= -100 and x <= 100 :
         
         if y >= 55 and y <= 105  :

                 turtle.clearscreen()
                 Play()
        
         elif y >= -135 and y <= -85:

                 turtle.clearscreen()
                 How_To_Play()

         elif y >= -40 and y <= 10 :

                 turtle.clearscreen()
                 settings()
             
         elif y >= 145 and y <= 195  :

                 turtle.clearscreen()
                 Level()                 

         elif y >= -225 and y <= -175 :

                turtle.clearscreen()
                Credits()

   main_sc.onscreenclick(coor)
   turtle.done()

# let's run it after all :

if "__main__" == __name__ :
                            Menu()
