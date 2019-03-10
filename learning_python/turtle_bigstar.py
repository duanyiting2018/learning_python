import turtle
a=turtle.Pen()
a.reset()
for i in range(1,18):
      a.color(0,1,0.25)
      a.forward(100)
      if i%2==0:
            a.left(175)
      else:
            a.left(225)
