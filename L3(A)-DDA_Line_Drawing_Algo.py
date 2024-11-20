import matplotlib.pyplot as plt 

#from (1, 1) to (4, 3)

x1, y1 = 1, 1
x2, y2 = 4, 3

dx = x2-x1
dy = y2-y1 
m = dy/dx

print('m =', m)

points = []
points.append((x1, y1))

xi, yi = x1, y1
while xi != x2 and yi != y2:
    if (abs(dx) >= abs(dy)):
        xi += 1
        yi += m
    else:
        yi += 1
        xi += 1/m


    points.append((xi, yi))


points.append((x2, y2))

x = [point[0] for point in points]
y = [point[1] for point in points]


print(points)

plt.plot(x, y, color= 'b', marker = 'o')
plt.grid(True)
plt.show()