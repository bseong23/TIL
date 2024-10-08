### 리스트(Array)
- 여러 개의 값을 순서대로 저장하는 변경 가능한 시퀀스 자료형
- 리스트는 대괄호[]로 표기한다.
- 데이터로는 어떤 자료형도 저장 가능
- 리스트는 가변 (변경이 가능하다)

### 튜플
- 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형
- 튜플은 소괄호()로 표기한다.
- 데이터로는 어떤 자료형도 저장 가능
- 튜플은 불변(변경 불가)

- 리스트와 튜플은 거의 유사하다. 하지만 가변과 불변으로 리스트인지 튜플인지 나뉘게 된다.
<br> 그렇다면 튜플은 어디에서 쓰일까?

1. 튜플의 불변 특성을 사용한 안전하게 여러 개의 값을 전달, 그룹화, 다중 할당 등
2. 개발자가 직접 사용하기 보다 '파이썬 내부 동작'에서 주로 사용된다.

### range
- 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
- range(시작 값, 끝 값, 증가 값)
- range(n)
    - 0부터 n-1까지의 숫자 시퀀스
- range(n, m)
    - n부터 m-1까지의 숫자 시퀀스
- range 특징
    - 증가 값이 없으면 1씩 증가
    - 증가 값이 음수이면 감소 / 증가 값이 양수이면 증가
    - 증가 값이 0이면 에러
    - 증가 값이 음수이면 시작 값이 끝 값보다 작아야함
    - 증가 값이 양수이면 시작 값이 끝 값보다 커야 함
### dict 딕셔너리 (객체)
- key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형
- key는 변경 불가능한 자료형만 사용 가능
- value는 모든 자료형 사용 가능
- key를 통해서 value에 접근이 가능하다
### set 세트
- 순서와 중복이 없는 변경 가능한 자료형
- 중괄호{}로 표기 단, 빈 set를 표현할 때는 set()로 표기한다 왜? 그냥 {}는 딕셔너리꺼임..



### 오늘 푼 문제
오늘 배운 내용들을 토대로 문제를 풀었는데 깊은 복사에 대한 내용이 나왔다. 복사를 통해서 값을 변경하라길래 그냥 변수에 넣고 변경을 했는데 이것은 할당하는 것이기 때문에 같은 주솟값을 가르키고 있어서 할당된 값을 변경하면 원본 값이 같이 변경이 되었다. 
<br>그래서 파이썬에서는 깊은 복사라는 개념이 있었다. 모듈을 활용해서 deepcopy라는 모듈을 들고와서 사용하게 된다면 같은 주소를 가르키는 것이 아닌 새로운 list를 만들게 된다.

```python
from copy import deepcopy

catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

original_backup = catalog


backup_catalog = deepcopy(catalog)

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''
catalog[3] = ['성공을 향한 한 걸음', '내 삶의 변화', '목표의 달성의 비밀']

print('catalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.
print(catalog == backup_catalog)

print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)

```