# 给你一个 下标从 0 开始 的正整数数组w ，其中w[i] 代表第 i 个下标的权重。
#
# 请你实现一个函数pickIndex，它可以 随机地 从范围 [0, w.length - 1] 内（含 0 和 w.length - 1）选出并返回一个下标。选取下标 i的 概率 为 w[i] / sum(w) 。
#
# 例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3)= 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3)= 0.75（即，75%）。
import random


class Solution:
    # pre_sum = [] 这样写为错误写法
    def __init__(self, w: list[int]):
        self.w = w
        cnt = 0
        # 类变量和成员变量不能混，否则导致多次实例化类带有记忆
        self.pre_sum = [0]
        for i in self.w:
            cnt += i
            self.pre_sum.append(cnt)
        print('presum:',self.pre_sum)

    def search_max_less_or_equal(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return r

    def pickIndex(self) -> int:
        i = random.randint(0, self.pre_sum[-1]-1)
        print('i:',i)
        return self.search_max_less_or_equal(self.pre_sum,i)



# Your Solution object will be instantiated and called as such:
obj = Solution([1,3])
for _ in range(4):
    param_1 = obj.pickIndex()
    print('res:',param_1)