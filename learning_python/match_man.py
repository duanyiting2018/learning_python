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
g=game()
g.main()
