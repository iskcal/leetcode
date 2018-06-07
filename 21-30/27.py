def removeElement(nums, val):
    if len(nums) == 0:
        return 0
    else:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count = count + 1
        return count

if __name__ == '__main__':
    print(removeElement([0,1,2,2,3,0,4,2], 2)) 