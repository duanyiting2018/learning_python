from tkinter import *
import time,random
tk=Tk()
tk.title("Bounce ball game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
c=Canvas(tk,width=500,height=450,bd=0,highlightthickness=0)
c.pack()
tk.update()
class ball:
      def __init__(self,ca,co):
            self.ca=ca
            self.id=ca.create_oval(10,10,30,30,fill=co)
            self.ca.move(self.id,245,100)
            starts=[-3,-2,-1,1,2,3]
            random.shuffle(starts)
            self.x=starts[0]
            self.y=-3
            self.c_h=self.ca.winfo_height()
            self.c_w=self.ca.winfo_width()
      def draw(self):
            self.ca.move(self.id,self.x,self.y)
            pos=self.ca.coords(self.id)
            if pos[1]<=0:
                  self.y=3
                  #print(self.y,"y")
            if pos[3]>=self.c_h:
                  self.y=-3
                  #print(self.y,"y")
            if pos[0]<=0:
                  self.x=3
                  #print(self.x,"x")
            if pos[2]>=self.c_w:
                  self.x=-3
                  #print(self.x,"x")
class paddle:
      def __init__(s,ca,co):
            self.id=ca.create_rectangle(0,0,100,20,fill=co)
            self.ca.move(self.id,200,300)
      def draw(self):
            pass
ball=ball(c,"green")
paddle=paddle(c,"orange")
while True:
      ball.draw()
      paddle.draw()
      tk.update_idletasks()
      tk.update()
      time.sleep(0.03)
