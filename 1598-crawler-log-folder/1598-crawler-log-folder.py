class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stage = 0
        for log in logs:
            if log == "../":
                stage = max(0, stage - 1)
            elif log != "./":
                stage += 1
        
        return stage