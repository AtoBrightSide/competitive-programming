class MapSum:

    def __init__(self):
        self.mapper = {}

    def insert(self, key: str, val: int) -> None:
        self.mapper[key] = val
    
    def sum(self, prefix: str) -> int:
        total = 0
        for k, v in self.mapper.items():
            total += v if k.startswith(prefix) else 0
        return total
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)