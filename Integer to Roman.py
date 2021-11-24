#example input
num = 3

#solution
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_table = [["I", 1],
                       ["IV", 4],
                       ["V", 5],
                       ["IX", 9],
                       ["X", 10],
                       ["XL", 40],
                       ["L", 50],
                       ["XC", 90],
                       ["C", 100],
                       ["CD", 400],
                       ["D", 500],
                       ["CM", 900],
                       ["M", 1000]]
        answer = ""
        for roman, value in reversed(roman_table):
            if num // value:
                count = num // value
                answer += (roman*count)
                num = num% value
        return answer
