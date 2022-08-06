# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

n = int(input())
cnt = 0

for _  in range(n):
    w_list = set()
    flag = 0

    word = input()
    for i in range(len(word)):
        if word[i] not in w_list:
            w_list.add(word[i])
        else:
            if word[i-1] != word[i]:
                flag = 1

    if flag == 0 or len(word) == 1:
        cnt += 1

print(cnt)