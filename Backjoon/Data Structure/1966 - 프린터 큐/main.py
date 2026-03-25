import collections

getTestCase = int(input())

for _ in range(getTestCase):
    count = 0
    n, m = map(int, input().split(" "))
    deque = collections.deque(list(map(int, input().split(" "))))

    while m != -1:
        if deque[0] == max(deque):
            deque.popleft()
            m -= 1
            count += 1
        else:
            deque.append(deque.popleft())
            if m == 0:
                m = len(deque) - 1
            else:
                m -= 1
    print(count)
