def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, target, 0)
    return answer

def dfs(numbers, target, depth):
    ans = 0
    if len(numbers) == depth:
        if sum(numbers) == target:
            return 1
        return 0
    else:
        ans += dfs(numbers, target, depth + 1)
        numbers[depth] *= -1    # 음수인 경우의 수 만들기
        ans += dfs(numbers, target, depth + 1)
        return ans