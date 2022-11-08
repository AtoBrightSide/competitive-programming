class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = set()
        used = set()
        def recur(mins, hrs):
            count = mins.bit_count() + hrs.bit_count()
            if count >= turnedOn or (mins, hrs) in used:
                if count == turnedOn and 0 <= hrs <= 11 and 0 <= mins <= 59:
                    curr_time = str(hrs) + ":" + (str(mins) if len(str(mins)) == 2 else "0" + str(mins))
                    ans.add(curr_time)
                return
            used.add((mins, hrs))
            for i in range(6):
                if i < 4 and not (hrs & (1 << i)):
                    recur(mins, hrs | (1 << i))
                if not (mins & (1 << i)):
                    recur(mins | (1 << i), hrs)
        
        recur(0, 0)
        return ans