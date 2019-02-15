import turtle
def mysquare(s,a,a2,a3):
      a=turtle.Pen()
      a.reset()
      for i in range(1,5):
            a.forward(s)
            a.left(90)
            a.color(a,a2,a3)
mysquare(50,0,1,0.27)
