from typing import Counter
def majorityElement(nums):
    counted = Counter(nums)
    res = [key for key in counted if counted[key]>len(nums)/3]
    return res
print(majorityElement([3,2,3]))