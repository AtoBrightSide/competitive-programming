class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        
        queue = [[-1] * 2 for i in range(len(people))] 

        for h, k in people:
            count = k
            for i in range(len(queue)):
                if count <= 0 and queue[i][0] == -1:
                    queue[i][0] = h
                    queue[i][1] = k
                    break
                if queue[i][0] == -1 or queue[i][0] == h:
                    count -= 1

        return queue