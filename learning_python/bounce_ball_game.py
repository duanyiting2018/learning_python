from tkinter import *
import time,random
tk=Tk()
a=1
tk.title("Bounce ball game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
c=Canvas(tk,width=500,height=450,bd=0,highlightthickness=0)
c.pack()
tk.update()
class ball:
      def __init__(self,ca,paddle,co):
            self.ca=ca
            self.paddle=paddle
            self.id=ca.create_oval(10,10,30,30,fill=co)
            self.ca.move(self.id,245,100)
            starts=[-3,-2,-1,1,2,3]
            random.shuffle(starts)
            self.x=starts[0]
            self.y=-3
            self.c_h=self.ca.winfo_height()
            self.c_w=self.ca.winfo_width()
            self.hit_bottom=False
      def hit_paddle(self,pos):
            paddle_p=self.ca.coords(self.paddle.id)
            if pos[2]>=paddle_p[0]and pos[0]<=paddle_p[2]:
                  if pos[3]>=paddle_p[1]and pos[3]<=paddle_p[3]:
                        return True
            return False
      def draw(self):
            global a
            self.ca.move(self.id,self.x,self.y)
            pos=self.ca.coords(self.id)
            if pos[1]<=0:
                  self.y=3
                  #print(self.y,"y")
            if pos[3]>=self.c_h:
                  self.hit_bottom=True
            if self.hit_paddle(pos)==True:
                  c.create_text(20,20,text=a,font=('Times',20))
                  self.y=-3
                  #print(self.y,"y")
                  a=a+1
            if pos[0]<=0:
                  self.x=3
                  #print(self.x,"x")
            if pos[2]>=self.c_w:
                  self.x=-3
                  #print(self.x,"x")
class paddle:
      def __init__(self,ca,co):
            self.ca=ca
            self.id=ca.create_rectangle(0,0,100,20,fill=co)
            self.ca.move(self.id,200,300)
            self.x=0
            self.c_w=self.ca.winfo_width()
            self.ca.bind_all('<KeyPress-Left>',self.t_l)
            self.ca.bind_all('<KeyPress-Right>',self.t_r)
      def draw(self):
            self.ca.move(self.id,self.x,0)
            pos=self.ca.coords(self.id)
            if pos[0]<=0:
                  self.x=-2
            elif pos[0]>=self.c_w:
                  self.x=2
      def t_l(self,evt):
            self.x=-2
      def t_r(self,evt):
            self.x=2
paddle=paddle(c,"orange")
ball=ball(c,paddle,"green")
while True:
      if ball.hit_bottom==False:
            ball.draw()
            paddle.draw()
      tk.update_idletasks()
      tk.update() 
      time.sleep(0.03)
