#이론적 방법 → 코드 안에서 연산 횟수를 세고 증가율 분석

def get_first_element(my_list):
    """리스트의 첫 번째 요소를 반환합니다."""
    return my_list[0]

# 입력 리스트의 크기가 10이든 1000이든 실행 시간은 동일합니다.
my_list = [1, 2, 3, 4, 5]

 # 이 코드의 시간복잡도는 O(1)입니다.

def find_max(my_list):
    """리스트에서 가장 큰 값을 찾습니다."""
    max_val = my_list[0]
    # for 루프는 리스트의 모든 요소를 한 번씩 순회합니다.
    # 리스트의 크기(n)가 커질수록 루프 횟수도 n에 비례하여 증가합니다.
    for element in my_list:
        if element > max_val:
            max_val = element
    return max_val

# 입력 리스트의 크기(n)에 비례하여 연산 횟수가 증가합니다.
# 이 코드의 시간복잡도는 O(n)입니다.

def find_duplicates(my_list):
    """리스트에 중복된 요소가 있는지 확인합니다."""
    for i in range(len(my_list)):
        # 첫 번째 for 루프: n번 실행
        for j in range(len(my_list)):
            # 두 번째 for 루프: n번 실행
            # 총 연산 횟수는 n * n = n^2에 비례합니다.
            if i != j and my_list[i] == my_list[j]:
                return True
    return False

# 입력 리스트의 크기(n)가 커질수록 연산 횟수는 n^2에 비례하여 증가합니다.
# 이 코드의 시간복잡도는 O(n^2)입니다.


def binary_search(sorted_list, target):
    """정렬된 리스트에서 이진 탐색을 수행합니다."""
    low = 0
    high = len(sorted_list) - 1
    # while 루프는 매번 탐색 범위를 절반씩 줄입니다.
    # 따라서 n이 2배가 되어도 루프 횟수는 1회만 증가합니다.
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 이진 탐색의 시간복잡도는 O(log n)입니다.


#실험적 방법 → 실행 시간을 측정해 복잡도를 추정
import time
import random

# 리스트에서 탐색 시간 측정
def measure_list_search(n):
    data = list(range(n))
    target = random.randint(0, n-1)

    start = time.time()
    target in data   # 탐색 연산
    end = time.time()

    return (end - start)

# 크기를 키워가며 실행 시간 확인
for n in [10**3, 10**4, 10**5, 10**6]:
    t = measure_list_search(n)
    print(f"n={n:7d}, 탐색시간={t:.8f}초")