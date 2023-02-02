class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:    return "Zero"
        mapper = { 1: ["One"], 2: ["Two","Twenty"], 3: ["Three","Thirty" ], 4: ["Four", "Forty"], 5: ["Five", "Fifty"], 6: ["Six", "Sixty"], 7: ["Seven", "Seventy"], 8: ["Eight", "Eighty"], 9: ["Nine", "Ninety"] }
        
        specialMapper = { 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen" }
        
        numbers = [[0] * 3 for i in range(4)]
        num = list(str(num))
        j = 3
        while num:
            i = 2
            while num and i > -1:
                numbers[j][i] = int(num.pop())
                i -= 1
            j -= 1
        
        english_words = ""
        for i in range(len(numbers)):
            current_number = ""
            for j in range(3):
                if numbers[i][j] != 0:
                    if j == 0:  current_number += mapper[numbers[i][j]][0] + " Hundred "
                    elif j == 1:
                        if numbers[i][j] == 1:
                            cur = str(numbers[i][j]) + str(numbers[i][j+1])
                            current_number += specialMapper[int(cur)] + " "
                            break
                        else:   current_number += mapper[numbers[i][j]][1] + " "
                    elif j == 2:   current_number += mapper[numbers[i][j]][0] + " "
            if current_number != "":
                if i == 0:      english_words += current_number + "Billion "
                elif i == 1:    english_words += current_number + "Million "
                elif i == 2:    english_words += current_number + "Thousand "
                else:           english_words += current_number
        
        return english_words[:-1]