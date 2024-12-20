def quick_sort(start, end, array):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if array[left] > array[pivot] > array[right]:
            array[left], array[right] = array[right], array[left]

        if array[left] <= array[pivot]:
             left += 1

        if array[right] >= array[pivot]:
             right -= 1

    array[pivot], array[right] = array[right], array[pivot]

    quick_sort(start, right - 1, array)
    quick_sort(left, end, array)


array = list(map(int, input().split()))
quick_sort(0, len(array) - 1, array)

print(' '.join(map(str, array)))