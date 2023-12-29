from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)  # mapping charCount to List of Anagrams

        for s in strs:
            count = [0] * 26  # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())


solution = Solution()
solution.groupAnagrams(["ate", "tea", "tan"])

""" 
This Python script is designed to group anagrams from a given list of strings. Here's a breakdown of what each part of the code does:

from collections import defaultdict: This line imports the defaultdict class from the collections module. A defaultdict is a dictionary subclass that calls a factory function to supply missing values, which is useful when the dictionary keys are not known in advance.

class Solution:: This line defines a class named Solution.

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:: This line defines a method named groupAnagrams within the Solution class. This method takes a list of strings as input and returns a list of lists of strings.

res = defaultdict(list): This line creates a defaultdict object named res. The default value of any new key will be an empty list. This dictionary will map character counts to lists of anagrams.

The for loop starting at line 7 iterates over each string in the input list. For each string, it does the following:

Initializes a list count with 26 zeros. This list will hold the counts of each letter in the string (assuming all strings are lowercase).
The inner for loop starting at line 10 iterates over each character in the string and increments the corresponding count in the count list.
Appends the string to the list in the res dictionary that corresponds to the tuple representation of the count list.
return res.values(): This line returns the values of the res dictionary, which are the lists of anagrams.

solution = Solution(): This line creates an instance of the Solution class named solution.

solution.groupAnagrams(["ate", "tea", "tan"]): This line calls the groupAnagrams method on the solution object with the input ["ate", "tea", "tan"]. This will group the anagrams from the input list and return the groups.
"""
