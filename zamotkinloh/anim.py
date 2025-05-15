#Библиотека time
import time

class Anim:
  
  def __init__(self, fps, draw):
    
    #Интервал обновления экрана
    self.interval = 1 / fps 
    #Таймер (объект класса Time)
    self.time = time.time()
    #Объект класса Draw
    self.draw = draw

  #Функция для анимации объектов на экране
  def anim(self, ball):
    self.draw.setColor("green") 

    while True:
      self.draw.pen(100)

      elapsed_time = time.time() - self.time
  
      if elapsed_time < self.interval:
          time.sleep(self.interval - elapsed_time)
          
      print(ball.radius)
      #self.draw.screen.clear()
      self.draw.circle(ball)
      self.draw.screen.update()