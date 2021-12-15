def merge(intervals):
    intervals.sort()
    res = []
    for i in range(1,len(intervals)):
        if res==[]:
            res.append(intervals[0])
        if res[-1][1]>=intervals[i][0]:
            res[-1][1]=max(res[-1][1],intervals[i][1])
        else:
            res.append(intervals[i])
    return res if len(intervals)>1 else [intervals[0]]
merge([[1,8]])