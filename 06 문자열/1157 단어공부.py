# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

word = input().lower()
word_set = list(set(word)) 
word_cnt = [0] * len(word_set)

for ws in word_set:
    for w in word:
        if ws == w:
            word_cnt[word_set.index(ws)] += 1

if word_cnt.count(max(word_cnt)) >= 2:
    print("?")
else:
    print(word_set[word_cnt.index(max(word_cnt))].upper())