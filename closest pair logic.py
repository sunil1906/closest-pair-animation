import sys
def distance(a, b):
    return ( (b[1] - a[1])**2 + (b[0] - a[0])**2 )**(1/2)

def bruteForce(points, n):
    mini = sys.maxsize
    for i in range(n-1):
        for j in range(i+1, n):
            if(distance(points[i], points[j]) < mini):
                mini = distance(points[i], points[j])
    return mini            

def stripClosest(points, n, prevMin):
    mini = prevMin
    for i in range(n-1):
        for j in range(i+1, n):
            if points[j][1] - points[i][1] > mini:
                break
            if(distance(points[i], points[j]) < mini):
                mini = distance(points[i], points[j])
    return mini            
def closestPair(x_sorted, y_sorted, n):
    if n<=3:
        return bruteForce(x_sorted, n)    
    middle = n//2
    midpoint = x_sorted[middle]    
    left_x = x_sorted[ : middle]
    right_x = x_sorted[middle : ]    
    left_y = y_sorted[ : middle]
    right_y = y_sorted[middle : ]    
    dl = closestPair(left_x, left_y, middle)
    dr = closestPair(right_x, right_y, n-middle)
    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(y_sorted[i][0] - midpoint[0]) < d:
            strip.append(y_sorted[i])
    return stripClosest(strip, len(strip), d)       

points = [(20, 43), (21, 21), (28, 39), (2, 10), (11, 47), (35, 46), (36, 3), (44, 41)
                  , (13, 5),  (40, 19)]
n = len(points)
x_sorted = sorted(points)
y_sorted = sorted(points, key = lambda x : x[1])

minimum = closestPair(x_sorted, y_sorted, n)
print(minimum)

