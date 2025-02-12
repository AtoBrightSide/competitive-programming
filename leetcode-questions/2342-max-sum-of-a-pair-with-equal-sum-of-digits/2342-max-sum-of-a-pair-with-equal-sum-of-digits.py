class Solution:
    def calculateDigitSum(self, num):
        return sum([int(digit) for digit in str(num)])

    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map = {}

        for num in nums:
            curr_num_sum = self.calculateDigitSum(num)

            if curr_num_sum not in digit_sum_map:
                digit_sum_map[curr_num_sum] = []

            heapq.heappush(digit_sum_map[curr_num_sum], num)
            if len(digit_sum_map[curr_num_sum]) > 2:
                heapq.heappop(digit_sum_map[curr_num_sum])

        max_sum_pair = -1
        for digit_sum, index_list in digit_sum_map.items():
            if len(index_list) == 2:
                num1, num2 = index_list
                max_sum_pair = max(max_sum_pair, num1 + num2)

        return max_sum_pair
