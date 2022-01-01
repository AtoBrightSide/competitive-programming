class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a res variable to store the next greater elements
        res = []
        # reverse the list to pop each last element
        nums1.reverse()
        # while there are elements in nums1
        while nums1:
            # pop the first elt and save it to use as a comparator
            temp = nums2.index(nums1.pop())
            # if all of the elements to the right of current element are less, append -1
            if max(nums2[temp:]) <= nums2[temp]:
                res.append(-1)
            # if not, iterate through list after the current element and return the first greater element
            for num in nums2[temp:]:
                if num > nums2[temp]:
                    res.append(num)
                    break
        return res
