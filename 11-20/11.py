def maxArea(height):
    maxV = 0
    start = 0
    stop = len(height) - 1
    while start < stop:
        curV = (stop - start) * min(height[start], height[stop])
        maxV = curV if curV > maxV else maxV
        if height[start] >= height[stop]:
            stop -= 1
        else:
            start += 1
    return maxV

if __name__ == '__main__':
    print(maxArea([2, 4, 8]))
