# https://www.acmicpc.net/problem/2798
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split(" ")))
card_list = list(map(int, input().split(" ")))

max_sum_card = -1

for num1 in card_list:
    for num2 in card_list.remove(num1):
        if num1 == num2:
            continue
        for num3 in card_list:
            if num2 != num3 and num1 != num3:
                sum_three_card = num1 + num2 + num3
                if sum_three_card <= M and max_sum_card <= sum_three_card:
                    max_sum_card = sum_three_card
            else:
                break
            
print(max_sum_card)