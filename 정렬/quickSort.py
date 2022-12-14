# 퀵 정렬 (Quick Sort)
# 시간 복잡도: O(NlogN), 최악의 경우 O(N**2)
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법.
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나.
# 가장 기본적인 퀵 정렬은 첫 번째 데이이터를 기준 데이터(Pivot)로 설정


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

#방법1: 
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while (left <= right):
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)

print("array:", array)

#방법2:

def quick_sort2(array):
    if len(array)<=1:
        return array
    pivot=array[0]
    tail=array[1:]

    left_side=[x for x in tail if x <=pivot]
    right_side=[x for x in tail if x>pivot]

    return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)
print("quick_sort2:",quick_sort2(array))