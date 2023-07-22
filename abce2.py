from tkinter import *
import random
from textwrap import *
from tkinter.simpledialog import *
import datetime
from PIL import Image, ImageTk
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()
def reset():
    global times,clicks,screen,hack
    screen = 0
    print('reseting..')
def fix():
    global left_click
    left_click = False
def button(x=0,y=0,siz=0,text='',sid=0,id=0,cnvs=None,function=None,scrn=None,s=10000):
    global screen
    if sid == id and sid != s:
        cnvs.create_rectangle(x-2, y, siz+x+2,
                         siz+y,
                         fill="white")
        cnvs.create_text(x+round(siz*0.5),y+round(siz*0.5),fill="black",font=f"Arial {round(siz*0.2)}",
                            text=text)
        x2 = root.winfo_pointerx() - root.winfo_rootx()
        y2 = root.winfo_pointery() - root.winfo_rooty()
        clicked = ((x2 > x and x2 < x + siz) and (y2 > y and y2 < y + siz)) and left_click
        if clicked and function:
            exec(function)
        elif clicked and scrn != None:
            print(f'Setting screen to {scrn}')
            screen = scrn
        return clicked
def rectbtn(x=0,y=0,w=0,h=0,text='',sid=0,id=0,cnvs=None,function=None,scrn=None,s=10000):
    global screen
    if sid == id and sid != s:
        cnvs.create_rectangle(x, y, x+w,
                         y+h,
                         fill="white")
        cnvs.create_text(x+round(w*0.5),y+round(h*0.5),fill="black",font=f"Arial {round((w+h)*0.1)}",
                            text=text)
        x2 = root.winfo_pointerx() - root.winfo_rootx()
        y2 = root.winfo_pointery() - root.winfo_rooty()
        clicked = ((x2 > x and x2 < x + w) and (y2 > y and y2 < y + h)) and left_click
        if clicked and function:
            exec(function)
        elif clicked and scrn != None:
            print(f'Setting screen to {scrn}')
            screen = scrn
        return clicked
def bigrectbtn(x=0,y=0,w=0,h=0,text='',sid=0,id=0,cnvs=None,function=None,scrn=None,s=10000):
    global screen
    if sid == id and sid != s:
        cnvs.create_rectangle(x, y, x+w,
                         y+h,
                         fill="white")
        cnvs.create_text(x+round(w*0.5),y+round(h*0.5),fill="black",font=f"Arial {round((w+h)*0.2)}",
                            text=text)
        x2 = root.winfo_pointerx() - root.winfo_rootx()
        y2 = root.winfo_pointery() - root.winfo_rooty()
        clicked = ((x2 > x and x2 < x + w) and (y2 > y and y2 < y + h)) and left_click
        if clicked and function:
            exec(function)
        elif clicked and scrn != None:
            print(f'Setting screen to {scrn}')
            screen = scrn
        return clicked
def normalrectbtn(x=0,y=0,w=0,h=0,text='',sid=0,id=0,cnvs=None,function=None,scrn=None,s=10000):
    global screen
    if sid == id and sid != s:
        cnvs.create_rectangle(x, y, x+w,
                         y+h,
                         fill="white")
        cnvs.create_text(x+round(w*0.5),y+round(h*0.5),fill="black",font=f"Arial {round((w+h)*0.13)}",
                            text=text)
        x2 = root.winfo_pointerx() - root.winfo_rootx()
        y2 = root.winfo_pointery() - root.winfo_rooty()
        clicked = ((x2 > x and x2 < x + w) and (y2 > y and y2 < y + h)) and left_click
        if clicked and function:
            exec(function)
        elif clicked and scrn != None:
            print(f'Setting screen to {scrn}')
            screen = scrn
        return clicked
def startbtn(x=0,y=0,siz=0,text='',sid=0,id=0,cnvs=None,function=None,scrn=None,s=10000):
    global screen
    if sid == id and sid != s:
        cnvs.create_rectangle(x-2, y, siz+x+20,
                         siz+y,
                         fill="green")
        cnvs.create_text(x+round((siz+20)*0.5),y+round(siz*0.5),fill="black",font=f"Arial {round(siz*0.4)}",
                            text=text)
        x2 = root.winfo_pointerx() - root.winfo_rootx()
        y2 = root.winfo_pointery() - root.winfo_rooty()
        clicked = ((x2 > x and x2 < x + siz + 20) and (y2 > y and y2 < y + siz)) and left_click
        if clicked and function:
            exec(function)
        elif clicked and scrn != None:
            print(f'Setting screen to {scrn}')
            screen = scrn
        return clicked
