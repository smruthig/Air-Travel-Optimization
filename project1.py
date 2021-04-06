import msvcrt
import pandas
from graphics import *
import time
from math import *


    
def input1(self,p,x):

            chk=-1
            #self.name=input()
            inputBox = Entry(Point(500,p), 30)

            inputBox.setFill("white")
            inputBox.draw(win)
            win.getMouse()
            self.name=inputBox.getText()
            print(self.name)
                    
            temp = pandas.read_csv('cities.csv')
            for i,rows in temp.iterrows():
                #print(temp.iloc[i,0])
                if temp.iloc[i,0] == self.name:
                    
                            chk+=1
                            #print(temp.name)
                            self.lon=temp.iloc[i,2]
                            self.lat=temp.iloc[i,1]
                            self.x=temp.iloc[i,3]
                            self.y=temp.iloc[i,4]
                            #print(self.x,self.y)
                            
                            
			
		
	
            if chk==-1:

                    label2 = Text(Point(500, p+50), "City not found. Please re-enter. Click to continue")
                    label2.setSize(20)
                    label2.setTextColor('blue')
                    label2.draw(win)
                    win.getMouse()
                    label2.undraw()
                    inputBox.undraw()
                    x.undraw()
                    departure()
                    
            label3 = Text(Point(500, p+50), "Click to continue")
            label3.setSize(20)
            label3.setTextColor('blue')
            label3.draw(win)
            win.getMouse()
            inputBox.undraw()
            label3.undraw()
            
            

           


def input2(self,p,x):

            chk=-1
            #self.name=input()
            inputBox = Entry(Point(500,p), 30)

            inputBox.setFill("white")
            inputBox.draw(win)
            win.getMouse()
            self.name=inputBox.getText()
            print(self.name)
                    
            temp = pandas.read_csv('cities.csv')
            for i,rows in temp.iterrows():
                #print(temp.iloc[i,0])
                if temp.iloc[i,0] == self.name:
                    
                            chk+=1
                            #print(temp.name)
                            self.lon=temp.iloc[i,2]
                            self.lat=temp.iloc[i,1]
                            self.x=temp.iloc[i,3]
                            self.y=temp.iloc[i,4]
                            #print(self.x,self.y)
                            
	
            if chk==-1:

                    label2 = Text(Point(500, p+50), "City not found. Please re-enter. Click to continue")
                    label2.setSize(20)
                    label2.setTextColor('blue')
                    label2.draw(win)
                    win.getMouse()
                    label2.undraw()
                    inputBox.undraw()
                    x.undraw()
                    arrival()
                    
            label3 = Text(Point(500, p+50), "Click to continue")
            label3.setSize(20)
            label3.setTextColor('blue')
            label3.draw(win)
            win.getMouse()
            inputBox.undraw()
            label3.undraw()
            

                

class City:

            def __init__(self,nam,lt,ln,locx,locy):
                    
                            self.lon=ln
                            self.lat=lt
                            self.x=locx
                            self.y=locy
                            self.name=nam
                            self.reltime=0

            def __init__(self):
                    
                            self.lat=self.lon=self.reltime=self.x=self.y=0
                            self.name=""

            def inputa(self,p,x): #input arrival
                return input1(Arr,p,x)
                
                
                

            def inputb(self,p,x): #input departure
                return input2(Dep,p,x)
                
                

Arr =City()
Mid =City()
Dep = City()
temp = City()
Singapore = City()
Beijing =City()
Dubai = City()
NewYork = City() #objects for transit city details

def create():
    temp = pandas.read_csv('cities.csv')
    for i,rows in temp.iterrows():
                if temp.iloc[i,0] == "Singapore":
                    
                            Singapore.lon=temp.iloc[i,2]
                            Singapore.lat=temp.iloc[i,1]
                            Singapore.x=temp.iloc[i,3]
                            Singapore.y=temp.iloc[i,4]
                            
                if temp.iloc[i,0] == "New York":
                    
                            NewYork.lon=temp.iloc[i,2]
                            NewYork.lat=temp.iloc[i,1]
                            NewYork.x=temp.iloc[i,3]
                            NewYork.y=temp.iloc[i,4]
                            
                if temp.iloc[i,0] == "Dubai":
                    
                            Dubai.lon=temp.iloc[i,2]
                            Dubai.lat=temp.iloc[i,1]
                            Dubai.x=temp.iloc[i,3]
                            Dubai.y=temp.iloc[i,4]

                if temp.iloc[i,0] == "Beijing":
                    
                            Beijing.lon=temp.iloc[i,2]
                            Beijing.lat=temp.iloc[i,1]
                            Beijing.x=temp.iloc[i,3]
                            Beijing.y=temp.iloc[i,4]
                            
R=6371
		 
def abs (n):

    if n>=0:
        return n
    else:
        return (n*(-1))



def departure(): #to input departure location details
	
	
            win.setBackground("black")
            label = Text(Point(500, 200), "Enter departure location and then click mouse")
            label.setTextColor('blue')
            label.setSize(20)
            label.draw(win)
            Dep.inputb(300,label)
            label.undraw()
            print(Dep.lat)


