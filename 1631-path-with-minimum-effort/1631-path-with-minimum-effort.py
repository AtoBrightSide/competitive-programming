class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def isValid(i, j):
            return 0<=i<len(heights) and 0<=j<len(heights[i])
        
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]        
        
        visited, myDict, myHeap = set(), {(0,0):0}, [[0, (0,0)]]
        
        def dijkstra():
            while len(visited)<len(heights)*len(heights[0]): 
                eff, (i, j) = heapq.heappop(myHeap)
                if (i, j) == (len(heights)-1, len(heights[0])-1):
                    return myDict[(i,j)]
                for x, y in dirs:
                    if isValid(i+x,j+y) and (i+x, j+y) not in visited:
                        max_eff = max(abs(heights[i+x][j+y] - heights[i][j]), eff)
                        if (x+i,y+j) not in myDict or ((x+i,y+j) in myDict and max_eff<myDict[(x+i, y+j)]):
                            myDict[(x+i, y+j)] = max_eff
                            heapq.heappush(myHeap, [max_eff, (i+x,j+y)])
                        
                        
                visited.add((i,j))
            return myDict[(len(heights)-1, len(heights[0])-1)]

        
        return dijkstra()