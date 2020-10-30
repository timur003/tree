import operator
class Tree:
    Left = None
    Right = None
    Data = None
    def __init__(self):
        self.Left = Tree
        self.Right = Tree
        self.Data = None
list1 = list()
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
        list1.append("Уровень " + str(i) + ": " + str(tr.Data))
        file.write("Уровень " + str(i) + ": " + str(tr.Data))
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

    while stack.count() > 0:
        cur = stack.pop() 
        stack.append(cur.left)
        stack.append(cur.right)   

    if tr.Data == None:
        return
    if level == 1:
        stack.append(tr.Data)
    elif level > 1:
          st(tr.Left, level-1, i);
          st(tr.Right, level-1, i);
def printst(st):




buildTree(5, eTree)
buildTree(10, eTree)
buildTree(15, eTree)
buildTree(20, eTree)
buildTree(3, eTree)
printAll(eTree)
st.append(eTree)
file.close()
