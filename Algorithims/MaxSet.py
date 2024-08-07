def max_independent_set(nums):

    t = [0 for i in range(len(nums))]
    t[0] = nums[0]
    t[1] = nums[1]
    for i in range(2, len(nums)):

        t[i] = max(nums[i], nums[i]+t[i-2], t[i-2], t[i-1])

    i = len(nums)-1
    list1 = []
    while (i > 1):
        if t[i] == t[i-1]:
            i -= 1
        elif t[i] == nums[i]:
            list1.append(nums[i])
            list1.reverse()
            return list1
        elif t[i] == t[i-2]+nums[i]:
            list1.append(nums[i])
            i = i-2
        else:
            i = i-2
    if i == 0:
        if (nums[i] > 0 or len(list1) == 0):
            list1.append(nums[i])
    else:
        t = max(nums[0], nums[1])
        if (t > 0 or len(list1) == 0):
            list1.append(t)
    list1.reverse()
    return list1
