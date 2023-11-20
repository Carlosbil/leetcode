"""
Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
"""
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        #get the vowels in the string
        vowel_list = [char for char in s if char in vowels]
        #sort the list in vowels
        vowel_list.sort(key=lambda x: vowels.index(x))
        #replace the vowels in the string with the sorted vowels
        for i, char in enumerate(s):
            if char in vowels:
                s = s[:i] + vowel_list.pop(0) + s[i+1:]
        return s