def imgbtn(x=0,y=0,siz=30,image='',text='',sid=0,id=0,cnvs=None,function=None,scrn=None,s=10000,color="#FFFFFF"):
    global screen
    if sid == id and sid != s:
        cnvs.create_image(x, y, image = image, anchor = NW)
        cnvs.create_text(x+round(siz*0.5),y+round(siz+3),fill=color,font=f"Arial {round(siz*0.2)} bold",
                            text=text)
        x2 = root.winfo_pointerx() - root.winfo_rootx()
        y2 = root.winfo_pointery() - root.winfo_rooty()
        clicked = ((x2 > x and x2 < x + siz) and (y2 > y and y2 < y + siz)) and left_click
        if clicked and function:
            exec(function)
        elif clicked and scrn != None:
            print(f'Setting screen to {scrn}')
            screen = scrn
        return clicked
def text(x,y,cnvs,text,color="#1C1C1C"):
    cnvs.create_text(x,y,fill=color,
                            text=text, anchor="nw")
def boxxedtext(x,y,w,h,cnvs,text):
    cnvs.create_rectangle(x, y, x+w,
                         y+h,
                         fill="white")
    cnvs.create_text(x+5,y+5,
                            text=text, anchor="nw")
    
times = 0
clicks = 0
screen = 0
left_click = False
def click_start(event):
    global left_click
    left_click = True

def click_stop(event):
    global left_click
    left_click = False
def keypress(event):
    global kext
    if screen == 2:
        if event.keysym == 'BackSpace':
            kext = kext[0:len(kext)-1]
        elif event.char != 'Return':
            kext += event.char
        elif event.char == '':
            kext = kext[0:len(kext)-2]
        else:
            kext += '\n'
def toggle():
    global menu
    menu = not menu
def getappname(app):
    if app == 1:
        return 'My computer'
    if app == 2:
        return 'Notepad'
    if app == 3:
        return 'Calc'
    return 'Unknown app'
root = Tk()
root.bind('<Key>', keypress)
m = Menu(root, tearoff=0)
m.add_command(label="Reset",command=reset)
m.add_command(label="Fix left click",command=fix)
root.title('pywinxp')
root.resizable(False, False)
root.bind("<Button-1>", click_start)
root.bind("<B1-ButtonRelease>", click_stop)
C = Canvas(bg='darkcyan', highlightthickness=0,
           borderwidth=0,height=300,width=400)
C.bind("<Button-3>", do_popup)
kext = ''
mypc = ImageTk.PhotoImage(Image.open("icons/MYPC.png"))
notepad = ImageTk.PhotoImage(Image.open("icons/notepad.png"))
calc = ImageTk.PhotoImage(Image.open("icons/calc.png"))
close = ImageTk.PhotoImage(Image.open("icons/close.png"))
shutdown = ImageTk.PhotoImage(Image.open("icons/shutdown.png"))
restart = ImageTk.PhotoImage(Image.open("icons/restart.png"))
bliss = ImageTk.PhotoImage(Image.open("icons/bliss.jpg"))
equation = ''
savedtext = ''
def add(num):
    global equation
    equation+=str(num)
