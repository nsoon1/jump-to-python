#2-6 집합 자료형
#set 키워드를 사용해 만들 수 있음
# s1 = set([1,2,3])
# print(s1)
# s2 = set("Hello")
# print(s2)
#비어있는 집합 자료형은 s = set()로 만들 수 있음
#set의 특징 - 중복 x, 순서 x(unordered) - indexing 지원 x
#set 자료형을 인덱싱으로 접근하는 방법
#s1 = set([1,2,3]) # set 자료형 생성
#l1 = list(s1) #리스트로 set 자료형을 변경
#l1[0] # 이후 인덱싱으로 접근
#교집합 구하기
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# print(s1 & s2) # {4,5,6}
# print(s1.intersection(s2)) #{4,5,6}
#합집합 구하기
# print(s1 | s2) # {1,2,3,4,5,6,7,8,9}
# print(s1.union(s2)) #{1,2,3,4,5,6,7,8,9}\
#차집합 구하기
# print(s1 - s2) #{1,2,3}
# print(s2 - s1) #{8,9,7}
# print(s1.difference(s2))#{1,2,3}
# print(s2.difference(s1))#{8,9,7}
#값 1개 추가하기 -add
# s1 = set([1,2,3])
# s1.add(4)
# print(s1) # {1,2,3,4}
#값 여러개 추가하기 - update
# s1.update([4,5,6])
# print(s1) # {1,2,3,4,5,6}
#특정 값 제거하기 - remove
#s1.remove(2)
#print(s1) {1,3}