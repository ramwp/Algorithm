# 지구 E : 1 ~ 15
# 태양 S : 1 ~ 28
# 달   M : 1 ~ 19


E, S, M = list(map(int, input().split(" ")))

count1 = 1
count2 = 1
count3 = 1

year = 1

while True:
    if count1 == E and count2 == S and count3 == M:
        break 
    
    if count1 < 15:
        count1 += 1
    else:
        count1 = 1
        
    if count2 < 28:
        count2 += 1
    else:
        count2 = 1
    
    if count3 < 19:
        count3 += 1
    else:
        count3 = 1
        
    year += 1

print(year)

