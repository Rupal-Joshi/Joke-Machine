from guizero import App, Text,PushButton, ButtonGroup


# joke 1- example
def stick_joke ():
  pushbutton1.hide()
  pushbutton2.hide()
  pushbutton3.hide()
  pushbutton4.hide()
    
  joke_text.value = "what is brown and sticky? "
  pushbutton1_2 = PushButton(app, text = "brown stick", command= brown_stick)
  pushbutton1_3 = PushButton(app, text ="strawberry cake", command = brown)

def brown_stick (): 
  joke_text.value = "correct"
  app.bg= "green"

def brown():
  joke_text.value = "incorrect"
  app.bg= "red"

# joke 2
def fluff ():
  pushbutton1.hide()
  pushbutton2.hide()
  pushbutton3.hide()
  pushbutton4.hide()
    
  pushbutton2_2 = PushButton(app,text = "pink fluff", command = pink_fluff)
  pushbutton2_3 = PushButton(app, text= "cotton wool", command =pink)

def pink_fluff ():
  joke_text.value = "correct"
  app.bg= "green"

def pink():
  joke_text.value="incorrect"
  app.bg= "red"

# joke 3
def toilet_paper ():
  pushbutton1.hide()
  pushbutton2.hide()
  pushbutton3.hide()
  pushbutton4.hide() 
  joke_text.value = "why do chickens cross the road? "
  pushbutton3_2 = PushButton(app, text="to get some toilet paper", command = paper)
  pushbutton3_3 = PushButton(app,text="to get to the other side", command=toilet)

def paper():
  joke_text.value = "correct"
  app.bg= "green"

def toilet(): 
  joke_text.value = "incorrect"
  app.bg= "red"
  

# joke 4
def frog_car():
  pushbutton1.hide()
  pushbutton2.hide()
  pushbutton3.hide()
  pushbutton4.hide()
  
  joke_text.value = "what happens to a frog's car when it breaks down"
  pushbutton4_2 = PushButton(app, text = "it gets toad away", command = frog)
  pushbutton4_3 = PushButton(app, text = "nothing happens", command= car)

def frog(): 
  joke_text.value= "correct"
  app.bg="green"
def car():
  joke_text.value= "incorrect"
  app.bg= "red"



app = App(title="jokes")


pushbutton1= PushButton(app, text="Stick", command = stick_joke)
pushbutton2= PushButton(app, text="fluff", command = fluff)
pushbutton3= PushButton(app, text="chicken", command = toilet_paper)
pushbutton4= PushButton(app, text="frog", command = frog_car,)
joke_text = Text(app, text="")

app.display()
