n = int(input())
info = dict()
age_list = list()
min_value = 9999999
for i in range(n):
    lst = input().split(" ")[::-1]
    
    for j in range(1, 3):
        if len(lst[j]) == 1:
            lst[j] = "0" + lst[j]
    
    age = int("".join(lst[0:3]))
    name = lst[-1]
    info[age] = name
    age_list.append(age)

# 오름차순 정렬 => 나이순
age_list.sort()
print(info[age_list[-1]]) # 가장 적은 나이
print(info[age_list[0]]) # 가장 많은 나이