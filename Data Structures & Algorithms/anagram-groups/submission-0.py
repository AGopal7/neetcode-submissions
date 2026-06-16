class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups ={}
        for  words in strs:
            t = " ".join(sorted(words))
            if t  not in groups:
                groups[t]=[]
            groups[t].append (words)
        return list (groups.values())