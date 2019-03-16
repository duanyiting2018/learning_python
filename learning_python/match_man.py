from tkinter import *
import random,time
class game:
      def __init__(self):
            self.tk=Tk()
            self.tk.title("Mr. Stick Man Races f t Exit.")
            self.tk.resizable(0,0)
            self.tk.wm_attributes("-topmost",1)
            self.c=Canvas(self.tk,width=500,height=500,\
                          highlightthickness=0)
            self.c.pack()
            self.tk.update()
            self.c_h=500
            self.c_w=500
            self.bg=PhotoImage(file="background.gif")
            w=self.bg.width()
            h=self.bg.height()
            for x in range(5):
                  for y in range(5):
                        self.c.create_image(x*w,y*h,image=\
                                            self.bg,anchor='nw')
            self.sprites=[]
            self.run=True
      def main(self):
            while True:
                  if self.run==True:
                        for sprites in self.sprites:
                              sprites.move()
                  self.tk.update()
                  time.sleep(0.03)
class coords:
      def __init__(self,x1=0,y1=0,x2=0,y2=0):
            self.x1=x1
            self.y1=y1
            self.x2=x2
            self.y2=y2
      def w_x(co1,co2):
            if co1.x1>co2.x1 and co1.x1<co2.x2:
                  return True
            elif co1.x2>co2.x1 and co1.x2<co2.x2:
                  return True
            elif co2.x1>co1.x1 and co2.x1<co1.x2:
                  return True
            elif co2.x2>co1.x1 and co2.x2<co1.x1:
                  return True
            else:
                  return False
      def w_y(co1,co2):
            if co1.y1>co2.y1 and co1.y1<co2.y2:
                  return True
            elif co1.y2>co2.y1 and co1.y2<co2.y2:
                  return True
            elif co2.y1>co1.y1 and co2.y1<co1.y2:
                  return True
            elif co2.y2>co1.y1 and co2.y2<co1.y1:
                  return True
            else:
                  return False
      def c_l(co1,co2):
            if w_y(co1,co2):
                  if co1.x1<=co2.x2 and co1.x1>=co2.x1:
                        return True
            return False
      def c_r(co1,co2):
            if w_y(co1,co2):
                  if co1.x2<=co2.x1 and co1.x2>=co2.x2:
                        return True
            return False
      def c_t(co1,co2):
            if w_x(co1,co2):
                  if co1.y1<=co2.y2 and co1.y1>=co2.y1:
                        return True
            return False
      def c_b(y,co1,co2):
            if w_x(co1,co2):
                  y_c=co1.y2+y
                  if y_c>=co2.x1 and co1.x1<=co2.x2:
                        return True
            return False
g=game()
g.main()
