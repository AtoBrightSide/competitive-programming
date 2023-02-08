class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        my_map = defaultdict(list)
        for x, y in adjacentPairs:
            my_map[x].append(y)
            my_map[y].append(x)
        
        for key in my_map:
            if len(my_map[key]) == 1:
                curr_num = key
                break
        
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