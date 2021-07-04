import sys

N = int(sys.stdin.readline()) 
my_dict = {} 

for i in range(N): 
    num = int(sys.stdin.readline()) 

    if num not in my_dict.keys(): 
        my_dict[num] = 1 
    else: 
        my_dict[num] = my_dict[num] + 1 

max_num = max(list(my_dict.values())) 
answer = [] 

for key, value in my_dict.items(): 
    if value == max_num:
        answer.append(key) 

print(min(answer))
