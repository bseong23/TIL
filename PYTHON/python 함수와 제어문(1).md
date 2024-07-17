## 함수 `Functions`
### 개요
- 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음


#### 함수를 사용하는 이유 
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
- <span style='color:red;'>재사용성</span>이 높아지고, 코드의 <span style='color:red;'>가독성과 유지보수성</span> 향상

    ```python
    # 두 수의 합을 구하는 코드
    num1 = 5
    num2 = 3

    sum_result = num1 + num2
    print(sum_result)
    ```
    
    ```python
    # 두 수의 합을 구하는 함수
    def get_sum(num1, num2):
        return num1 + num2

    # 함수 사용하여 결과 출력
    num1 = 5
    num2 = 3
    sum_result = get_sum(num1, num2)
    print(sum_result)
    ```

### 다양한 인자 종류
1. 위치 인자
2. 기본 인자 값
3. 키워드 인자
4. 임의의 인자 목록
5. 임의의 키워드 인자 목록

#### Positional Arguments (위치인자)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
- <span style='color:crimson;'>위치인자는 함수 호출 시 반드시 값을 전달해야 함</span>

    ```python
    def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살이시군요.')


    greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요
    ```
#### Default Argument Values (기본 인자 값)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

    ```python
    def greet(name, age=30):
        print(f'안녕하세요, {name}님! {age}살이시군요.')


    greet('Bob') # 안녕하세요, Bob님! 30살이시군요.
    greet('Charlie', 40) # 안녕하세요, Charlie님! 40살이시군요.
    ```
####  Keyword Arguments (키워드 인자)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
- <span style='color:crimson;'>단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함</span>

    ```python
    def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살이시군요.')


    greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
    greet(age=35, 'Dave')  #  positional argument follows keyword argument
    ```

#### Arbitrary Argument Lists (임의의 인자 목록)
- c언어 argc, argv랑 같은 뜻인거 같음
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 <span style='color:red;'>`‘*’`</span>를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
- 위치인자와 같이 사용하려면 앞에 사용해야한다. def calculate_sum(params, *args)이렇게

    ```python
    def calculate_sum(*args):
        print(args)
        total = sum(args)
        print(f'합계: {total}')


    """
    (1, 2, 3)
    합계: 6
    """
    calculate_sum(1, 2, 3)
    ```

#### Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 <span style='color:red;'>`‘**’`</span>를 붙여 사용하며, <br>여러 개의 인자를 dictionary로 묶어 처리

    ```python
    def print_info(**kwargs):
        print(kwargs)


    print_info(name='Eve', age=30) # {'name': 'Eve', 'age': 30}
    ```

## 함수와 Scope
### Python의 범위(Scope)
- 함수는 코드 내부에 `local scope`를 생성하며, 그 외의 공간인 `global scope`로 구분

### 범위와 변수 관계
- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
- variable 
    - global variable : global scope에 정의된 변수
    - local variable : local scope에 정의된 변수

#### 변수 수명주기(lifecycle)
- 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨
1. built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
2. global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

#### 이름 검색 규칙(Name Resolution)
- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
    1. Local scope : 지역 범위(현재 작업 중인 범위)
    2. Enclosed scope : 지역 범위 한 단계 위 범위
    3. Global scope : 최상단에 위치한 범위
    4. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
- <span style='color:crimson;'>함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음</span>

