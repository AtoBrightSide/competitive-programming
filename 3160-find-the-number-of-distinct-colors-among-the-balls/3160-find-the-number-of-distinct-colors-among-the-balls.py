class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToColorTracker = {}
        colorToBallTracker = {}
        distinctColors = []
        currColors = 0
        for query in queries:
            ball, color = query
            # check if ball has been colored before
            if ball in ballToColorTracker:
                prevColor = ballToColorTracker[ball]
                if colorToBallTracker[prevColor] == 1:
                    del colorToBallTracker[prevColor]
                    currColors -= 1
                else:
                    colorToBallTracker[prevColor] -= 1

            currColors += 1 if color not in colorToBallTracker else 0

            ballToColorTracker[ball] = color
            colorToBallTracker[color] = colorToBallTracker.get(color, 0) + 1

            distinctColors.append(currColors)

        return distinctColors
