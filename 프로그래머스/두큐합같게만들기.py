from collections import deque


def solution(queue1, queue2):
    target = (sum(queue1)+sum(queue2))/2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    while sum(queue1) != target and sum(queue2) != target:
        if (sum(queue1) > target and sum(queue2) > target) or (sum(queue1) < target and sum(queue2) < target):
            return -1

        if sum(queue1) > target:
            v = queue1.popleft()
            while sum(queue1) > target:
                v = queue1.popleft()
                if v > target:
                    return -1
                queue2.append(v)
                cnt += 1

        if sum(queue2) > target:
            while sum(queue2) > target:
                v = queue2.popleft()
                if v > target:
                    return -1
                queue1.append(v)
                cnt += 1

    return cnt
