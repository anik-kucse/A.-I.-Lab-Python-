from itertools import permutations
from itertools import combinations 


def takeStatement():
    print('number of statement: ')
    n = input()
    listFact = []
    listLeftSide = []
    listRightSide = []
    for i in range(int(n)):
        statement = input()
        statement = statement.replace(' ','')
        
        if(len(statement) == 1):
            listFact.append(statement)
            
        elif('=>' in statement):
            ls, rs = statement.split('=>')
            listLeftSide.append(ls)
            listRightSide.append(rs)
            
    print('fact = ',listFact,' ls = ',listLeftSide, ' rs = ',listRightSide)
    return listFact, listLeftSide, listRightSide

def makePermutayion(listFact):
    listPermutaion = []
    for k in range(1,len(listFact)+1):
        perm = permutations(listFact, k) 
        for i in list(perm):
            arg = ''
            for j in i: 
                arg = arg + j
            listPermutaion.append(arg)
    return listPermutaion

def leftSideSearch(leftList, listPermutaion):
    for i in listPermutaion:
        for j in range(len(leftList)):
            if(i in leftList[j]):
                return j
    return -1

def leftSideSplit(listLeftSide): 
    leftList = []
    for i in range(len(listLeftSide)):
        if('.' in listLeftSide[i]):
            left = ''
            for j in listLeftSide[i].split('.'):
                left = left + j
            leftList.append(left)
        else:
            leftList.append(listLeftSide[i])
    return leftList


# listFact, listLeftSide, listRightSide = takeStatement()
listFact = ['a', 'b']
listLeftSide = ['p', 'a.b', 'a.p', 'b.l', 'l.m']
listRightSide = ['q', 'l', 'l', 'p', 'p']
goal = 'q' 
leftList = leftSideSplit(listLeftSide)
# print('left',leftList)
while(True):
    listPermutaion = makePermutayion(listFact)
    # print("perm",listPermutaion)
    j = leftSideSearch(leftList,listPermutaion)
    if(j<0):
        print('False')
        break
    newFact = listRightSide[j]
    
    print(leftList[j],' => ', listRightSide[j])
    if(goal == newFact):
        print("True")
        break
    else:
        listFact.append(newFact)
        del(leftList[j])
        del(listRightSide[j])

# 7
# a
# b
# p=>q
# a.b=>l
# a.p=>l
# b.l=>p
# l.m=>p