class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a res variable to store the frequent elements
        res=[]
        # count the frequency of the elements
        freq=Counter(nums)
        # store each element and its freq as a pair in a list
        pairs=list(freq.items())
        # sort the list in increasing order, using the frequency as a key
        pairs.sort(key=lambda x:x[1])
        # use while loop to append k freq elements
        while len(res)<k:
            # adding the most frequent elements to res list
            res.append(pairs.pop()[0])
        return res
