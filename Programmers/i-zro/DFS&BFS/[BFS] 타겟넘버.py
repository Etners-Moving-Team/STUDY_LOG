def solution(numbers, target):
    answer = 0
    answer = bfs(numbers, target)
    return answer

from collections import deque
def bfs(numbers, target):
    ans = 0
    current_q = deque()
    current_q.extendleft([numbers[0], -numbers[0]])
    next_q = deque()
    for t in numbers[1:]:    
        for num in current_q:
            next_q.appendleft(num + t)
            next_q.appendleft(num - t)
        current_q = deque()
        current_q.extendleft(next_q)
        next_q = deque()
    for c in current_q:
        if c == target:
            ans += 1
            
    return ans