def arrival(): #to input arrival location details

	
            win.setBackground("black")
            label = Text(Point(500, 200), "Enter arrival location and then click mouse")
            label.setTextColor('blue')
            label.setSize(20)
            label.draw(win)
            Arr.inputa(300,label)
            label.undraw()
            print(Arr.lat)

def drawroute(D,A): #to draw route on world map using slope between to coordinates

            print(A.x,D.x)
            dx = int(A.x) - int(D.x)
            dy = int(A.y) - int(D.y)
            steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
            Xinc = dx / steps
            Yinc = dy / steps
            X = int(D.x)
            Y = int(D.y)
            l=[]
            for i in range(0,steps+1):
            
                    circle = Circle(Point(X, Y-20), 2)
                    circle.setOutline('red')
                    circle.setFill('red')
                    l.append(circle)
                    circle.draw(win)
                    X += Xinc
                    Y += Yinc
                    time.sleep(0.02)
            time.sleep(5)
            return l

	


def load():#loading screen
    
      label=Text(Point(win.getWidth()/2,200),"Loading...")
      label.setTextColor("blue")
      label.setSize(20)
      label.draw(win)
      rect = Rectangle(Point(550, 300), Point(750,348))
      rect.setFill("white")
      rect.draw(win)
      for i in range (20):
            
            rect1 = Rectangle(Point(552+(i*10), 302), Point(560+(i*10), 348))
            rect1.setFill("blue")
            rect1.draw(win)
            time.sleep(0.05)
            
      win.setBackground('black')
      label.undraw()
      for i in range (20):
             
            rect1 = Rectangle(Point(552+(i*10), 302), Point(560+(i*10), 348))
            rect1.setFill("black")
            rect1.draw(win)
      rect.undraw()
        
            

def loadmaps(): #to load background map
	#
	image=Image(Point(1350/2,800/2),"world-map.gif")
	image.draw(win)
	return image
	



def citylist(): #to print list of cities available
	#
	image=Image(Point(1350/2,700/2),"citynames.gif")
	image.draw(win)
	keyString = win.getKey()

	image.undraw()


def start():#first screen UI


  image=Image(Point(1350/2,800/2),"maps.gif")
  image.draw(win)
  image1=Image(Point(710,400),"findyourroute.gif")
  image1.draw(win)
  image2=Image(Point(683,575),"clickhere.gif")
  image2.draw(win)
  p=win.getMouse()
  #print(p.x,p.y)
  if p.x>600 and p.y>534 and p.x<765 and p.y<605:
    #print("A")
    win.setBackground('black')
    image.undraw()
    image1.undraw()
    image2.undraw()
    load()
    citylist()
    win.setBackground('black')
    load()
    departure()
    arrival()
 



def distance(lata,latb,lona,lonb): #to find distance between two cities on earth

    lat1=radians(lata)
    lat2=radians(latb)
    lon1=radians(lona)
    lon2=radians(lonb)
    difflat=lat1-lat2
    difflon=lon1-lon2
    a=fabs(sin(difflat/2)*sin(difflat/2)+cos(lat1)*cos(lat2)*sin(difflon/2)*sin(difflon/2))
    c=2*atan2(2*sqrt(a),sqrt((1-a)))
    d=R*c
    return d


def min(a,b):
    if a<b:
        return a
    else:
        return b


    
def endscreen():  

    win.setBackground('black')
    img = Image(Point(1350/2,800/2),"maps.gif")
    img.draw(win)
    img1 = Image(Point(710,400),"findyourroute.gif")
    img1.draw(win)
    img2 = Image(Point(460,575),"newroute.gif")
    img2.draw(win)
    img3 = Image(Point(875,575),"exit.gif")
    img3.draw(win)
    p=win.getMouse()
    if p.x > 320 and p.x < 600 and p.y>530 and p.y<620:

                    win.setBackground('black')
                    img.undraw()
                    img1.undraw()
                    img2.undraw()
                    img3.undraw()
                    load()
                    citylist()
                    win.setBackground('black')
                    load()
                    departure()
                    arrival()
                    findroute()
                    
    elif p.x > 750 and p.x < 1000 and p.y>530 and p.y<620:

        win.close()
  


