import sys
from pprint import pprint
row, col = map(int,input().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(row)]


exams_W = [['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W']]
exams_B = [['B','W','B','W','B','W','B','W'], ['W','B','W','B','W','B','W','B']]
cnts_B = []
cnts_W = []
for i in range(0,row-7):
    for j in range(0,col-7):
        temp = []
        cnt_B = 0
        cnt_W = 0
        for k in range(0,8):
            temp = arr[i+k][j:j+8]
            exam_W = exams_W[k % 2]
            exam_B = exams_B[k % 2]
            for q in range(0,8):
                if temp[q] != exam_W[q]:
                    cnt_W += 1
                if temp[q] != exam_B[q]:
                    cnt_B += 1

        cnts_B.append(cnt_B)
        cnts_W.append(cnt_W)

print(min(min(cnts_W),min(cnts_B)))




