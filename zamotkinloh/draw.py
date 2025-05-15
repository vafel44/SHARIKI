import turtle

class Draw:
  
  def __init__(self):
    self.t = turtle.Turtle()
    self.t.hideturtle()
    self.screen = self.t.getscreen()
    self.screen.tracer(0)
    
  def setColor(self, color = "BLACK"):
    self.t.color(color)
    self.t.fillcolor(color)

  def teleport(self, x, y):
    self.t.penup()
    self.t.goto(x, y)
    self.t.pendown()
  
  def circle(self, ball):
    self.teleport(ball.x, ball.y)
    self.t.begin_fill()
    self.t.circle(ball.radius)
    self.t.end_fill()

  def pen(self, size):
    self.t.pensize(size)
  
