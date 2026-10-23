class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]!="0":
            prev_prev=1 
        else:
            return 0
        if len(s)<2:
            return prev_prev
        if s[1]!="0" and int(s[:2])<=26:
            prev=2
        elif s[1]=="0" and int(s[:2])>26:
            return 0
        else:
            prev=1
        for i in range(2,len(s)):
            print(prev_prev,prev)
            temp=prev_prev
            prev_prev=prev
            prev=0
            if s[i]!="0":
                prev+=prev_prev
            if 10<=int(s[i-1:i+1])<=26:
                prev+=temp
            if prev==0:
                return 0
        return prev
