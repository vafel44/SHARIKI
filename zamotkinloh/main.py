#Импорт библиотек и файлов
from draw import *
from ball import *
from anim import *

#Функция Main с единой ответственностью - вызывать другую функцию
#где и происходит выполнение кода
def Main():
  
  #Запись в переменную объекта класса Шар (x, y, Radius)
  BB = Ball(0, 0, 15)
  
  #Создание объекта класса Аним (FPS, Draw, Ball)
  #и вызов функции anim(Объект шара)
  Anim(60, Draw()).anim(BB)

#Вызов Main
Main()

