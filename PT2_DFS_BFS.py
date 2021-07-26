# Chp05 : DFS/BFS --> 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

# < 스택 > --> 선입후출 or 후입선출 : 박스쌓기에 비유가능 --> 아래에서 위로 쌓아올리고(입력) 치울때는 위에서 아래로 치움(출력)

# 스택 예제
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# < 큐 > --> 선입선출 : 줄설때 줄먼저 선 사람이 먼저 드감

# 큐 예제

from collections import deque

# 큐(queue) 구현하기 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 재귀 함수 예제
def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()
recursive_function()
#결과 에러걸림


# 재귀 함수의 종료 예제

def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다')

# 탐색 알고리즘 DFS/BFS (pg134)

# 인접 행렬 방식 예제
INF = 999999999

graph = [[0,7,5],
         [7,0,INF],
         [5,INF, 0]]

print(graph)

# 인접 리스트 방식 예제
# 행(Row)이 3개인 2차원 리스트로 인접 시르스 표현
graph = [[]for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)

