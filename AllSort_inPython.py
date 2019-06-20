def bubble_sort(arr):
    """冒泡排序"""

    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def selection_sort(arr):
    """简单选择排序"""
    for i in range(0, len(arr)):
        # 设置哨兵， 哨兵由i担当
        min_index = i
        # 寻找比哨兵位置的值更小的，找到了则替换哨兵员
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # 若哨兵员发生变换则替换两者的值
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


def insertion_sort(arr):
    """直接插入排序"""
    for i in range(len(arr)):
        # 待比较数值的前一位索引号
        preindex = i - 1
        # 待比较数的值
        current = arr[i]
        # 不断的与前面已排好序的数比较，待比较的数较小的话则不断的
        # 把较的数往后移动，直至队列的头部
        while preindex >= 0 and arr[preindex] > current:
            arr[preindex + 1] = arr[preindex]
            preindex -= 1
        # 找到比待比较数小的位置，插入到该位置
        arr[preindex + 1] = current
    return arr


def shell_sort(arr):
    # 设置增量
    increment = len(arr)//3 + 1
    # 增量最小间隔
    while increment > 0:
        for i in range(increment, len(arr)):
            # 进行插入排序
            while i >= increment and arr[i] < arr[i - increment]:
                arr[i], arr[i - increment] = arr[i - increment], arr[i]
                # 跳跃式移动 将越后面的数多经历几次比较防止初始位置在很后面，
                # 但是数值又很小的数，还被放到了中间。从而实现基本有序
                i -= increment
        # 为了防止死循环，incremen =1 只能有1次，排序后将跳出循环
        if increment == 1:
            break
        # 改变增量 增量必须保证有相邻排序的，因此是int(increment/3) + 1
        increment = len(arr)//3 + 1
    return arr


def heap_sort(arr):
    """
堆排序-待排序序列构成大顶堆，堆顶（最大值与数组尾交换）
将剩余n-1序列重构成一个堆，可得n元素中次大值，反复执行，最终得到有序序列
    :param arr: 待排序序列
    """
    arr_length = len(arr)
    # 初始数组排序成为一个大顶堆
    for i in range(arr_length // 2, arr_length):
        heap_adjust(arr, arr_length - 1 - i, arr_length - 1)
    # 堆顶（最大值与数组尾交换）
    # 将剩余n-1序列重构成一个堆，可得n元素中次大值，反复执行，最终得到有序序列
    for i in range(arr_length):
        arr[0], arr[arr_length - 1 - i] = arr[arr_length - 1 - i], arr[0]
        # 列表从0开始，初始就输出了一个最大值，列表待排序数为length-1
        # 列表里待排序的最后一位是索引值是 length-2
        heap_adjust(arr, 0, arr_length - 2 - i)


def heap_adjust(arr, s, m):
    """
其中两个待解决问题，初始无序序列变成大顶堆
输出堆顶数，同时调整剩余元素成为新堆
    :param arr: 待排序序列
    :param s: 待排序比较的数值的起始值
    :param m: 待排序比较的数值的范围末尾
    """
    temp = arr[s]
    # 两倍s是二叉树的性质，孩子节点与双亲节点的层序编号的二倍性质
    for j in range(2 * s, m):
        # j保留左右孩子节点中值较大的层序编号
        if arr[j] < arr[j + 1]:
            j += 1
        # 默认下层已排序好，根节点的值比孩子节点的值大，结束循环
        if temp > arr[j]:
            break
        arr[s] = arr[j]
        s = j
        j *= 2
    arr[s] = temp


def merging(left, right):
    """
归并排序算法， 从网上找到的代码
#https://www.cnblogs.com/Lin-Yi/p/7309143.html
    :param left: 有序的左边序列
    :param right: 有序的右边序列
    :return:返回排列好的序列
    """
    result = []
    while len(left) > 0 and len(right) > 0:
        # 比较有序序列的首部，选择两者最小的
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 如果有剩余的，则无需比较可以直接加入最终列表
    if len(left) != 0:
        result += left
    if len(right) != 0:
        result += right
    return result


def merging_sort(arr):
    # 迭代的出口，拆分至最小的单个元素时，不再继续拆分
    if len(arr) == 1:
        return arr
    # 不断的迭代折半拆分
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    l1 = merging_sort(left)
    r1 = merging_sort(right)
    # 最后一次迭代时，合并已经排序好的左右两边子序列
    return merging(l1, r1)


def qsort(arr, low, hight):
    """
快速排序-分割两端
    :param arr: 待排序序列
    :param low: 序列起始
    :param hight: 序列终止
    """
    if low < hight:
        # 找到一个关键位置（枢轴值）的使得两边的数满足，左边的数都小于枢轴值
        # 右边的数都大于枢轴值
        pivot = partition(arr, low, hight)
        # 对两端继续分割
        qsort(arr, low, pivot - 1)
        qsort(arr, pivot + 1, hight)


def partition(arr, low, hight):
    """
快速排序的核心代码-寻找待排序数组中的枢轴值
    :param arr: 待排序数组
    :param low: 待排序数组起始端
    :param hight: 待排序数组的终止端
    :return: 返回枢轴值
    """
    # 枢轴值初始设为数组的的起始位置
    pivotkey = arr[low]
    while low < hight:
        # 从高位比较与枢轴值的大小，若比枢轴值小则交换到低位
        while low < hight and arr[hight] >= pivotkey:
            hight -= 1
        arr[hight], arr[low] = arr[low], arr[hight]
        # 从低位比较与枢轴值的大小，若比枢轴值大则交换到高位
        while low < hight and arr[low] <= pivotkey:
            low += 1
        arr[hight], arr[low] = arr[low], arr[hight]
    # 这个数组中枢轴值所在的位置
    return low


def quicksort(arr):
    """
快速排序
    :param arr: 待排序序列
    """
    qsort(arr, 0, len(arr) - 1)


arr = [3, 38, 5, 8, 41, 50, 12, 36, 21, 4, 19, 2, 31]
# bubble_sort(arr)
# selection_sort(arr)
# shell_sort(arr)
# heap_sort(arr)
# result = merging_sort(arr)
# print(result)
quicksort(arr)
print(arr)
