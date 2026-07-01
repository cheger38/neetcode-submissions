class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        for i in range(len(s)//2):
            if s[i] != s[-(i + 1)]:
                return False
        
        return True

        


