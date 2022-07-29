class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        votes = defaultdict(int)
        vote_times = {}
        leader = -1
        for i in range(len(times)):
            votes[persons[i]] += 1
            leader = persons[i] if votes[persons[i]] >= votes[leader] else leader
            vote_times[times[i]] = leader
        
        self.vote_times = vote_times
        self.times = times
        self.persons = persons

    def q(self, t: int) -> int:
        l, r = 0, len(self.times) - 1
        while l <= r:
            md = (r + l) // 2
            if self.times[md] > t:
                r = md - 1
            else:
                best = md
                l = md + 1
        return self.vote_times[self.times[best]]
    
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)