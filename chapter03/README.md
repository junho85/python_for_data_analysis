# chapter 03 IPython 소개
* IPython 기본 사용법 안내

### 3.1.7 매직 명령어
```
%quickref - IPython의 빠른 도움말 표시
%magic - 모든 매직 함수에 대한 상세 도움말 출력
%debug - 최근 예외 트레이스백의 하단에서 대화형 디버거로 진입
%hist - 명령어 입력(그리고 선택적으로 출력) 히스토리 출력
%pdb - 예외가 발생하면 자동적으로 디버거로 진입
%paste - 클립보드에서 들여쓰기가 된 채로 파이썬 코드 가져오기
%cpaste - 실행 파이썬 코드를 수동으로 붙여넣을 수 있는 프롬프트 표시
%reset - 대화형 네임스페이스에서 정의된 모든 변수와 이름을 삭제
%page OBJECT - 객체를 pager를 통해 보기 좋게 출력
%run script.py - IPython 내에서 파이썬 스크립트 실행
%prun statement - cProfile을 통해 statement를 실행하고 프로파일링 결과를 출력
%time statement - 단일 statement 실행 시간을 출력
%timeit statement - statement를 여러 차례 실행한 후 평균 실행 시간을 출력. 매우 짧은 시간 안에 끝나는 코드의 시간을 측정할 때 유용
%who, %who_ls, %whos - 대화형 네임스페이스 내에서 정의된 변수를 다양한 방법으로 표시
%xdel variable - variable을 삭제하고 IPython 내부적으로 해당 객체에 대한 모든 참조를 제거
```

### 3.1.8 Qt 기반의 GUI 콘솔

```
ipython qtconsole --pylab=inline
```

### 3.1.9 Pylab 모드와 Matplolib 통합
```
ipython --pylab
```

## 3.2 명령어 히스토리 사용하기

### 3.2.1 명령어 검색과 재사용

### 3.2.2 입.출력 변수

### 3.2.3 입.출력 기록하기

## 3.3 운영체제와 함께 사용하기

### 3.3.1 셸 명령어와 별칭

## 3.4 소프트웨어 개발 도구

### 3.4.1 인터랙티브 디버거

```
%run -d ch03/ipython_bug.py
%run -d -b2 ch03/ipython_bug.py
```
-b 행 번호 브레이크포인트를 미리 설정 해 줌


### 3.4.2 코드 시간 측정 %time 과 %timeit
```
import time
start = time.time()
for i in range(iterations):
    # some code to run here
elapsed_per = (time.time() - start) / iterations
```

```
# a very large list of strings
strings = ['foo', 'foobar', 'baz', 'qux', 'python', 'Guido Van Rossum', 'scari'] * 100000

method1 = [x for x in strings if x.startswith('foo')]
method2 = [x for x in strings if x[:3] == 'foo']
```

```
%time method1 = [x for x in strings if x.startswith('foo')]
%time method2 = [x for x in strings if x[:3] == 'foo']
```

```
%timeit method1 = [x for x in strings if x.startswith('foo')]
%timeit method2 = [x for x in strings if x[:3] == 'foo']
```

```
x = 'foobar'
y = 'foo'
%timeit x.startswith(y)
%timeit x[:3] == y
```

### 3.4.3 기본적인 프로파일링: %prun 과 %run -p
```
python3 -m cProfile cprof_example.py
```

* 시간 출력
```
python3 -m cProfile -s cumulative cprof_example.py
```

* ipython 에서
```
%prun -l 7 -s cumulative run_experiment()
```

### 3.4.4 함수의 각 줄마다 프로파일링하기
```
c.TerminalIPytonApp.extensions = ['line_profiler']
```

## 3.5 IPython HTML 노트북
JSON 파일 형식 .ipynb
ipython notebook --pylab=inline

## 3.6 IPython을 사용한 제품 개발을 위한 팁
### 3.6.1 모듈 의존성 리로딩하기

```
import some_lib
reload(some_lib)

x = 5
y = [1,2,3,4]
result = some_lib.get_answer(x, y)
```
dreload(some_lib)
some_lib 와 some_lib 에 의존하는 다른 모든 모듈을 새로 읽어온다


### 3.6.2 코드 설계 팁

중첩을 피하자

긴 파일에 대한 두려움을 버리자

## 3.7 IPython 고급 기능
### 3.7.1 IPython 친화적인 클래스 만들기

```
class Message:
    def __init__(self, msg):
        self.msg = msg

x = Message('I have a secret')
x
```

```
class Message:
    def __init__(self, msg):
        self.msg = msg
    def __repr__(self):
        return 'Message: %s' % self.msg

x = Message('I have a secret')
x
```

### 3.7.2 프로파일과 설정
```
~/.config/ipython/ipython_config.py
```

```
ipython profile create secret_project
```
