#2-5 딕셔너리 자료형
#딕셔너리 - 말 그대로 사전이라는 뜻. Key와 Value를 한 쌍으로 가짐. ex) Key = "baseball", Value = "야구"
#리스트, 튜플과 달리 순차적으로 요솟값을 구하지 않고 Key를 통해 Value를 얻음.
#딕셔너리의 기본형
#{Key1: Value1, Key2: Value2, Key3: Value3, ...}
#Key와 Value의 쌍 여러개가 {}로 둘러싸여있고, 각각의 요소는 Key: Value 형태로 이루어져있고, 쉼표(,)로 구분
#dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
#a= {1: 'hi'} #정숫값 1을 key로 사용
#a = {'a': [1,2,3]} # Value에 리스트를 사용
#딕셔너리 쌍 추가하기
#a = {1: 'a'}
#a[2] = 'b' # {2: 'b'} 쌍 추가
#print(a) # {1: 'a', 2: 'b'}
#a['name'] = 'pey' # {name: 'pey'} 쌍 추가
#print(a) # {1: 'a', 2: 'b', name: 'pey'}
#a[3] = [1,2,3] # {3: [1,2,3]} TKd cnrk
#print(a) # {1: 'a', 2: 'b', name: 'pey', 3: [1,2,3]}
#딕셔너리 요소 삭제하기
#del a[1] # Key가 1인 Key: Value 쌍 삭제
#print(a) # {2:'b', name: 'pey', 3: [1,2,3]}
#딕셔너리에서 Key를 사용해 Value 얻기
# grade = {'pey': 10, 'julliet' : 99}
# print(grade['pey']) #Key가 'pey'인 딕셔너리의 Value를 반환
# print(grade['julliet']) #Key가 'julliet'인 딕셔너리의 Value를 반환
# a = {1: 'a', 2: 'b'}
# print(a[1]) #Key가 1인 요소의 Value를 반환
# print(a[2]) #Key가 2인 요소의 Value를 반환
#딕셔너리 만들 때 주의 사항
#딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨.
#a = {1: 'a', 1: 'b'}
#print(a) # {1: 'b'}
#Key에는 리스트를 쓸 수 없음. 하지만 튜플은 Key로 쓸 수 있음.
#딕셔너리의 Key로 쓸 수 있느냐, 없느냐는 Key가 변하는 값인지, 변하지 않는 값인지에 달려있음. 리스트는 그 값이 변할 수 있으므로 Key로 쓸 수 없음
#딕셔너리 관련 함수
#key 리스트 만들기 - keys
#a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
#print(a.keys()) # dict_keys(['name','phone,'birth'])
#dict_keys 객체를 리스트로 변환하려면?
#list(a.keys()) # ['name', 'phone, 'birth']
#value 리스트 만들기 - values
#print(a.values()) # dict_values(['pey', '010-9999-1234', '1118'])
#Key, Value 쌍 얻기 - items
#print(a.items()) # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])
#Key: Value 쌍 모두 지우기 - clear
#a.clear()
#print(a) # {}
#key로 Value 얻기 - get
#a.get('name') #'pey'
#a.get('phone') # '010-9999-1234'
#print(a.get('nokey')) #컴파일 에러가 아닌 None 출력
#get(x,'디폴트 값') 사용시 key가 없을경우 디폴트 값을 출력
#print(a.get('nokey','foo')) # 'foo'
#해당 Key가 딕셔너리 안에 존재하는지 조사하기 - in
#print('name' in a) # True
#print('email' in a) # False