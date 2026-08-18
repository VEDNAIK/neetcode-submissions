class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            temp = tuple(sorted(strs[i]))
            if temp in hashmap:
                hashmap[temp].append(i)
            else:
                hashmap[temp] = [i]
        ans = []
        for key in hashmap:
            temp = []
            for i in hashmap[key]:
                temp.append(strs[i])
            ans.append(temp)
        return ans

        