#희소 행렬은 대부분의 요소가 0인 행렬을 메모리 효율적으로 저장하기 위한 구조

#파이썬에서 희소 행렬(Sparse Matrix)을 다루는 가장 일반적이고 효율적인 방법은 
#SciPy 라이브러리의 sparse 모듈을 사용하는 것

####################################
#1. 희소 행렬 저장 형식 (Formats)
#SciPy는 여러 희소 행렬 형식을 제공함
#1) Coordinate Format	COO	(행 인덱스, 열 인덱스, 값) 튜플 리스트로 저장. 생성과 변환이 빠름.
#2) Compressed Sparse Row	CSR	압축된 행 형식. 행렬 곱셈 및 행 기반 슬라이싱에 가장 효율적.

#################################
#5×5 크기의 행렬을 만들고, COO 형식으로 변환한 후, 이를 다시 CSR 형식으로 변환하는 예제

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix

# 1. 일반적인 5x5 행렬 (밀집 행렬)을 정의
# 희소 행렬을 만들기 위해 대부분의 요소를 0으로 설정
dense_matrix = np.array([
    [0, 0, 1, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 0, 0, 3],
    [4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

print("--- 1. 밀집 행렬 ---")
print(dense_matrix)

# 2. COO 형식으로 변환 (Coordinate Format)
# 행렬의 0이 아닌 요소만 (값, (행 인덱스, 열 인덱스)) 형태로 저장
sparse_coo = coo_matrix(dense_matrix)

print("\n--- 2. COO 형식 (값, 인덱스만 저장) ---")
# data: 0이 아닌 값들
# row: 해당 값들의 행 인덱스
# col: 해당 값들의 열 인덱스
print(f"데이터: {sparse_coo.data}")
print(f"행 인덱스: {sparse_coo.row}")
print(f"열 인덱스: {sparse_coo.col}")

# COO 형식의 메모리 사용량 (대략적인 비교)
coo_size = sparse_coo.data.nbytes + sparse_coo.row.nbytes + sparse_coo.col.nbytes
print(f"COO 메모리 사용 (추정): {coo_size} bytes")


# 3. CSR 형식으로 변환 (Compressed Sparse Row)
# 계산 효율을 높이기 위해 가장 많이 사용되는 형식
sparse_csr = sparse_coo.tocsr() # COO 객체에서 CSR로 쉽게 변환

print("\n--- 3. CSR 형식 (계산 최적화) ---")
# data: 0이 아닌 값들
# indices: 해당 값들의 열 인덱스
# indptr: 각 행이 시작하는 위치를 포인터로 나타냄 (압축의 핵심)
print(f"데이터: {sparse_csr.data}")
print(f"열 인덱스: {sparse_csr.indices}")
print(f"행 시작 포인터 (indptr): {sparse_csr.indptr}")


# 4. 희소 행렬을 다시 밀집 행렬로 복원
restored_matrix = sparse_csr.toarray()
print("\n--- 4. 복원된 밀집 행렬 ---")
print(restored_matrix)