import math
import random

class tree:
    def __init__(self,maximumValidation,val):
        self.maximumValidation = maximumValidation
        self.val = val
        self.listchild = []
    
    def childNode(self, child):
        self.listchild.append(child)

    def generateTree(self, parent, depth, branchFactor, lavel):
        if(depth <= 1):
            for i in range(branchFactor):
                if(lavel % 2 != 0):
                    leaf = tree(True, random.randint(-10,10))
                else:
                    leaf = tree(False, random.randint(-10,10))
                parent.childNode(leaf)
            return parent
        else:
            for i in range(branchFactor):
                if(lavel % 2 != 0):
                    leaf = tree(True, -math.inf)
                else:
                    leaf = tree(False, math.inf)
                parent.childNode(leaf)
                self.generateTree(leaf, depth-1, branchFactor, lavel+1)
            return parent
    
    def __repr__(self):
        return str(self.val) +' '+ str(self.maximumValidation) 

    def __str__(self, level=0):
        ret = " \t " * level + repr(self.val) + " \n "
        for child in self.listchild:
            ret += child.__str__(level+1)
        return ret

def AlphaBetaBpruning(parent, depth, a, b):
    flag = True
    if len(parent.listchild) == 0:
        return parent.val

    if(parent.maximumValidation == False):
        value = math.inf
        for i in parent.listchild :
            if flag:
                NewValue = AlphaBetaBpruning(i, depth+1, a, b)
                value = min( value, NewValue) 
                b = min( b, value)
                parent.val = value
                if b <= a:
                    print('depth',depth)
                    flag = False
            else:
                parent.listchild.remove(i)
        return value
        
    else:
        value = -math.inf
        for i in parent.listchild :
            if flag:
                NewValue = AlphaBetaBpruning(i, depth+1, a, b)
                value = max(value, NewValue) 
                a = max(a, value)
                parent.val = value
                if b <= a:
                    print('depth',depth)
                    flag = False
            else:
                parent.listchild.remove(i)
        return value
        
parentNode = tree(True, -math.inf)
parentNode.generateTree(parentNode, 3, 2, 0)
print(parentNode)
AlphaBetaBpruning(parentNode, 0, -math.inf, math.inf)
print(parentNode)