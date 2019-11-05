# задача 1.2.8

x1 ,y1, x2, y2 = int(input("x1.1= ")), int(input ("y1.1= ")), int(input ("x1.2= ")), int(input("y1.2= "))
x3, y3, x4, y4 = int(input("x2.1= ")), int(input ("y2.1= ")), int(input ("x2.2= ")), int(input("y2.2= "))
# задал координаты диагоналей прямоугльников

# x1.1=x1  y1.1= y1  x1.2=x2  y1.2=y2  x2.1=x3 y2.1=y3  x2.2=x4  y2.2=y4

#if x1.2 > x1.1 and y1.2 > y1.1 and x2.2 > x2.1 and y2.2 > x2.1
#    D_x1 = math.fabs(x1.2-x1.1)
#    D_y1 = math.fabs(y1.2-y1.1)
#    D_x2 = math.fabs(x2.2-x2.1)
#    D_y2 = math.fabs(y2.2-y2.1)
#    for x1.1 in x1.2:

if x1 > x2:
    x1, x2 = x2, x1
if x3 > x4:
    x3, x4 = x4, x3
if y1 > y2:
    y1, y2 = y2, y1
if y3 > y4:
    y3, y4 = y4, y3


if x1 == x3 and y1 == y3 and  x2 == x4 and y2 == y4:
    print("прямоугольники совподают!")
if x1 == x4 and y1 == y4:
    print("прямоугольники пересекаются в точке (" + str(x1) + ";" + str(y1) + ")")
if x2 == x3 and y2 == y3:
    print("прямоугольники пересекаются в точке (" + str(x2) + ";" + str(y2) + ")")
if x1 == x4 and y2 == y3:
    print("прямоугольники пересекаются в точке (" + str(x1) + ";" + str(y2) + ")")
if x2 == x3 and y1 == y4:
    print("прямоугольники пересекаются в точке (" + str(x2) + ";" + str(y1) + ")")
    
if x3 > x1 and x3 < x2 and y3 > y1 and y3 < y2 and x4 > x1 and x4 < x2 and y4 > y1 and y4 < y2:
    print("Прямоугольник 2 меньше и находится внутри прямоугольника 1 ")
if x1 > x3 and x1 < x4 and x2 > x3 and x2 < x4 and y1 > y3 and y1 < y4 and y2 > y3 and y2 < y4:
    print("Прямоугольник 1 меньше и находится внутри прямоугольника 2 ")
    
if x3 > x1 and x3 < x2 and x4 > x2 and y3 > y1 and y3 < y2 and y4 > y2 :
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x3) + " ; " + str(y2) + " ) , ( " + str(x2) + " , " + str(y3) + " )")
if x1 > x3 and x1 < x4 and x2 > x4 and y1 > y3 and y1 < y4 and y2 > y4 :
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x1) + " ; " + str(y4) + " ) , ( " + str(x4) + " , " + str(y1) + " )")
if x3 > x1 and x3 < x2  and x4 > x2 and y1 > y3 and y1 < y4 and y2 > y4 :
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x3) + " ; " + str(y1) + " ) , ( " + str(x2) + " , " + str(y4) + " )")
if x1 > x3 and x1 < x4 and x2 > x4 and y2 > y3 and y2 < y4 and y1 < y3 :
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x1) + " ; " + str(y3) + " ) , ( " + str(x4) + " , " + str(y2) + " )")
    
if x3 > x1 and x3 < x2 and x4 > x2 and y3 > y1 and y3 < y2 and y4 < y2 : 
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x2) + " ; " + str(y3) + " ) , ( " + str(x2) + " , " + str(y4) + " )")
if x3 > x1 and x3 < x2 and x4 < x2 and y3 > y1 and y3 < y2 and y4 > y2 : 
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x3) + " ; " + str(y2) + " ) , ( " + str(x4) + " , " + str(y2) + " )")
if x4 > x1 and x4 < x2 and x3 < x1 and y3 > y1 and y3 < y2 and y4 < y2 : 
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x1) + " ; " + str(y3) + " ) , ( " + str(x1) + " , " + str(y4) + " )")
if x3 > x1 and x3 < x2 and x4 < x2 and y4 > y1 and y4 < y2 and y3 < y1 : 
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x3) + " ; " + str(y1) + " ) , ( " + str(x4) + " , " + str(y1) + " )")

if x1 > x3 and x1 < x4 and x2 > x4 and y1 > y3 and y1 < y4 and y2 < y4 : 
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x4) + " ; " + str(y1) + " ) , ( " + str(x4) + " , " + str(y2) + " )")
if x1 > x3 and x1 < x4 and x2 < x4 and y1 > y3 and y1 < y4 and y2 > y4 : 
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x1) + " ; " + str(y4) + " ) , ( " + str(x2) + " , " + str(y4) + " )")
if x2 > x3 and x2 < x4 and x1 < x3 and y1 > y3 and y1 < y4 and y2 < y4 : 
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x3) + " ; " + str(y1) + " ) , ( " + str(x3) + " , " + str(y2) + " )")
if x1> x3 and x1 < x4 and x2 < x4 and y2 > y3 and y2 < y4 and y1 < y3 : 
    print("Прямоугольники пересекаются в 2 точках: ( " + str(x1) + " ; " + str(y3) + " ) , ( " + str(x2) + " , " + str(y3) + " )")


        

    
        





