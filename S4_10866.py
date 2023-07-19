from collections import deque
import sys

q = deque()

N = int(input())



for i in range(N):
   inst = sys.stdin.readline().split()


   if inst[0] == 'push_back':
      q.append(int(inst[1]))

   elif inst[0] == 'push_front':
      q.appendleft(int(inst[1]))

   elif inst[0] == 'pop_front':
      if len(q) == 0:
         print(-1)
      else:
         print(q.popleft())

   elif inst[0] == 'pop_back':
      if len(q) == 0:
         print(-1)
      else:
         print(q.pop())

   elif inst[0] == 'size':
      print(len(q))

   elif inst[0] == 'empty':
      if len(q) == 0:
         print(1)
      else:
         print(0)

   elif inst[0] == 'front':
      if len(q) == 0:
         print(-1)

      else:
         temp = q.popleft()
         print(temp)
         q.appendleft(temp)

   elif inst[0] == 'back':
      if len(q) == 0:
         print(-1)
      else:
         temp = q.pop()
         print(temp)
         q.append(temp)
