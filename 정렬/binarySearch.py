# 이진 탐색 (Binary Search)
# 시간 복잡도: O(logN)
# 순타 탐색: 리스트 안에서 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.

# 방법1 : 재귀함수 사용
from xml.dom import minidom


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)


# 방법2: 반복문 구현

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
result2 = binary_search2(array, target, 0, n-1)
if result == None and result2==None:
    print("원소가 존재하지 않습니다.")
else:
    print("binary1:",result+1)
    print("binary2:",result2+1)
