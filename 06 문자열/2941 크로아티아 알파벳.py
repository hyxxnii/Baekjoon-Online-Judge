# 다른 사람 풀이
# .replace 함수 사용

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for c in croatia:
    word = word.replace(c, '*')
    
print(len(word))