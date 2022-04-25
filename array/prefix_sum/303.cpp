//给定一个整数数组 nums，处理以下类型的多个查询:
//
//计算索引left和right（包含 left 和 right）之间的 nums 元素的 和 ，其中left <= right
//实现 NumArray 类：
//
//NumArray(int[] nums) 使用数组 nums 初始化对象
//int sumRange(int i, int j) 返回数组 nums中索引left和right之间的元素的 总和 ，包含left和right两点（也就是nums[left] + nums[left + 1] + ... + nums[right])

class NumArray {
public:
    vector<int> preSum;
    NumArray(vector<int>& nums) {
        preSum.push_back(0);
        for(int i=0;i<nums.size();i++){
            preSum.push_back(nums[i]+preSum[i]);
        }
    }

    int sumRange(int left, int right) {
        return preSum[right+1] - preSum[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */