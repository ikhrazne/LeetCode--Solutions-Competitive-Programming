class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return re.findall(p, s)[0] == s if len(re.findall(p, s)) > 0 else False
        