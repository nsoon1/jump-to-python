#2-2 문자열 자료형
#문자열(string) - 문자,단어 등으로 구성된 문자들의 집합, 따옴표로 둘러싸여 있으면 모두 문자열(ex. "123"은 숫자형이 아닌 문자열)
#4가지 문자열 사용 방법
#1. 작은 따옴표(' ') 사용
#2. 큰 따옴표(" ") 사용
#3. 작은 따옴표 3개(''' ''') 사용
#4. 큰 따옴표 3개(""" """) 사용
#왜 문자열 사용 방법이 4개나 존재하는가?
#문자열 안에 큰 따옴표나 작은 따옴표가 존재하는 경우, 문자열을 감싸는 따옴표과 구분하기 위해서 사용
#이외에도 이스케이프 코드를 사용하여 따옴표를 표현할 수 있음
#이스케이프 코드 - \로 시작하는 문자 조합들
#\n - 줄 바꿈(new line)
#\t - 탭(tab)
#\\ - 문자 \ 자체
#\' - 작은 따옴표
#\" - 큰 따옴표
#\r - 캐리지 리턴(carriage return), 줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동
#\f - 폼 피드(form feed), 줄 바꿈 문자, 커서를 다음 줄로 이동
#\a - 벨(bell), 경고음 발생
#\b - 백스페이스(backspace), 커서를 한 칸 뒤로 이동
#\000 - 널 문자(null character)
# 활용 빈도가 높은 것은 \n, \t, \\, \', \", 나머지는 거의 사용하지 않음
#연속된 따옴표 3개를 사용하는 방법은, 여러 줄을 문자열로 표현할 때 유용
#\n을 통해서 직접 줄바꿈을 할 수도 있음

#print("Life is too short,\n You need python")

#문자열 연산
#문자열 더하기
# head = "Python"
# tail = " is fun!"
# print(head + tail) # 문자열 더하기 연산 결과 : Python is fun!
# 문자열 곱하기
# a = "Python"
# print(a * 2) # 문자열 곱하기 연산 결과 : PythonPython
# print ("=" * 50)
# print ("My Program")
# print ("=" * 50)
#문자열 길이 구하기
#len 함수 - 파이썬 기본 내장 함수
# a = "Life is too short"
# print(len(a)) # 문자열 길이 : 17
#'You need python' 문자열의 길이를 구해보자
# print (len("You need python"))

#문자열 인덱싱, 슬라이싱
#인덱싱(indexing) - 무엇인가를 가리킨다는 의미, 슬라이싱(slicing) - 무엇인가를 잘라낸다는 의미
#a = "Life is too short, You need Python"
#각각의 문자들은 인덱스(index)라는 고유한 번호를 가지고 있음
#인덱스는 0부터 시작, ex) L(0) i(1) f(2) e(3) (4) i(5) s(6) ...
# print(a[3]) #인덱스 3(4번째 문자) 출력 : e
# print(a[-1]) # 음수 인덱스 - 문자열을 뒤에서부터 읽음. -1은 마지막 문자, -2는 마지막에서 두번째 문자 ... -0의 경우 0과 동일하므로 첫번째 문자.
#문자열 슬라이싱
# print(a[0:4]) # 인덱스 0부터 4직전까지(0,1,2,3) 출력 : Life, a[p:q] - p부터 q 직전까지 (q 미포함)
# print(a[p:q])에서, p를 생략하면 처음부터, q를 생략하면 끝까지 의미
# 슬라이싱의 경우에도 음수 사용 가능 ex) print(a[-4:-1]) # Pyt 출력
#슬라이싱으로 문자열 나누기
# a = "20230331Rainy"
# date = a[:8] # 인덱스 0부터 8 직전까지(8 미포함) : 20230331
# print(date)
# weather = a[8:] # 인덱스 8부터 끝까지 : Rainy
# print(weather)
# 더 세분화 하는 방법
# year = a[0:4] # 인덱스 0부터 4 직전까지 : 2023
# day = a[4:8] # 인덱스 4부터 8 직전까지 : 0331
# print(year)
# print(day)
# print(weather)
# print("지금은 " + year + "년 " + day + "일이고, 날씨는 " + weather + " 입니다." )

#문자열 포매팅
#포매팅(formatting) - 문자열 안에 특정 값을 삽입하는 방법
# 1. 숫자 바로 대입
#print(" I eat %d apples." %3)
# 2. 문자열 바로 대입
#print("I eat %s apples." %"five")
# 3. 숫자 값을 나타내는 변수로 대입
# number = 3
# print("I eat %d apples." %number)
# 4. 2개 이상의 값 넣기
# number = 10
# day = "three"
# print("I ate %d apples. so I was sick for %s days." %(number, day))
# print("I ate %d apples. so I was sick for %s days." % (10, "three"))
#문자열 포맷 코드
# %s - 문자열(string)
# %c - 문자 1개(character)
# %d - 정수(integer)
# %f - 부동소수(floating-point)
# %.숫자f - 소수점 특정 자리수까지 표현
# %o - 8진수(octal)
# %x - 16진수(hexadecimal)
# %% - 문자 % 자체
# %s 포맷 코드는 어떤 형태의 값이든지 모두 문자열로 바꾸어 삽입
# print ("I have %s apples." %3)
# 포매팅 연산자와 %를 같이 사용할때는 %%를 사용
# print("Error is %d%." %98) - Error is 98%.의 출력을 기대하겠지만, 에러가 발생
# print("Error is %d%%." %98) # Error is 98%.로 제대로 출력됨.
# %를 직접 표기하고 싶을 때는 따옴표 안에 직접 적어도 되지만, 포매팅 연산자와 함께 사용할 때는 %%를 사용해야 함.

