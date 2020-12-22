#Examples
speed=8
import random
import time
speed1=2
speed2=3
speed3=4
y1=100
y2=random.randint(100,450)
x2=1000
y3=random.randint(450, 900)
x3=1000
y4=random.randint(100, 450)
x4=1000
y5=random.randint(450, 900)
x5=1000
y6=random.randint(100, 450)
x6=1000
y7=random.randint(450, 900)
x7=1000
y8=random.randint(100, 450)
x8=1000
y9=random.randint(450, 900)
x9=1000
y10=random.randint(100, 450)
x10=1000
y11=random.randint(450, 900)
x11=1000
y12=random.randint(100, 450)
x12=1000
y13=random.randint(450, 900)
x13=1000
y14=random.randint(100, 450)
x14=1000
y15=random.randint(450, 900)
x15=1000
y16=random.randint(100,450)
x16=1000
y17=random.randint(450, 900)
x17=1000
y18=random.randint(100, 450)
x18=1000
y19=random.randint(450, 900)
x19=1000
y20=random.randint(100, 450)
x20=1000
y21=random.randint(450, 900)
x21=1000
y22=random.randint(100, 450)
x22=1000
y23=random.randint(450, 900)
x23=1000
y24=random.randint(100, 450)
x24=1000
y25=random.randint(450, 900)
x25=1000
y26=random.randint(100, 450)
x26=1000
y27=random.randint(450, 900)
x27=1000
y28=random.randint(100, 450)
x28=1000
y29=random.randint(450, 900)
x29=1000
y30=random.randint(100, 450)
x30=1000
y0=-10000
speed0=1
speed01=10000



def setup ():
    size(1000,1000)
    background(100)
def keyPressed():
    global y1

    
    #z:shadowraze 
    #x:shadowraze
    #c:shadowraze
    if key=='w':
        y1=y1-speed
    if key=='s':
        y1=y1+speed
    if x25>1000:
        if key=='r':                                                                                             
            exit()
    if key=='ESKAPE':
        exit(0)
    if y1<50:
        y1=y1+speed
    if y1>950:
        y1=y1-speed

    
