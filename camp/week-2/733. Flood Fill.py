class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # these are my directions
        myDirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        # need to store the pixels that have been affected
        visited = set()
        # store the value of the pixel to be changed
        px = image[sr][sc]

        self.myRecur(image, sr, sc, myDirs, px, visited, newColor)

        return image

    def myRecur(self, image, r, c, dirs, px, vis, newColor):
        # check the nodes at the four directions
        for d in dirs:
            image[r][c] = newColor
            r_new, c_new = r+d[0], c+d[1]

            if self.myHelper(image, r_new, c_new, vis) and image[r_new][c_new] == px:
                vis.add((r_new, c_new))
                image[r_new][c_new] = newColor
                self.myRecur(image, r_new, c_new, dirs, px, vis, newColor)

    def myHelper(self, image, r, c, vis):
        if (r, c) in vis:
            return False
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[r]):
            return False
        return True
