class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        mapper = defaultdict(int)
        for year in range(1950, 2051):
            for born, death in logs:
                if born <= year < death:
                    mapper[year] += 1
        
        return sorted(list(mapper.items()), key=lambda x:(-x[1], x[0]))[0][0]
        