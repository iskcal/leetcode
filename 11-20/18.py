def fourSum(nums, target):
    if len(nums) < 4:
        return []
    else:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)-3):
            if i >=1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):    
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                start = j+1
                end = len(nums)-1
                acc = target - nums[i] - nums[j]
                while start < end:
                    if nums[start] + nums[end] > acc:
                        end -= 1
                    elif nums[start] + nums[end] == acc:
                        result.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start+1]: # 防止重复
                            start += 1
                        start += 1
                        end -= 1
                    else:
                        start += 1
        return result

if __name__ == '__main__':
    print(fourSum([0, 0, 0, 0], 0))