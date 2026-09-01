class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        result = 0

        for char in char_set:
            l, count = 0, 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1
            
            # If we need to make more substitutions than allowed, substring is invalid
            # when window becomes invalid, move over one char at a time until new char.
                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1

                result = max(result, r - l + 1)
        return result
