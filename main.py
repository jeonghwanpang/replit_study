a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[3])

#크기가 n이고, 모든 값이 0인 리스트 초기화
n = 10
a = [0] * n
print(a)

a = [7, 3, 2, 5, 9]
#인덱스 값을 이용해 원소 접근(인덱싱indexing)
a[4] = 4
print(a)
#뒤에서 세 번째 원소 출력
print(a[-3])
# 두 번째 원소부터 네 번째 원소까지(슬라이싱sli)
print(a[1 : 4])

#리스트 초기화 방법 리스트 컴프리헨션 획기적!
#0부터 9까지의 수 리스트
array = [i for i in range(10)]
print(array)