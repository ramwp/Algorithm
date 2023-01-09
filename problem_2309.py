# https://www.acmicpc.net/problem/2309
height_list = [int(input()) for _ in range(9)]

sum_height = sum(height_list)
is_find = False

for num1 in height_list:
    for num2 in height_list:
        if num1 != num2:
            if sum_height - (num1 + num2) == 100:
                is_find = True
                height_list.remove(num1)
                height_list.remove(num2)
                height_list.sort()
                for height in height_list:
                    print(height)
                break
    if is_find:
        break