class Solution:
    def isValid(self, s: str) -> bool:
        # save open and remove when see valid closed
        pairs={"(":")","{":"}","[":"]"}
        curr=[]
        for p in s:
            if p in pairs:
                curr.append(p)
            else:
                if not curr:
                    return False
                last=curr.pop()
                if pairs[last]!=p:
                    return False
        if curr:
            return False
        return True

