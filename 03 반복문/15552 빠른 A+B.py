# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.
# input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

import sys
T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A + B)