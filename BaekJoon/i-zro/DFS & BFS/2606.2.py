n = int(input())  # 전체 노드 수
m = int(input())  # 받을 엣지 수

network = list()
for _ in range(m):
  temp = list(map(int, input().split()))
  network.append(temp)
  network.append(temp[::-1])
  
# print(network)

from collections import deque
def bfs(network, length):
  q = deque()
  visited = [False] * length
  answer = 0  # 정답
  q.appendleft(1) # 1번 노드 추가하고 시작
  visited[0] = True  
  
  while q:
    pop_item = q.pop()

    for net in network:
      if net[0] == pop_item and not visited[net[1]-1]:
        q.appendleft(net[1])
        visited[net[1]-1] = True
        answer+=1

  return answer # 1번 제외

print(bfs(network, n))