def findroute(): # to find route and decide if direct flight or transit flight and transit city location

    
    #Arr is an object of class city
        d=distance(Arr.lat,Dep.lat,Arr.lon,Dep.lon)
        d1=distance(Arr.lat,Dubai.lat,Arr.lon,Dubai.lon)
        d2=distance(Dep.lat,Dubai.lat,Dep.lon,Dubai.lon)
        s1=distance(Arr.lat,Singapore.lat,Arr.lon,Singapore.lon)
        s2=distance(Dep.lat,Singapore.lat,Dep.lon,Singapore.lon)
        n1=distance(Arr.lat,NewYork.lat,Arr.lon,NewYork.lon)
        n2=distance(Dep.lat,NewYork.lat,Dep.lon,NewYork.lon)
        b1=distance(Arr.lat,Beijing.lat,Arr.lon,Beijing.lon)
        b2=distance(Dep.lat,Beijing.lat,Dep.lon,Beijing.lon)
        #print(d," ",d1," ",d2," ",n1," ",n2," ",s1," ",s2)
        if d<=d1+d2 and d<=s1+s2 and d<=b1+b2 and d<=n1+n2 and d<15000:
         
            print("Direct flight")
            win.setBackground('black')
            s="DIRECT FLIGHT"  
            label=Text(Point(1350/2,200),s)
            label.setSize(20)
            label.setTextColor('blue')
            label.draw(win)
            label1=Text(Point(1350/2,300),'Press enter to view route')
            label1.setSize(20)
            label1.setTextColor('blue')
            label1.draw(win)
            win.getKey()
            win.setBackground('black')
            label.undraw()
            label1.undraw()
            image=loadmaps()
            print(Arr.x,Dep.x)
            #time.sleep(7)
            l=drawroute(Dep, Arr)
            for i in l:
                i.undraw()
            time.sleep(7)
            image.undraw()
            endscreen()

         
        elif d1+d2<s1+s2 and d1+d2<b1+b2 and d1+d2<n1+n2:
         
               #A:
                if str.lower(Dep.name)!="dubai" and str.lower(Arr.name)!="dubai":
              
                    print("Via Dubai \n")
                    win.setBackground('black')
                    s="FLIGHT VIA DUBAI"
                    label=Text(Point(1350/2,200),s)
                    label.setSize(20)
                    label.setTextColor('blue')
                    label.draw(win)
                    label1=Text(Point(1350/2,300),'Press enter to view route')
                    label1.setSize(20)
                    label1.setTextColor('blue')
                    win.getKey()
                    win.setBackground('black')
                    label.undraw()
                    label1.undraw()
                    loadmaps()
                    l1=drawroute(Dep,Dubai)
                    l2=drawroute(Dubai,Arr)
                    time.sleep(7)
                    for i in l1:
                        i.undraw()
                    for i in l2:
                        i.undraw()
                    endscreen()
              
                else:
                #goto B
                  pass


         

        elif s1+s2<d1+d2 and s1+s2<b1+b2 and s1+s2<n1+n2:
           
                #B:
                if str.lower(Dep.name)!="singapore" and str.lower(Arr.name)!="singapore":
                
                    print("Via Singapore \n")
                    win.setBackground('black')
                    s="FLIGHT VIA SINGAPORE"
                    label=Text(Point(1350/2,200),s)
                    label.setSize(20)
                    label.setTextColor('blue')
                    label.draw(win)
                    label1=Text(Point(1350/2,300),'Press enter to view route')
                    label1.setSize(20)
                    label1.setTextColor('blue')
                    label1.draw(win)
                    win.getKey()
                    win.setBackground('black')
                    label.undraw()
                    label1.undraw()
                    loadmaps()
                    l3=drawroute(Dep, Singapore)
                    l4=drawroute(Singapore, Arr)
                    time.sleep(7)
                    for i in l3:
                        i.undraw()
                    for i in l4:
                        i.undraw()
                    endscreen()
                
                else:
                    #goto A
                    pass
           
        elif n1+n2<d1+d2 and n1+n2<s1+s2 and n1+n2<b1+b2:
        
            #C:
                if str.lower(Dep.name)!="new york" and str.lower(Arr.name)!="new york":
                
                    print("Via New York")
                    win.setBackground('black')
                    s="FLIGHT VIA NEW YORK"
                    label=Text(Point(1350/2,200),s)
                    label.setSize(20)
                    label.setTextColor('blue')
                    label.draw(win)
                    label1=Text(Point(1350/2,300),'Press enter to view route')
                    label1.setSize(20)
                    label1.setTextColor('blue')
                    label1.draw(win)
                    win.getKey()
                    win.setBackground('black')
                    label.undraw()
                    label1.undraw()
                    loadmaps()
                    l5=drawroute(Dep, NewYork)
                    l6=drawroute(NewYork, Arr)
                    time.sleep(7)
                    for i in l5:
                        i.undraw()
                    for i in l6:
                        i.undraw()
                    
                    endscreen()
                
                else:
                    #goto A
                    pass
        
        else:
        
            #D:
                if str.lower(Dep.name)!="beijing" and str.lower(Arr.name)!="beijing":
                
                    print("Via Beijing \n")
                    win.setBackground(10)
                    s="FLIGHT VIA BEIJING"
                    label=Text(Point(1350/2,200),s)
                    label.setSize(20)
                    label.setTextColor('blue')
                    label.draw(win)
                    label1=Text(Point(1350/2,300),'Press enter to view route')
                    label1.setSize(20)
                    label1.setTextColor('blue')
                    label1.draw(win)
                    win.getKey()
                    label.undraw()
                    label1.undraw()
                    win.setBackground('black')
                    loadmaps()
                    l7=drawroute(Dep, Beijing)
                    l8=drawroute(Beijing, Arr)
                    time.sleep(7)
                    for i in l7:
                        i.undraw()
                    for i in l8:
                        i.undraw()
                    
                    endscreen()
                
                else:
                    #goto B
                    pass


win = GraphWin('Project', 1350, 800)
create()
start()
print(Arr.lat,Dep.lat)
findroute()
 
