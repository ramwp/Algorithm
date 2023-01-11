

# 1 - 1 - 1 - 1  = 4  count += 1
        # - 2    =  4 count += 1
        # - 3
    # 
    # - 2


T = int(input())

find_n_count = 0

def add(start, dst):
    global find_n_count
    if start > dst:
        return
    elif start == dst:
        find_n_count += 1
        return
    else:
        for add_num in range(1, 4):
            add(start + add_num, dst)

for i in range(T):
    n = int(input())
    add(0, n)
    print(find_n_count)
    find_n_count = 0