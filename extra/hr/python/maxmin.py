N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()
min = 10000000000
for x in range(0,N-K+1):
    if min > abs(lists[x]-lists[x+K-1]):
        min = abs(lists[x]-lists[x+K-1])
print "min = ",
print min