class Solution:
    # 记忆化回溯
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger > desiredTotal: 
            return True
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        state = [0] * (maxChoosableInteger + 1)
        res_dict = {}
        return self.backtrace_with_memo(desiredTotal, state, res_dict)
    def backtrace_with_memo(self, desiredTotal, state, res_dict):
        key = "".join([str(i) for i in state])
        if res_dict.get(key):
            return res_dict[key]
        for i in range(1, len(state)):
            if state[i] == 0:
                state[i] = 1
                # 如果当前选了i已经赢了或者选了i没有赢但是后面对方输了
                if (desiredTotal <= i or (not self.backtrace_with_memo(desiredTotal - i, state, res_dict))):
                    res_dict[key] = True
                    state[i] = 0  # 在返回之前回溯，重置被改变的值
                    return True
                # 如果不能赢也要记得回溯, 重置被改变的值
                state[i] = 0
        # 如果赢不了
        res_dict[key] = False
        return False

so = Solution()
res = so.canIWin(10, 40)
res