from itertools import combinations

n = 67

nonzero = [i for i in range(1,n)]
squares = [(i*i)%n for i in range(1,int(n/2+1))]
squares.sort()
print("SQUARES: " + str(squares))


## check for every pair (0,x) how many vertices of the graph point to both 0 and x
dominators2 = []
for i in range(1,n):
    dominators2.append(0)
    for j in squares: ## as they point to 0 they must be in `squares`
        if j == i:
            continue
        elif (j-i)%n in squares:
            dominators2[i-1] += 1
    if dominators2[i-1] == 0:
        print("NOT 2")
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
    if dominators3[cnt] == 0:
        print("NOT 3")
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
        print("NOT 4")
    cnt += 1
print("4-DOMS: " + str(dominators4))

## the 5 check is commented out as it can take a very long time to run
'''
## the check for 5-sets (0,x,y,z)
dominators5 = []
cnt = 0
for i in combinations(nonzero,4):
    dominators5.append(0)
    for j in squares:
        if j == i[0] or j == i[1] or j == i[2] or j == i[3]:
            continue
        elif ((j-i[0])%n in squares) and ((j-i[1])%n in squares) and ((j-i[2])%n in squares) and ((j-i[3])%n in squares):
            dominators5[cnt] += 1
    if dominators5[cnt] == 0:
        print("NOT 5")
    cnt += 1
print("5-DOMS: " + str(dominators5))
'''





