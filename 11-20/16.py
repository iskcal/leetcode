def threeSumClosest(nums, target):
    if len(nums) < 3:
        return []
    else:
        result = 0
        dif = float('inf') # 初始无穷大
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i >=1 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = len(nums)-1
            while start < end:
                cur_dif = nums[i] + nums[start] + nums[end] - target
                if abs(cur_dif) < dif:
                    dif = abs(cur_dif)
                    result = nums[i] + nums[start] + nums[end]
                
                if cur_dif >= 0:
                    end -= 1
                else:
                    start += 1
        return result

if __name__ == '__main__':
    print(threeSumClosest([1,1,-1,-1,3],  3))