file = open('text.txt', 'w')

class Tree:
    Left = None
    Right = None
    Data = None
    def __init__(self):
        self.Left = Tree
        self.Right = Tree
        self.Data = None

eTree = Tree()

def buildTree(n, tr):
        if tr.Data == None:
           tr.Data = n
           tr.Left = Tree()
           tr.Right = Tree()
        elif n <= tr.Data:
                buildTree(n, tr.Left)
        elif n > tr.Data:
                buildTree(n, tr.Right)

def height(tr):
    if tr.Data == None:
        return 0
    else:
        lheight = height(tr.Left)
        rheight = height(tr.Right)
        if lheight > rheight:
            return(lheight+1)
        else:
            return(rheight+1)

def printLevel(tr, level, i):
    if tr.Data == None:
        return
    if level == 1:
        file.write(" Уровень " + str(i) + ": " + str(tr.Data))
    elif level > 1:
          printLevel(tr.Left, level-1, i);
          printLevel(tr.Right, level-1, i);

def printAll(tr):
    h = height(tr)
    i=1
    while(i<=h):
        printLevel(tr, i, i)
        i +=1

stack = list()

def st(tr):
    stack.append(tr)
    while len(stack) > 0:
        cur = stack.pop() 
        if cur.Data != None:
            print(cur.Data)
        if cur.Right != None:
            stack.append(cur.Right)   
        if cur.Left != None:
            stack.append(cur.Left)

buildTree(5, eTree)
buildTree(10, eTree)
buildTree(15, eTree)
buildTree(20, eTree)
buildTree(3, eTree)
printAll(eTree)
st(eTree)
file.close()
