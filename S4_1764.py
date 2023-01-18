N,M = map(int,input().split())
See = set()
Listen = set()

for i in range(N):
    See.add(input())

for i in range(M):
    Listen.add(input())

answer = list(See & Listen)
answer.sort()

print(len(answer))
for i in answer:
    print(i)