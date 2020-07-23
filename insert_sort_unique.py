def insert_sort(arr):
    # 从第二个元素开始
    for i in range(1, len(arr)):
        # 基准是第二个元素
        key = arr[i]
        # 前一个元素index
        j = i - 1
        # 从右往左遍历
        # 寻找比key小的元素
        while j >= 0 and arr[j] > key:
            # arr[j] 比 key 大, 交换位置
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j = j - 1
        arr[j+1], key = key, arr[j + 1]
    pre = 0 # 要保留的元素index
    curr = pre + 1 
    while curr < len(arr):
        # 如果pre位置的元素等于curr的元素，curr继续向右移动
        while(arr[curr] == arr[pre]):
            curr = curr + 1
        # pre 向右移动一个位置, 为非重复元素插入位置
        pre = pre + 1
        arr[pre] = arr[curr]
        curr = curr + 1
    return arr[:pre+1]
            


def insert_sort(arr):
    # 用一个set存储所有的unique元素
    nums = set()
    # 记录重复次数
    dup_nums = 0
    i = 1
    nums.add(arr[0])
    while i < len(arr):
        key = arr[i]
        # 如果重复, 则i++, dup_nums ++
        if key in nums:
            dup_nums = dup_nums + 1
            i = i + 1
            continue
        # 不重复则加入nums
        nums.add(key)
        # j指针应该减去重复次数, 到达已排完序并且去重的区域
        j = i - 1 - dup_nums
        while j >= 0 and arr[j] > key:
             arr[j+1], arr[j] = arr[j], arr[j+1]
             j = j - 1
        arr[j+1], key = key, arr[j + 1]
        i = i + 1
    return arr[:len(arr)-dup_nums]




