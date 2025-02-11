class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = defaultdict(set)
        count = {}
        
        for user, time in logs:
            uam[user].add(time)
        
        for key, values in uam.items():
            count[len(values)] = count.get(len(values), 0) + 1
        
        answer = []
        for i in range(k):
            answer.append(count.get(i + 1, 0))
        
        return answer