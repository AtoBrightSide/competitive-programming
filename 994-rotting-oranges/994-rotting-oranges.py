class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = -1
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def inBound(i,j):
            return 0 <= i < len(grid) and 0<= j < len(grid[i])    
        
        myqueue = deque()
        count = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count[grid[i][j]] += 1
                if grid[i][j] == 2:
                    myqueue.append((i,j))
                    
        if count[1] <= 0:
            return 0
        
        if (myqueue == []):
            return -1
        
        while myqueue:
            levels = deque()
            while myqueue:
                i, j = myqueue.popleft()
                for x,y in dirs:
                    if inBound(i+x, j+y) and grid[i+x][j+y] == 1:
                        grid[i+x][j+y] = 2
                        count[1] -= 1
                        levels.append([i+x, j+y])
            
            minutes += 1
            myqueue = levels
    
        return minutes if count[1] <= 0 else -1 