def draw():
    global game_over,x1,y0,speed0
    y0=y0+speed0
    square(1,y0,1)
    background(0,0,0)
    fill(255,255,255)
    textSize(50)
    text("New game", width/2-140, 100)
    textSize(30)
    fill(255,0,0)
    rect(width/2-175,150,340,100)
    fill(255,255,255)
    text("Press 'F' to play",width/2-125,200)
    
    
    
    
    
    
    
    

    
    if key=='f':
        speed0=speed01
    if y0>0:
        game_over=False
        if (game_over == False) :
            if y1 in range(50,950):
                background(0,102,102)
                noStroke()
                fill(255,255,255)
                circle(50,y1,100)
            global x1,x2,x3,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30
            x2=x2-speed1
            noStroke()
            fill(255,128,0)
            square(x2,y2,100)
            if x2<850:
                x3=x3-speed1
                square(x3,y3,100)
                if x3<850:
                    x4=x4-speed1
                    square(x4,y4,100)
                    if x4<850:
                        x5=x5-speed1
                        square(x5,y5,100)
                        if x5<850:
                            x6=x6-speed1
                            square(x6,y6,100)
                            if x6<850:
                                x7=x7-speed1
                                square(x7,y7,100)
                                if x7<850:
                                    x8=x8-speed1
                                    square(x8,y8,100)
                                    if x8<850:
                                        x9=x9-speed1
                                        square(x9,y9,100)
                                        if x9<850:
                                            x10=x10-speed1
                                            square(x10,y10,100)
                                            if x10<850: 
                                                x12=x12-speed2 
                                                square(x12,y12,100) 
                                                if x12<850: 
                                                    x13=x13-speed2 
                                                    square(x13,y13,100)
                                                    if x13<850: 
                                                        x14=x14-speed2 
                                                        square(x14,y14,100)
                                                        if x14<850: 
                                                            x15=x15-speed2 
                                                            square(x15,y15,100)
                                                            if x15<850: 
                                                                x16=x16-speed2 
                                                                square(x16,y16,100) 
                                                                if x16<850: 
                                                                    x17=x17-speed2 
                                                                    square(x17,y17,100) 
                                                                    if x17<850: 
                                                                        x18=x18-speed2 
                                                                        square(x18,y18,100) 
                                                                        if x18<850: 
                                                                            x19=x19-speed2 
                                                                            square(x19,y19,100) 
                                                                            if x19<850: 
                                                                                x20=x20-speed2 
                                                                                square(x20,y20,100) 
                                                                                if x20<850:
                                                                                    x21=x21-speed3 
                                                                                    square(x21,y21,100) 
                                                                                    if y21<850: 
                                                                                        x22=x22-speed3 
                                                                                        square(x22,y22,100) 
                                                                                        if x22<850: 
                                                                                            x23=x23-speed3 
                                                                                            square(x23,y23,100) 
                                                                                            if x23<850: 
                                                                                                x24=x24-speed3 
                                                                                                square(x24,y24,100) 
                                                                                                if x24<850: 
                                                                                                    x25=x25-speed3 
                                                                                                    square(x25,y25,100)
                                                                                                    if y25<850: 
                                                                                                        x26=x26-speed3 
                                                                                                        square(x26,y26,100)
                                                                                                        if x26<850: 
                                                                                                            x27=x27-speed3 
                                                                                                            square(x27,y27,100)
                                                                                                            if x27<850: 
                                                                                                                x28=x28-speed3 
                                                                                                                square(x28,y28,100)
                                                                                                                if x28<850: 
                                                                                                                    x29=x29-speed3 
                                                                                                                    square(x29,y29,100)
                                                                                                                    if x29<850: 
                                                                                                                        x30=x30-speed3 
                                                                                                                        square(x30,y30,100)
                                                                                                                        if x30<0:
                                                                                                                            textSize(60)
                                                                                                                            filter(BLUR, 5)
                                                                                                                            fill(255,255,255)         
                                                                                                                            stroke(255,255,255)
                                                                                                                            text("GAME OVER", width/2-125, 300)
                                                                                                                            text("win", width/2-350, 375)
                                                                                                                            fill(200,200,200)
                                                                                                                            stroke(200,200,200)
                                                                                                                            textSize(20)
                                                                                                                            text("Press 'r' to exit game", width/2-100, 325)
                                                                                                                            fill(237,204,17)
                                                                                                                            stroke(237,204,17)
                                                                                                                            filter(GRAY)
                                                                                                                            noLoop()    
            fill(255,255,255)                                                                                               
            if x2 in range(0,200):                            
                if y2 in range(y1-50,y1+50):
                        game_over =  True
            if x3 in range(0,100):
                if y3 in range(y1-50,y1+50):
                        game_over =  True
            if x4 in range(0,100):                            
                if y4 in range(y1-50,y1+50):
                    game_over =  True
            if x5 in range(0,100):                            
                if y5 in range(y1-50,y1+50):
                    game_over =  True
            if x6 in range(0,100):                            
                if y6 in range(y1-50,y1+50):
                    game_over =  True
            if x7 in range(0,100):                            
                if y7 in range(y1-50,y1+50):
                    game_over =  True
            if x8 in range(0,100):                            
                if y8 in range(y1-50,y1+50):
                    game_over =  True
            if x9 in range(0,100):                            
                if y9 in range(y1-50,y1+50):
                    game_over =  True
            if x10 in range(0,100):                            
                if y10 in range(y1-50,y1+50):
                    game_over =  True
            if x11 in range(0,100):                            
                if y11 in range(y1-50,y1+50):
                    game_over =  True
            if x12 in range(0,100):                            
                if y12 in range(y1-50,y1+50):
                    game_over =  True
            if x13 in range(0,100):                            
                if y13 in range(y1-50,y1+50):
                    game_over =  True
            if x14 in range(0,100):                            
                if y14 in range(y1-50,y1+50):
                    game_over =  True
            if x15 in range(0,100):                            
                if y15 in range(y1-50,y1+50):
                    game_over =  True
            if x16 in range(0,100):                            
                if y16 in range(y1-50,y1+50):
                    game_over =  True
            if x17 in range(0,100):                            
                if y17 in range(y1-50,y1+50):
                    game_over =  True
            if x18 in range(0,100):                            
                if y18 in range(y1-50,y1+50):
                    game_over =  True
            if x19 in range(0,100):                            
                if y19 in range(y1-50,y1+50):
                    game_over =  True
            if x20 in range(0,100):                            
                if y20 in range(y1-50,y1+50):
                    game_over =  True
            if x21 in range(0,100):                            
                if y21 in range(y1-50,y1+50):
                    game_over =  True
            if x22 in range(0,100):                            
                if y22 in range(y1-50,y1+50):
                    game_over =  True
            if x23 in range(0,100):                            
                if y23 in range(y1-50,y1+50):
                    game_over =  True
            if x24 in range(0,100):                            
                if y24 in range(y1-50,y1+50):
                    game_over =  True
            if x25 in range(0,100):                            
                if y25 in range(y1-50,y1+50):
                    game_over =  True
            if x26 in range(0,100):                            
                if y26 in range(y1-50,y1+50):
                    game_over =  True
            if x27 in range(0,100):                            
                if y27 in range(y1-50,y1+50):
                    game_over =  True
            if x28 in range(0,100):                            
                if y28 in range(y1-50,y1+50):
                    game_over =  True                                                                                                
            if x29 in range(0,100):                            
                if y29 in range(y1-50,y1+50):
                    game_over =  True                                                                                                
            if x30 in range(0,100):                            
                if y30 in range(y1-50,y1+50):
                    game_over =  True       
                                                                                                                 
            if  (game_over == True):
                textSize(60)
                filter(BLUR, 5)
                fill(255,255,255)         
                stroke(255,255,255)
                text("G   A   M   E       O   V   E   R", width/2-425, 300)
                fill(200,200,200)
                stroke(200,200,200)
                textSize(20)
                fill(0, 255, 127)
                text("Escape  to exit game.", width/2-100, 325)
                fill(0, 255, 127)
                stroke(237,204,17)
                filter(GRAY)
                noLoop()
