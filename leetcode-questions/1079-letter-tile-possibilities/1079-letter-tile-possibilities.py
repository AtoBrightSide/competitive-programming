class Solution:
    def __init__(self):
        self.tiles = ""
        self.seen = set()

    def backtrack(self, curr_tiles, index_set):
        if curr_tiles in self.seen:
            return 0

        self.seen.add(curr_tiles)
        sequences = 1
        for index, letter in enumerate(self.tiles):
            curr_tiles += letter
            if curr_tiles not in self.seen and index not in index_set:
                index_set.add(index)
                sequences += self.backtrack(curr_tiles, index_set)
                index_set.remove(index)
            curr_tiles = curr_tiles[:-1]

        return sequences

    def numTilePossibilities(self, tiles: str) -> int:
        self.tiles = tiles
        all_sequences = 0
        for index, letter in enumerate(self.tiles):
            all_sequences += self.backtrack(letter, set([index]))

        return all_sequences
