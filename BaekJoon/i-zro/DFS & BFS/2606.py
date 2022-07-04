n = int(input())  # 전체 노드 수
m = int(input())  # 받을 엣지 수

network = list()
for _ in range(m):
  network.append(list(map(int, input().split())))

from collections import deque
def bfs(network, length):
  q = deque()
  visited = [False] * length
  answer = 0  # 정답
  q.appendleft(1) # 1번 노드 추가하고 시작
  
  while q:
    pop_item = q.pop()
    if not visited[pop_item]:
      visited[pop_item] = True
      for net in network:
        if net[0] == pop_item:
          q.appendleft(net[1])
          answer+=1

  return answer-1 # 1번 제외

print(bfs(network, n))
    