class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color_tracker = {}
        color_to_ball_tracker = {}
        distinct_colors = []
        curr_colors = 0
        for query in queries:
            ball, color = query
            # check if ball has been colored before
            if ball in ball_to_color_tracker:
                prev_color = ball_to_color_tracker[ball]
                if color_to_ball_tracker[prev_color] == 1:
                    del color_to_ball_tracker[prev_color]
                    curr_colors -= 1
                else:
                    color_to_ball_tracker[prev_color] -= 1

            curr_colors += 1 if color not in color_to_ball_tracker else 0

            ball_to_color_tracker[ball] = color
            color_to_ball_tracker[color] = color_to_ball_tracker.get(
                color, 0) + 1

            distinct_colors.append(curr_colors)

        return distinct_colors
