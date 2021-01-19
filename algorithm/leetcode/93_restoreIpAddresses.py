class Solution:
    def restoreIpAddresses(self, s):
        size = len(s)
        path = []
        res = []
        if size < 4 or size > 12: return []

        def dfs(path, s, depth, begin_index):
            if len(s) == 0:
                if depth == 4:
                    res.append(".".join(path))
                return
            if size - begin_index < (4 - depth) or size - begin_index > 3 * (4 - depth):
                return 
            for i in range(1, 4):
                if i > len(s): break
                ip_segment = s[:i]
                if is_valid(ip_segment):
                    #path.append(ip_segment)
                    dfs(path + [ip_segment], s[i:], depth + 1, begin_index + i)
                    #path.pop()
        def is_valid(ip_segment):
            if len(ip_segment) > 1 and ip_segment[0] == '0':
                return False
            if int(ip_segment) > 255:
                return False
            return True

        dfs(path, s, 0, 0)
        return res

so =  Solution()
a = so.restoreIpAddresses("25525511135")




            