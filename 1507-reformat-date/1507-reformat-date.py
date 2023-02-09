class Solution:
    def reformatDate(self, date: str) -> str:
        month = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", 
            "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
        }[date.split()[1]]
        
        year = date.split()[2]
        
        day = date.split()[0][:-2]
        day = f"0{day}" if len(day) == 1 else day
        return f"{year}-{month}-{day}"