![image](https://github.com/ragu6963/TIL/assets/32388270/15b4f0c6-7f21-4986-8349-fd8740e49573)

#### `global` 키워드
- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

    ```python
    num = 0 # 전역 변수


    def increment():
        global num # num를 전역 변수로 선언
        num += 1


    print(num) # 0
    increment()
    print(num) # 1
    ```

### Packing `패킹`
- 여러 개의 값을 하나의 변수에 묶어서 담는 것

### `‘*’`을 활용한 패킹
- `*b`는 남은 요소들을 리스트로 패킹하여 할당

    ```python
    numbers = [1, 2, 3, 4, 5]
    a, *b, c = numbers
    
    print(a) # 1
    print(b) # [2, 3, 4]
    print(c) # 5
    ```
- print 함수에 임의의 가변 인자를 작성할 수 있었던 이유

    ```python
    print('hello') # hello
    print('you', 'need', 'python') # you need python
    ```

    ![image](https://github.com/ragu6963/TIL/assets/32388270/05db04bd-d01c-4f4c-a193-854e59385d67)

### Unpacking `언패킹`
- 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것

#### 언패킹 예시
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
    
    ```python
    packed_values = 1, 2, 3, 4, 5
    a, b, c, d, e = packed_values
    print(a, b, c, d, e)  # 1 2 3 4 5

#### `‘*’`을 활용한 언패킹
- `*` 는 리스트의 요소를 언패킹하여 인자로 전달

    ```python
    def my_function(x, y, z):
        print(x, y, z)
    
    names = ['alice', 'jane', 'peter']
    my_function(*names) # alice jane peter
    ```
    ```

#### `‘**’`을 활용한 언패킹
- `**` 는 딕셔너리의 키-값 쌍을 함수의 키워드 인자로 언패킹
- 대신 매개변수와 딕셔너리 키 값의 이름이 같아야한다.
    
    ```python
    def my_function(x, y, z):
        print(x, y, z)


    my_dict = {'x': 1, 'y': 2, 'z': 3}
    my_function(**my_dict)  # 1 2 3
    ```

#### `*`, `**` 패킹 / 언패킹 연산자 정리
- `‘*’`
    - 패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 튜플로 묶음
    - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달
    
- `‘**’`
    - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달


#  오늘 가장 막혔던 문제

- 오늘 배웠던 개념들을 토대로 약 10문제 정도를 풀었다. 그 중 가장 이상하고 어려웠던 문제이다.
- python파일로도 TIL에 올렸지만 어떻게 내가 풀었는지에 대한 생각을 정리하고자 한다.


```python
number_of_people = 0
number_of_book = 100

def rental_book(info):
    name_1 = info['name']
    number = info['age'] // 10
    decrease_book(number)
    print(f'{name_1}님이 {number}권의 책을 대여하였습니다.')

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'현재 남은 책의 수 : {number_of_book}')

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    user_info = {
        'name': name,
        'age': age,
        'address': address,
    }
    print(f'{name}님 환영합니다!')
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user, name, age, address))

info = list(map(lambda x: {'name': x['name'], 'age': x['age']}, many_user))

list(map(rental_book, info))
```
- 먼저 요구사항이 
<br>
실습 4에서 작성한 코드를 활용하여 many_user 변수에 모든 신규 고객 정보 딕셔너리를 요소로 갖는 리스트를 할당한다.
<br>
실습 3에서 작성한 코드를 활용하여 decrease_book 함수를 작성한다.
<br>
rental_book 함수는 info 인자 하나만 할당 받을 수 있다.
<br>
info 인자는 신규 고객의 이름과 나이를 담은 딕셔너리이다.
신규 고객의 나이를 10으로 나눈 몫을 대여할 책의 수로 활용한다. (decrease_book 함수의 인자)
<br>
info 인자에 사용될 딕셔너리는 many_user와 map을 사용해 새로운 딕셔너리를 생성한다.
<br>
이 때, map에 사용될 함수는 lambda로 구현한다.
 그 결과를 rental_book 함수에 각각 전달하여 호출한다. 이 때 역시 map 함수를 사용한다.

이러한 요구사항을 충족해야만 했다. 처음엔 문제를 이해하는데 시간을 많이 사용했었다. <br>
그래서 내가 할 수 있는 것들을 하나씩 해보기로 생각했고 먼저 신규 고객 나이를 10으로 나눈 몫을 대여할 책의 수를 건들여 보기로 생각했다. <br>
그 작업은 `rental_book` func에서 이루어 졌고 many_user의 인덱스 값을 사용해 확인 해보니 원하는 값을 도출해 낼 수 있었다. 그 다음으로 생각 한 것은 변수 info를 만들어 내는 것 이였다. <br>
요구사항을 살펴보면 신규고객의 이름과 나이를 담은 딕셔너리이고,<br>
many_user와 map을 사용해 새로운 딕셔너리를 생성하라고 했다. 그리고 lambda로 구현을 하라고 해서 머리가 아파오기 시작했다.<br>
그래서 먼저 lambda(익명 함수)로 구현하기 보단 함수를 하나 만들어서 구현해보자고 생각을 했고, many_user에서 이름과 나이만 뽑아오게 되면 만들 수 있겠다는 생각이 들었다. <br>
딕셔너리에 밸류값으로 many_user의 값들을 사용했고 내가 원하는 답을 얻어낼 수 있었다. 그래서 이것을 토대로 lambda를 만들어서 사용했다. <br>
마지막으로 이제 만든 info를 rental_book에다가 담는 것인데 이는 map을 사용하게 된다면 쉽게 넣을 수 있었다. 하지만 여기서 한가지 변수가 발생했는데 print가 되지 않았다.<br>
그래서 고민을 하다가 list를 사용해서 만들어보니 print가 작동을 하는 것을 볼 수 있었다. 이에 왜 list를 사용하지 않으면 안될까? 라는 생각이 들어서 강사님께 여쭤보니 다음 주에 배울 수 있는 부분이라고 하셨고, <br>
위에서 list로 값들을 뽑아서 사용했으니 아래도 똑같이 사용한다! 라고 일단은 쉽게 생각하라고 말씀해주셨다.<br>
for문을 사용한다면 조금 더 쉽게 만들 수 있었을 것 같지만 아직 for문을 배우지 않았으니, 또 요구사항을 충족하고자 노력하였다. 
