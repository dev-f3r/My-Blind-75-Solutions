class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # Initialize an empty string to store the encoded result
        res = ""

        # Iterate through each string in the list
        for s in strs:
            # Append the length of the string, followed by '#', and then the string itself
            res += str(len(s)) + "#" + s

        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s):
        # Initialize an empty list to store the decoded result
        res, i = [], 0

        # Iterate through the string
        while i < len(s):
            # Find the position of the '#' delimiter
            j = i
            while s[j] != "#":
                j += 1

            # Extract the length of the string
            length = int(s[i:j])

            # Append the substring (actual string content) to the result list
            res.append(s[j + 1 : j + 1 + length])

            # Move the index to the next position after the current string
            i = j + 1 + length

        return res