menu = False
def update():
    C.delete('all')
    C.create_image(0,0, image = bliss, anchor = NW)
    # Desktop
    if screen < 1:
        imgbtn(10,10,image=mypc,text='My computer',cnvs=C,scrn=1)
        imgbtn(10,50,image=notepad,text='Notepad',cnvs=C,scrn=2)
        imgbtn(10,90,image=calc,text='Calc',cnvs=C,scrn=3)
    if screen == -1:
        C.create_rectangle(0, 125-25, 100,
                         300-25,
                         fill="lightgrey")
        rectbtn(0,100,100,25,text='My computer', cnvs=C, scrn=1)
        rectbtn(0,125,100,25,text='Notepad', cnvs=C, scrn=2)
        rectbtn(0,150,100,25,text='Calc', cnvs=C, scrn=3)
        rectbtn(0,250,100,25,text='Shutdown', cnvs=C, scrn=4)
    # add other background to other screens
    if screen > 0:
        C.create_rectangle(0, 0, 400,
                         300,
                         fill="lightgrey")
        C.create_rectangle(0, 0, 400,
                         16,
                         fill="#4b5bff")
        imgbtn(400-16,1,image=close,text='',cnvs=C,scrn=0)
        text(2,2,C,getappname(screen),'#FFFFFF')
    if screen == 1:
        text(5,32,C,'WINDOWS')
        text(5,48,C,'Users')
        text(5,64,C,'Program Files')
    elif screen == 2:
        bigrectbtn(0,16,36,20,text='File', cnvs=C, function="toggle()")
        bigrectbtn(36,16,36,20,text='Edit', cnvs=C)
        bigrectbtn(36*2,16,36,20,text='For..', cnvs=C)
        bigrectbtn(36*3,16,36,20,text='View', cnvs=C)
        bigrectbtn(36*4,16,36,20,text='Help', cnvs=C)
        C.create_rectangle(0, 36, 400,
                         300-16,
                         fill="white")
        text(5,40,C,kext)
        if menu:
            C.create_rectangle(0, 16+20, 64,
                         128,
                         fill="#aeab95")
            normalrectbtn(0,16+20,64,20,text='New', cnvs=C, function="global kext; kext=''")
            normalrectbtn(0,16+40,64,20,text='Save', cnvs=C, function="global kext, savedtext; savedtext=kext")
            normalrectbtn(0,16+60,64,20,text='Save As', cnvs=C, function="global kext, savedtext; savedtext=kext")
            normalrectbtn(0,16+80,64,20,text='Open', cnvs=C, function="global kext, savedtext; kext=savedtext")
            normalrectbtn(0,16+100,64,20,text='Close', cnvs=C, scrn=0)
    elif screen == 3:
        boxxedtext(100,100-60,150,150,C,'')
        bigrectbtn(130,70,30,30,text='C', cnvs=C, function="global equation; equation=''")
        bigrectbtn(100,70,30,30,text='<-', cnvs=C, function="global equation; equation = equation[0:len(equation)-1]")
        bigrectbtn(100,100,30,30,text='1', cnvs=C, function="add(1)")
        bigrectbtn(130,100,30,30,text='2', cnvs=C, function="add(2)")
        bigrectbtn(160,100,30,30,text='3', cnvs=C, function="add(3)")
        bigrectbtn(100,130,30,30,text='4', cnvs=C, function="add(4)")
        bigrectbtn(130,130,30,30,text='5', cnvs=C, function="add(5)")
        bigrectbtn(160,130,30,30,text='6', cnvs=C, function="add(6)")
        bigrectbtn(100,160,30,30,text='7', cnvs=C, function="add(7)")
        bigrectbtn(130,160,30,30,text='8', cnvs=C, function="add(8)")
        bigrectbtn(160,160,30,30,text='9', cnvs=C, function="add(9)")
        bigrectbtn(100,190,60,30,text='0', cnvs=C, function="add(0)")
        bigrectbtn(160,190,30,30,text='.', cnvs=C, function="add('.')")
        bigrectbtn(190,190,30,30,text='+', cnvs=C, function="add('+')")
        bigrectbtn(190,160,30,30,text='-', cnvs=C, function="add('-')")
        bigrectbtn(190,130,30,30,text='*', cnvs=C, function="add('*')")
        bigrectbtn(190,100,30,30,text='/', cnvs=C, function="add('/')")
        bigrectbtn(220,160,30,60,text='=', cnvs=C, function="global equation; equation = str(eval(equation))")
        boxxedtext(100,100-60,150,30,C,equation)
    C.create_rectangle(0, 300-25, 400,
                         300,
                         fill="#4b5bff")
    text(400-55,300-20,C,datetime.datetime.now().strftime("%I:%M %p"))
    startbtn(0,300-25,25,'Start',cnvs=C,scrn=-1 if screen != -1 else 0)
    if screen == 4:
        C.create_rectangle(0, 0, 400,
                         300,
                         fill="black")
        C.create_rectangle(50, 50, 400-50,
                         300-50,
                         fill="white")
        C.create_rectangle(50, 50, 350,
                         100,
                         fill="#4b5bff")
        C.create_rectangle(50, 250, 350,
                         200,
                         fill="#4b5bff")
        imgbtn(130,130,image=shutdown,text='Shutdown',cnvs=C,scrn=5,color="#000000")
        imgbtn(130+90,130,image=restart,text='Restart',cnvs=C,function="reset()",color="#000000")
        rectbtn(300-50,215,80,50-(15*2),text='Cancel',cnvs=C,scrn=0)
    if screen == 5:
        C.create_rectangle(0, 0, 400,
                         300,
                         fill="black")
        C.create_text(200,150,fill="orange",
                            text='Its now safe to turn off your computer')
    root.after(70,update)

update()
C.pack()
mainloop()
