# Module

### 모듈이란?
- 과학자, 수학자가 모든 이론을 새로 만들거나 증명하지 않는 것처럼<br>개발자 또한 프로그램 전체를 모두 혼자 힘으로 작성하는 것은 드문 일
- 이미 다른 프로그래머가 이미 작성해 놓은 수천, 수백만 줄의 코드를 사용하는<br>것은 생산성에서 매우 중요한 일
  
#### 모듈 `Module`
- 한 파일로 묶인 변수와 함수의 모음<br>특정한 기능을 하는 코드가 작성된 파이썬 파일(`.py`)

### 모듈 import (js와 거의 유사하나, 조금 다른듯.. export안해줘도 되는 거 같음, 그냥 import로 파일 가져와서 사용하면 되는 듯?)
- import문과 from문의 차이...
- import문만 들고오게 된다면 math.sqrt처럼 math를 사용해줘야하고 
- from문을 사용하게 된다면 sqrt만 사용해서 가능!
- math같은 모듈을 가져와서 사용하게 되면 import문만 사용해서 math.sqrt처럼 사용하는게 더 좋음 왜? 모듈의 함수인것을 알 수 있으니까
#### 모듈을 가져오는 방법
- `import` 문 사용

    ```python
    import math
    
    print(math.sqrt(4))
    ```
- `from` 절 사용

    ```python
    from math import sqrt

    print(sqrt(4))
    ```


#### 모듈 사용하기
- `'.' (dot)` 연산자
  - "점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라“ 라는 의미

    ```python
    # 모듈명.변수명
    print(math.pi)

    # 모듈명.함수명
    print(math.sqrt(4))
    ```

#### 모듈 주의사항
- 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
- 마지막에 `import`된 이름으로 대체됨

    ```python
    from math import pi, sqrt
    from my_math import sqrt

    ```
    ```python
    # 그래서 모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음
    
    from math import *
    ```

## 파이썬 표준 라이브러리
### 파이썬 표준 라이브러리 `Python Standard Library`
- 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음
- 설치를 따로 안해도 되는 모듈과 패키지

> 참고 문서 : https://docs.python.org/ko/3/library/index.html

#### 패키지 `Package`
- 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것


# 제어문
### 제어문 `Control Statement`
- 코드의 실행 흐름을 제어하는 데 사용되는 구문<br>
- <span style='color:red;'>조건</span>에 따라 코드 블록을 실행하거나 <span style='color:red;'>반복</span>적으로 코드를 실행 

### 제어문 종류
- 조건문
    - `if`, `elif`, `else`
- 반복문
    - `for`, `while`
- 반복문 제어
    - `break`, `continue`, `pass`

### 조건문 `Conditional Statement`
- 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 <br>
코드 블록을 실행하거나 건너뜀

### 반복문 `Loop Statement`
- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
1. 특정 작업을 반복적으로 수행
2. 주어진 조건이 참인 동안 반복해서 실행

### 파이썬 반복문에 사용되는 키워드
- `for`
  - 특정 작업을 반복적으로 수행
- `while`
  - 주어진 조건이 참인 동안 반복해서 실행
  
### `‘for’` statement
- 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
- for statement의 기본 구조

    ```python
    for 변수 in 반복 가능한 객체:
        코드 블록
    ```

### ‘while’ statement
- 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행 == 조건식이 거짓(False)가 될 때 까지 반복
- while statement의 기본 구조

    ```python
    while 조건식:
        코드 블록
    ```
- 하지만 거의 for문 위주로 많이 사용하게 될 듯
- while문은 종료조건이 반드시 필요하다!


### 반복 제어
- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만<br>
때때로 일부만 실행하는 것이 필요할 때가 있음

#### 반복문 제어 키워드
- `break`
  - 반복을 즉시 중지
- `continue`
  - 다음 반복으로 건너뜀
- `pass`
  - 아무런 동작도 수행하지 않고 넘어감

#### continue 예시
- 리스트에서 홀수만 출력하기
- `현재 반복문의 남은 코드를 건너뛰고 다음 반복으로 넘어감`

    ```python
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for num in numbers:
        if num % 2 == 0:
            continue
        print(num)
    ```

### List Comprehension
- 간결하고 효율적인 리스트 생성 방법
- comprehension을 남용하지 말자
- 가독성이 떨어진다.

#### List Comprehension 활용 예시
- 2차원 배열 생성 시 (인접행렬 생성 시)
- _ 는 변수를 딱히 쓸 일이 없을 때, _로 표기를 한다.

```python
data1 = [[0] * (5) for _ in range(5)]

# 또는
data2 = [[0 for _ in range(5)] for _ in range(5)]

```


### 성능 비교

1. list comprehension
    - 대부분의 경우 가장 빠르고 파이썬스러운(Pythonic) 방법
2. map
    - 특정 상황(예: 기존 함수를 사용할 때)에서 리스트 컴프리헨션과 비슷하거나 약간 더 빠를 수 있음
3. loop
    - 일반적으로 가장 느리다고 알려져 있지만,
      python 버전이 올라가면서 다른 방식과 비슷하거나 때로는 더 나은 결과를 보이기도 함
    - 복잡한 로직이 필요한 경우에는 여전히 유용하게 사용될 수 있음

결론
- 성능 차이는 대부분의 경우 미미하므로, 
  코드의 가독성과 유지보수성을 고려하여 상황에 맞는 적절한 방법을 선택하는 것을 권장

### enumerate
### `enumerate(iterable, start=0) `
- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
- index값이 필요할 때 쓰면 좋아요

#### enumerate 예시

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
print(f'인덱스 {index}: {fruit}')

"""
인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
"""
```


# 오늘 풀었던 문제 (control.py)

```python
import requests
from pprint import pprint 

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def censorship(company, name):
    for i in range(len(black_list)):
        if company == black_list[i]:
            print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
            return False

    print('이상 없습니다.')
    return True

def create_user(user_list):
    censored_user_list = {}
    for i in range(len(user_list)):
        user_name = user_list[i]['name']
        user_company = user_list[i]['company']
        if censorship(user_company, user_name) == True:
            censored_user_list[user_company] = [f'{user_name}']
    return censored_user_list


dummy_data = []

for i in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    info = {}
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        info['company'] = parsed_data['company']['name']
        info['lat'] = parsed_data['address']['geo']['lat']
        info['lng'] = parsed_data['address']['geo']['lng']
        info['name'] = parsed_data['name']
        dummy_data.append(info)



print(create_user(dummy_data))

```

- 오늘의 문제는 api를 가져와 필터링을 거쳐서 내가 원하는 정보만 나오게 하는 것이 였다.
- 문제가 어려웠던 이유는 넘길 인자를 설정하는 부분에서 감을 잡는것
- 그리고 넘어갔을 때의 데이터를 내가 원하는 대로 필터링하는 것
- 마지막으로 user_list에 True인 값을 넣는 것이였다.
- 넘길 인자가 너무 더러운 느낌이 들어서 주변에 도움을 구해보니 변수로 만들어 넘기면 가독성을 높일 수 있다고 했다.(해결)
- 데이터가 넘어갔을 때 값이 원하는 대로 안나오는 문제를 직면했다.
- 이유는 for문안에서 True값이 들어가서 나오지 않는 것을 확인했다.
- 마지막으로 필터링된 데이터를 넣을 때 문제가 딕셔너리로 넣는데 value값을 리스트로 넣어야해서 그 부분은 f-string으로 풀어서 해결하였다.