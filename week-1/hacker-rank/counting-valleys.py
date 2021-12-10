# UDDDUDUU
def countingValleys(steps, path):
    # Write your code here
    counter, down = 0, 0
    for step in path:
        counter = counter + (1 if (step == 'D' and down == 0) else 0)
        down = down + (1 if step == 'D' else -1)
    return counter


print(countingValleys(8, "DDUUDDUDUUUD"))