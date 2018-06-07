def removeDuplicates(nums):
    if len(nums) in [0, 1]:
        return len(nums)
    count = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[count]:
            count = count + 1
            nums[count] = nums[i]

    return count + 1

if __name__ == '__main__':
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))