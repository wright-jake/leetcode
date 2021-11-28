#example input
strs = ["flower","flow","flight"]

#solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #if nothing in the list of strings return ""
        if len(strs) == 0:
            return("")
        
        #if only one string in the list return that string
        if len(strs) == 1:
            return(strs[0])
        
        #first prefix in list
        pref = strs[0]
        
        #length of the prefix
        plen = len(pref)
        
        #loop through strings in list
        for s in strs[1:]:
            while pref != s[0:plen]:
                pref = pref[0:(plen-1)]
                plen -= 1
                
                if plen == 0:
                    return("")
                
        return pref
