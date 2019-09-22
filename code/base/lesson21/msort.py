def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
        print( "i= ", i)
        for j in range(len(nums) - i - 1):  # j为列表下标
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                print("j = ", j)
                print(nums)
            else:
                print("else j = ", j)

    return nums


print(bubble_sort([45, 32, 8, 33, 12, 22, 19, 97]))
# 输出：[8, 12, 19, 22, 32, 33, 45, 97]