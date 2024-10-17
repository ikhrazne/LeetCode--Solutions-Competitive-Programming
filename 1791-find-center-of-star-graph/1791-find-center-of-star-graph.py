class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
        for index, edge in enumerate(edges):
            for i in edge:
                if i in edges[index + 1]:
                    if index + 2 <= len(edges) - 1:
                        if i in edges[index + 2]:
                            return i
                    else:
                        return i
        