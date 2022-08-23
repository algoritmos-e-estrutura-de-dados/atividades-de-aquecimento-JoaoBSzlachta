import math

px1 , py1 = [float(x) for x in input().split()]
px2 , py2 = [float(x) for x in input().split()]

d = float(math.sqrt(((px2 - px1)**2) + ((py2 - py1)**2)))

print (f" {round(d , 4)} ")