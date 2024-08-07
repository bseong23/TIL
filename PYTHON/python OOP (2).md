### 상속

상속 Inheritance
- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것을 말한다.

상속이 필요한 이유
1. 코드의 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음.
    - 부모 클래스와 자식 클래스 간에 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음
2. 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음
3. 유지 보수의 용이성
    - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지보수가 용이하다
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화 할 수 있음

### MRO (Method Resolution Order)
- 메서드의 결정 순서

### super()
- 부모 클래스 객체륿 반환하는 내장 함수
- 다중 상속 시 MRO를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출

### MRO가 필요한 이유
- 부모 클래스들이 여러 번 액세스 되지 않도록, 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고, 각 부모르 오직 한 번만 호출하고, 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성
- 프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있도록 도운다
- 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성이 향상된다.


### 에러와 디버깅
#### 디버깅
버그
- 소프트웨어에서 발생하는 오류 또는 결함
- 프로그램의 예상된 동작과 실제 동작 사이의 불일치

버그의 기원
- 'bug'라는 용어는 소프트웨어 이전부터 공학 분야에서 사용되었다.
- 컴퓨터 분야에서의 첫 사용은 1947년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼와 그녀의 팀이 컴퓨터의 릴레이에서 실제 나방을 발견한 것이 시초로 알려짐
- 하버드 Mark Ⅱ 컴퓨터 회로에 실제 나방이 들어가 합선을 일으켜 비정상적으로 동작한 것을 기록한 것
- 발견된 나방은 컴퓨터 로그북에 테이프로 붙여서 보존되었고 "First actual case of bug being found" (실제 버그가 발견된 첫 사례)라는 메모가 남겨짐
- "버그"라는 용어는 이전부터 사용되어 왔지만 이 사건을 계기로 컴퓨터 시스템에서 발생하는 오류 또는 결함을 지칭하는 용어로 널리 사용되기 시작

### Debugging
- 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
- 프로그램의 오작동 원인을 식별하여 수정하는 작업

디버깅 방법
1. print 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
3. [Python tutor](https://pythontutor.com/) 활용 (단순 파이썬 코드인 경우) 
4. 뇌 컴파일, 눈 디버깅 등

## 에러
### 에러 `Error`
- 프로그램 실행 중에 발생하는 예외 상황

#### 파이썬의 에러 유형
- 문법 에러 `Syntax Error`
    - 프로그램의 구문이 올바르지 않은 경우 발생 <br>(오타, 괄호 및 콜론 누락 등의 문법적 오류)
- 예외 `Exception`
    - 프로그램 실행 중에 감지되는 에러


## 예외
### 예외 `Exception`
- 프로그램 실행 중에 감지되는 에러

#### 내장 예외 `Built-in Exceptions`
- 예외 상황을 나타내는 예외 클래스들
- 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용
> 참고 문서 : https://docs.python.org/ko/3/library/exceptions.html#ValueError

## 예외 처리
- 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법

### 예외 처리 사용 구문
- `try`
  - 예외가 발생할 수 있는 코드 작성
- `except`
  - 예외가 발생했을 때 실행할 코드 작성
- `else`
  - 예외가 발생하지 않았을 때 실행할 코드 작성
- `finally`
  - 예외 발생 여부와 상관없이 항상 실행할 코드 작성

  ```python
  try:
      x = int(input('숫자를 입력하세요: '))
      y = 10 / x
  except ZeroDivisionError:
      print('0으로 나눌 수 없습니다.')
  except ValueError:
      print('유효한 숫자가 아닙니다.')
  else:
      print(f'결과: {y}')
  finally:
      print('프로그램이 종료되었습니다.')
  ```

### try & except
- try 블록 안에는 예외가 발생할 수 있는 코드를 작성
- except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
- 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동

    ```py
    try:
        # 예외가 발생할 수 있는 코드

    except 예외:
        # 예외 처리 코드
    ```

### 마무리
처음엔, javascript를 메인으로 공부하다가 python을 공부하게 되니 다른 부분이 많아서 힘들었다.
하지만 오늘의 수업을 끝으로 python수업을 다 들었는데 문법이 다른것이지 기본적인 틀은 같다는 확신을 가지게 되었다.
물론 완벽하게 안다, 완벽하게 배웠다 라고 할 수는 없겠지만 앞서 해왔던 공부들이 의미없는 행동이 아니였다는 것을 깨달을 수 있어서 좋은 시간이였다. 결국 객체지향 프로그래밍 언어라는 것들의 특징은 거의 비슷하고 배우는 사람들은 그 큰 틀을 이해하고 메인 언어를 잘 공부해 뒀다면 다른 언어를 배우는 것은 어렵지 않은 선택이 될 것 같다.
나도 프론트엔드가 꿈이라고 파이썬을 소홀히 하지 않고 모든 것이 연장되는 일이라고 생각하고 더욱 열심히 할 필요가 있다고 느꼈다.
<br>오늘의 문제들은 그렇게 어려운 것은 없었다. 익숙치 않아서 self와 super()를 쓰는 것이 조금 헷갈렸지만 수업에 나온 내용들을 다시 한 번 생각하고 복습을 하면서 문제들을 풀어나갈 수 있었다.