# solution: https://www.youtube.com/watch?v=5QpMpO2CAb0

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        problem_letters=[]
        flag=True
        counter=Counter(s)
        for letter in counter:
            if counter[letter]<k:
                problem_letters.append(letter)
                flag=False
        if flag:
            return len(s)
        
        for letter in problem_letters:
            s=s.replace(letter,' ')
        strings_after_divide=s.split()
        ans=0
        for string in strings_after_divide:
            ans=max(ans,self.longestSubstring(string,k))
        return ans
        
