"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        return self.dfs(employees, id)
        
    def dfs(self, employees, id):
        total = 0
        for i in range(len(employees)):
            if employees[i].id == id:
                if employees[i].subordinates != []:
                    for sub_id in employees[i].subordinates:
                        total += self.dfs(employees, sub_id)
                    return total+employees[i].importance
                else:
                    return employees[i].importance
            
