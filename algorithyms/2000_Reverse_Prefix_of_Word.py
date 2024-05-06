class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            pos = word.index(ch)
            # copy reversing the characters
            prefix_reversed = word[:pos+1][::-1]
            # add the following of them
            return prefix_reversed + word[pos+1:]
        else:
            return word