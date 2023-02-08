class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        my_map = defaultdict(list)
        for x, y in adjacentPairs:
            my_map[x].append(y)
            my_map[y].append(x)
        
        curr_num = sorted(my_map.items(), key=lambda x: (len(x[1]), x[0]))[0][0]
        nums = [curr_num]
        used = set([curr_num])
        while len(nums) < len(my_map):
            for adjNum in my_map[curr_num]:
                if adjNum not in used:
                    used.add(adjNum)
                    curr_num = adjNum
                    break
            nums.append(curr_num)
        
        return nums