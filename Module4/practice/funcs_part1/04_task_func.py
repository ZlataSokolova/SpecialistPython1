# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
   
       if (p1[0] == p2[0] and p2[0]==p3[0]) or (p1[1] == p2[1] and p2[1] == p3[1]):
        print('треугольник построить невозможно')
       else:
           print('треугольник построить можно')
    pass


# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
