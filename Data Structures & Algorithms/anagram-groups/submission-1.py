class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for w in strs:
            key = tuple(sorted(w))
            if key in dict1:
                dict1.get(key).append(w)
            else:
                dict1[key] = [w]
        return list(dict1.values())