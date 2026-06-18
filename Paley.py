from itertools import combinations

n = 67

nonzero = [i for i in range(1,n)]
squares = [(i*i)%n for i in range(1,int(n/2+1))]
squares.sort()
print("SQUARES: " + str(squares))
nonsqua = [i for i in range(1,n) if i not in squares]
paley = [(a,b) for a in range(0,n) for b in range(0,n) if (b-a)%n in squares]


## check for every pair (0,x) how many vertices of the graph point to both 0 and x
dominators2 = []
for i in range(1,n):
    dominators2.append(0)
    for j in squares: ## as they point to 0 they must be in `squares`
        if j == i:
            continue
        elif (j-i)%n in squares:
            dominators2[i-1] += 1
print("2-DOMS: " + str(dominators2))

## the same check for triples (0,x,y)
dominators3 = []
cnt = 0
for i in combinations(nonzero,2):
    dominators3.append(0)
    for j in squares:
        if j == i[0] or j == i[1]:
            continue
        elif ((j-i[0])%n in squares) and ((j-i[1])%n in squares):
            dominators3[cnt] += 1
    cnt += 1
print("3-DOMS: " + str(dominators3))

## the check for 4-sets (0,x,y,z)
dominators4 = []
cnt = 0
for i in combinations(nonzero,3):
    dominators4.append(0)
    for j in squares:
        if j == i[0] or j == i[1] or j == i[2]:
            continue
        elif ((j-i[0])%n in squares) and ((j-i[1])%n in squares) and ((j-i[2])%n in squares):
            dominators4[cnt] += 1
    if dominators4[cnt] == 0:
        print("BAD")
        exit()
    cnt += 1
print("4-DOMS: " + str(dominators4))

## this doesn't print "BAD", so every 4-set (0,x,y,z) has atleast one vertex pointing
## at all four, hence the n=67 Paley digraph is a 4-paradox tournament.





