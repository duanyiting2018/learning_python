from tkinter import *
import time
tk=Tk()
c=Canvas(width=500,height=500)
c.pack()
image=PhotoImage(file='F:/duanyiting2018_GitHub/learn_python/learning_python/text.gif')
c.create_image(0,0,anchor=NW,image=image)
for i in range(60):
      c.move(1,6,0)
      tk.update()
      time.sleep(0.05)
