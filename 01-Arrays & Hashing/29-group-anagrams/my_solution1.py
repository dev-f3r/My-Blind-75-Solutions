from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict to store lists of anagrams
        anagrams = defaultdict(list)

        # Iterate through each word in the input list of strings
        for w in strs:
            # Sort the characters in the word to create a unique key
            sorted_w = "".join(sorted(w))

            # Append the original word to the list associated with the sorted key
            anagrams[sorted_w].append(w)

        # Convert the values (lists of anagrams) to a list and return
        return list(anagrams.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(solution.groupAnagrams(["","b"]))
# print(solution.groupAnagrams(["vow","pam","vic","bee","ken","jay","oft","sue","joy","yuk","sac","mac","inc","big","icy","bus","lob","flo","day","aol","eel","rex","jug","man","cod","mix","guy","ken","ion","meg","tot","noe","ref","ito","inn","van","cry","tad"]))
