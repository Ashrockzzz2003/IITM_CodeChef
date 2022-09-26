T = int(input())

for _ in range(T):
    N = int(input())
    contest_codes = list(map(str, input().split(' ')))
    d = {'START38': 0, 'LTIME108': 0}
    for i in contest_codes:
        d[i] += 1
    print(d['START38'], d['LTIME108'])
