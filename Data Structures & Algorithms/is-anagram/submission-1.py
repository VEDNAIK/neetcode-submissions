class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        len_s = len(s)
        len_t = len(t)
        if len_s != len(t):
            return False
        for i in range(len_s):
            if s[i] not in hashmap_s:
                hashmap_s[s[i]] = 1
            else:
                hashmap_s[s[i]] += 1
            if t[i] not in hashmap_t:
                hashmap_t[t[i]] = 1
            else:
                hashmap_t[t[i]] += 1
        for i in range(len_s):
            if s[i] not in hashmap_t or hashmap_s[s[i]] != hashmap_t[s[i]]:
                return False
        return True
        
        