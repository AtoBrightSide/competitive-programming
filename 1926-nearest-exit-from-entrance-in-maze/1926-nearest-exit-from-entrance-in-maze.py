class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        inBounds = lambda i,j: 0 <= i < len(maze) and 0 <= j < len(maze[0])
        DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        queue = deque([[entrance[0], entrance[1], 0]])
        visited = set([entrance[0], entrance[1]])
        
        while queue:
            for _ in range(len(queue)):
                i, j, move = queue.popleft()
                
                for x, y in DIRS:
                    new_i, new_j = x + i, y + j
                    if not inBounds(new_i, new_j) and [i, j] != entrance:
                        return move
                    if inBounds(new_i, new_j) and maze[new_i][new_j] == "." and (new_i, new_j) not in visited:
                        visited.add((new_i, new_j))
                        queue.append([new_i, new_j, move + 1])
                        
        return -1