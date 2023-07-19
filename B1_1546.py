sub_num = int(input())
sub_arr = list(map(int,input().split()))

M = max(sub_arr)
for i in range(0,len(sub_arr)):
    sub_arr[i] = sub_arr[i]/M*100

result = sum(sub_arr)/sub_num

print(result)