class NumberContainers:

    def __init__(self):
        # index: number
        self.index_to_number_map = {}
        # number: set
        self.number_to_index_map = {}

    def change(self, index: int, number: int) -> None:
        # if index is being replaced
        if index in self.index_to_number_map:
            # update the number_index_map
            prev_num = self.index_to_number_map[index]
            self.number_to_index_map[prev_num].discard(index)

            if len(self.number_to_index_map[prev_num]) == 0:
                del self.number_to_index_map[prev_num]

        # if new index is being added
        if number in self.number_to_index_map:
            self.number_to_index_map[number].add(index)
        else:
            self.number_to_index_map[number] = SortedList([index])

        self.index_to_number_map[index] = number

    def find(self, number: int) -> int:
        if number not in self.number_to_index_map:
            return -1

        return self.number_to_index_map[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
