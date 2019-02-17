from tkinter import *
import time
tk=Tk()
c=Canvas(width=500,height=500)
c.pack()
c.create_polygon(10,10,10,60,40,40)
for i in range(60):
      c.move(1,6,0)
      tk.update()
      time.sleep(0.05)
