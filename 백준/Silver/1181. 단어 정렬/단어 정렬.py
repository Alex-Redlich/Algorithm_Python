import sys
input = sys.stdin.readline

n = int(input())
word = []
for i in range(n):
    a = input().strip()
    if a not in word:
        word.append(a)
word.sort()
word.sort(key=lambda x:len(x))

for i in range(len(word)):
    print(word[i])