#포맷 코드와 숫자 함께 사용하기
#1. 정렬과 공백
#print("%10s" %"hi") # 전체 길이 10칸 중에서 오른쪽 정렬로 hi 출력 출력 - "        hi"
#print("%-10sjane" %"hi") # 전체 길이 10칸 중에서 왼쪽 정렬로 hi 출력 - "hi        jane"
#2. 소수점 표현하기
#print("%0.4f" %3.14159265359) # 소수점 4자리까지 표현 : 3.1416 
# 소수점 포인트 앞의 숫자는 문자열 전체 길이를 의미, 0이면 전체 길이 상관없이 출력, 생략하면 0과 같은 의미로 작동
#print("%10.4f" %3.42134234) # 전체 길이 10, 소수점 4자리까지 표현 :     3.4213
#print("%10.4f" %50124922412.12334556) # 출력 50124922412.1233. 전체 길이가 최소 10이라는 것이지, 10을 넘어가는 경우 넘게 출력됨.
#format 함수를 사용한 포매팅
#1. 숫자 바로 대입
# print("I eat {0} apples." .format(3)) # 문자열중 {0} 위치에 format 함수의 첫번째 인자 3이 대입됨.
#2. 문자열 바로 대입
# print("I eat {0} apples." .format("five")) # 문자열중 {0} 위치에 format 함수의 첫번째 인자 "five"가 대입됨.
#3. 숫자 값을 나타내는 변수로 대입
# number = 3
# print("I eat {0} apples." .format(number)) # 문자열중 {0} 위치에 format 함수의 첫번째 인자 number가 대입됨.
#4. 2개 이상의 값 넣기
# number = 10
# day = "three"
# print("I ate {0} apples. so I was sick for {1} days." .format(number, day)) # 문자열중 {0} 위치에 format 함수의 첫번째 인자 number가, {1} 위치에 두번째 인자 day가 대입됨.
#중괄호 안에 인덱스 번호를 생략할 수도 있음
# print("I ate {} apples. so I was sick for {} days." .format(number, day)) # 인덱스 번호 생략 가능
#중괄호 안에 인덱스 번호를 마음대로 지정할 수도 있음
# print("I ate {1} apples. so I was sick for {0} days." .format(day, number)) # 인덱스 번호 마음대로 지정 가능
#이름으로 넣기
# print("I ate {number} apples. so I was sick for {day} days." .format(number=10, day="three"))
#인덱스와 이름을 혼용해서 넣기
# print("I ate {0} apples. so I was sick for {day} days." .format(10, day="three"))
#왼쪽 정렬
#print("{0:<10}" .format("hi")) # 전체 길이 10칸 중에서 왼쪽 정렬로 hi 출력 : "hi        "
#오른쪽 정렬
#print("{0:>10}" .format("hi")) # 전체 길이 10칸 중에서 오른쪽 정렬로 hi 출력 : "        hi"
#가운데 정렬
#print("{0:^10}" .format("hi")) # 전체 길이 10칸 중에서 가운데 정렬로 hi 출력 : "    hi    "
#공백 채우기
#print("{0:=^10}" .format("hi")) # 전체 길이 10칸 중에서 가운데 정렬로 hi 출력, 공백 채우기 문자 = 사용 : "====hi===="
#print("{0:!<10}" .format("hi")) # 전체 길이 10칸 중에서 왼쪽 정렬로 hi 출력, 공백 채우기 문자 ! 사용 : "hi!!!!!!!!"
#소수점 표현하기
#print("{0:0.4f}" .format(3.14159265359)) # 소수점 4자리까지 표현 : 3.1416
#print("{0:10.4f}" .format(3.42134234)) # 전체 길이 10, 소수점 4자리까지 표현 :     3.4213
#{ 또는 } 문자 표현하기
#print("{{ and }}" .format()) # {와 } 문자 표현하기 : { and } {{처럼 {를 두 번 적으면 { 문자 하나로 인식됨. }}도 마찬가지.
#f 문자열 포매팅 (파이썬 3.6버전 이상에서 사용 가능)
#문자열 앞에 f 또는 F를 붙이면 문자열 안에 중괄호{}를 사용해 변수나 표현식을 삽입할 수 있음
#name = "홍길동"
#age = 30
#print(f"나의 이름은 {name}입니다. 나이는 {age}살입니다.") # 나의 이름은 홍길동입니다. 나이는 30살입니다.
# print(f"나의 이름은 {name}입니다. 나이는 {age+1}살입니다.") # 나의 이름은 홍길동입니다. 나이는 31살입니다.
#정렬과 공백
#print(f"{'hi':<10}") # 전체 길이 10칸 중에서 왼쪽 정렬로 hi 출력 : "hi        "
#print(f"{'hi':>10}") # 전체 길이 10칸 중에서 오른쪽 정렬로 hi 출력 : "        hi"
#print(f"{'hi':^10}") # 전체 길이 10칸 중에서 가운데 정렬로 hi 출력 : "    hi    "
#print(f"{'hi':=^10}") # 전체 길이 10칸 중에서 가운데 정렬로 hi 출력, 공백 채우기 문자 = 사용 : "====hi===="
#print(f"{'hi':!<10}") # 전체 길이 10칸 중에서 왼쪽 정렬로 hi 출력, 공백 채우기 문자 ! 사용 : "hi!!!!!!!!"
#소수점 표현하기
#print(f"{3.14159265359:0.4f}") # 소수점 4자리까지 표현 : 3.1416
#print(f"{3.42134234:10.4f}") # 전체 길이 10, 소수점 4자리까지 표현 :     3.4213
#{ 또는 } 문자 표현하기
#print(f"{{ and }}") # {와 } 문자 표현하기 : { and }
# format 함수 또는 f 문자열 포매팅을 사용해 !!!python!!!문자열을 출력하기
# print(f"{'python':!^12}")
#문자열 관련 함수들
# 문자열 내장 함수는 문자열 변수 이름 뒤에 '.'을 붙인 후 함수 이름을 사용
#1. count 함수 - 문자열 내에 특정 문자가 몇 개 있는지 세는 함수
# a= "hobby"
# print(a.count('b')) # b문자가 몇 개 있는지 세기 : 2
#2. find 함수 - 특정 문자가 문자열 내에 존재하는지 확인하고, 존재한다면 그 위치(인덱스)를 알려주는 함수
# a= "Python is the best choice"
# print(a.find('b') ) # b문자의 위치(인덱스) 확인 : 14
# print(a.find('k') ) # k문자가 존재하지 않으므로 -1 반환 : -1
#3. index 함수 - find 함수와 동일하게 특정 문자의 위치(인덱스)를 알려주는 함수, 단, 문자열 내에 특정 문자가 존재하지 않으면 오류 발생
# a = "Life is too short"
# print(a.index('t')) # t문자의 위치(인덱스) 확인 : 8
# print(a.index('k')) # k문자가 존재하지 않으므로 오류 발생
#4. join 함수 - 문자열 삽입 함수, 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 함수
# print(",".join('abcd')) # abcd 문자열 각각의 문자 사이에 , 삽입 : a,b,c,d
# print(",".join(['a', 'b', 'c', 'd'])) # ['a', 'b', 'c', 'd'] 리스트의 각 문자 사이에 , 삽입 : a,b,c,d"
#5. upper 함수 - 문자열을 모두 대문자로 변환하는 함수
# a = "hi"
# print(a.upper()) # hi 문자열을 모두 대문자로 변환 : HI
#6. lower 함수 - 문자열을 모두 소문자로 변환하는 함수
# a = "HI"
# print(a.lower()) # HI 문자열을 모두 소문자로 변환 : hi
#7. lstrip 함수 - 문자열 왼쪽에 존재하는 특정 문자들을 제거하는 함수, 별도의 인자가 없으면 공백 문자 제거
# a = "  hi  "
# print(a.lstrip()) # 문자열 왼쪽의 공백 문자 제거 : "hi  "
#8. rstrip 함수 - 문자열 오른쪽에 존재하는 특정 문자들을 제거하는 함수, 별도의 인자가 없으면 공백 문자 제거
# a = "  hi  "
# print(a.rstrip()) # 문자열 오른쪽의 공백 문자 제거 : "  hi"
#9. strip 함수 - 문자열 양쪽에 존재하는 특정 문자들을 제거하는 함수, 별도의 인자가 없으면 공백 문자 제거
# a = "  hi  "
# print(a.strip()) # 문자열 양쪽의 공백 문자 제거 : hi
# b = "!!hi!!!"
# print(b.strip("!")) # 문자열 양쪽의 ! 문자 제거 : hi
#10. replace 함수 - 문자열 내의 특정 문자들을 다른 문자들로 바꾸는 함수. replace(바뀔_문자열, 바꿀_문자열)
# a = "Life is too short"
# print(a.replace("Life", "Your leg")) # Life 문자열을 Your leg 문자열로 바꾸기 : Your leg is too short
#11. split 함수 - 문자열을 특정 문자를 기준으로 나누어 리스트로 만드는 함수, 별도의 인자가 없으면 공백 문자를 기준으로 나눔
# a = "Life is too short"
# print(a.split()) # 공백 문자를 기준으로 문자열 나누기 : ['Life', 'is', 'too', 'short']
# b = "a:b:c:d"
# print(b.split(":")) # : 문자를 기준으로 문자열 나누기 : ['a', 'b', 'c', 'd']