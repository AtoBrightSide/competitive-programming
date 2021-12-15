def kClosest(points,k):
    res=[]
    for i in points:
        res.append((pow(i[0],2)+pow(i[1],2), i)) 
    res.sort()
    points=[]
    for i in range(k):  
        points.append(res[i][1])
    return points
print(kClosest([[1,3],[-2,2],[2,-2]]
,2))