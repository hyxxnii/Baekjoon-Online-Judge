# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

# ---
# 한 자리 수, 두 자리 수 : 한수
# 세자리 수: str(i)의 앞에서 두 자리씩 int(자리수) 뺀 값이 동일하면 한수

num = int(input())

if num < 100: # 두 자리 수 이하
    print(num)

else: # 세 자리 수
    result = 99
    for n in range(100, num + 1):
        str_num = str(n)
        if int(str_num[0])-int(str_num[1]) == int(str_num[1]) - int(str_num[2]):
            result += 1
    print(result)
        

