def threeSum(nums):
    if len(nums) < 3:
        return []
    else:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i >=1 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = len(nums)-1
            acc = -nums[i]
            while start < end:
                if nums[start] + nums[end] > acc:
                    end -= 1
                elif nums[start] + nums[end] == acc:
                    result.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]: # 防止重复
                        start += 1
                    start += 1
                    end -= 1
                else:
                    start += 1
        return result

if __name__ == '__main__':
    print(threeSum([0,0,0]))