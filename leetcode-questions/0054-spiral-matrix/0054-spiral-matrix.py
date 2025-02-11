class Solution:
    def spiralOrder(self, inputMatrix: List[List[int]]) -> List[int]:
      DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
      inBounds = lambda x, y: 0 <= x < len(inputMatrix) and 0 <= y < len(inputMatrix[0])

      ans = []
      visited = set()
      def traverse(i, j, goTo):
        ans.append(inputMatrix[i][j])
        visited.add((i, j))
        for _ in range(4):
          new_i = i + DIRS[goTo % 4][0]
          new_j = j + DIRS[goTo % 4][1]
          if inBounds(new_i, new_j) and (new_i, new_j) not in visited:
            traverse(new_i, new_j, goTo)
          else:
            goTo += 1

      traverse(0, 0, 0)
      return ans