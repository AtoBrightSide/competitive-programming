class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        
        L = min(len(version1), len(version2))
        M = max(len(version1), len(version2))
        
        for i in range(M):
            if i < L:
                if int(version1[i]) > int(version2[i]):     return 1
                elif int(version1[i]) < int(version2[i]):   return -1
            
            else:
                if i < len(version1) and int(version1[i]) > 0:
                    return 1

                if i < len(version2) and int(version2[i]) > 0:
                    return -1
            
        return 0