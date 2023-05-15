def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    index = 0
    substring = set()
    for i in range(len(s)):
        if s[i] in substring:
            while s[i] in substring:
                substring.remove(s[index])
                index += 1
        substring.add(s[i])
        if len(substring) > res:
            res = len(substring)
    return res


print(lengthOfLongestSubstring("ohvhjdml"))
