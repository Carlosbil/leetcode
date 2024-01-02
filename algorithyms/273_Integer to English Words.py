class Solution:
    """
    use maps will be faster than arrays, buy will use more memory
    change map to array will be slower but use less memory
    """   
    under_twenty_map = {
        0: '',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine', 
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve', 
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen', 
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen', 
        19: 'Nineteen'
    }
    tens = {
        0: '',
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty', 
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy', 
        8: 'Eighty',
        9: 'Ninety'
    }
    thousands = ['','Thousand','Million','Billion']
    def helper(self, num):
        if num == 0: return ''
        elif num < 20: return self.under_twenty_map[num] + ' '
        elif num < 100: return self.tens[num // 10] + ' ' + self.helper(num % 10)
        else: return self.under_twenty_map[num // 100] + ' Hundred ' + self.helper(num % 100)

    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        res = ''
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + ' ' + res
            else:
                break
            num //= 1000
        return res.strip()