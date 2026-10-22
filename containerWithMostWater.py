# Container with most contain water
def maximumAreaContains(container):
    left = 0
    right = len(container) - 1
    maxArea = 0

    while left < right:
        width = right - left
        height = min(container[right] , container[left])
        area = width * height
        maxArea = max(maxArea,area) 

        if (container[left] > container[right]):
            right -= 1
        else:
            left += 1


    return maxArea

result = maximumAreaContains([12,45,78,21,65,45])
print(result)


