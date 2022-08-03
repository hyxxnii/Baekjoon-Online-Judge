# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
num_list = list(map(int, input().split()))

min_ = num_list[0]
max_ = num_list[0]

for num in num_list:
    if min_ > num:
        min_ = num
    if max_ < num:
        max_ = num

print(min_, max_)