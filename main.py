class Node(object):
    def __init__(self):
        self.child1 = None
        self.child2 = None
        self.data = None
        self.tag = None
        self.skA = 0
        self.skC = 0
        self.skG = 0
        self.skT = 0
        self.isRipe = False

    def addchild(self, child):
        if self.child1 == None:
            self.child1 = child
        elif self.child2 == None:
            self.child2 = child
        else:
            print("Trying to add too many nodes")
        return

    def addData(self, data):
        self.data = data
        return

    def getData(self):
        return self.data

    def toString(self):
        print("###")
        if self.data != None:
            print(self.data)
        else:
            print("No data in this node")


# Run the input
def main(inputString):
    lines = inputString.splitlines()
    nodeTuples = []
    numLeaves = 0
    for i in range(len(lines)):
        if i == 0:
            numLeaves = int(lines[i])
            continue
        nodeTuples.append(lines[i].split("->"))

    nodeArray = []
    # This adds leaves to the nodeArray
    i = 1
    for element in nodeTuples:
        currNode = Node()
        if i <= numLeaves:
            currNode.addData(element[1])
            nodeArray.append(currNode)
            i = i + 1
        else:
            break

    # This prints the nodeArray that should only have leaves
    # for i in range(len(nodeArray)):
    #   nodeArray[i].toString()

    # This adds parents to all of the leaves
    i = 0
    for element in nodeTuples:
        if i < numLeaves:
            if len(nodeArray) <= int(element[0]):
                currNode = Node()
                currNode.addchild(nodeArray[i])
                # nodeArray[i].toString()
                nodeArray.append(currNode)
            else:
                currNode = nodeArray[int(element[0])]
                currNode.addchild(nodeArray[i])
                # nodeArray[i].toString()
            i = i + 1
        else:
            break

    # adds parents to non-leaf nodes
    startLoop = i
    for i in range(startLoop, len(nodeTuples)):
        if len(nodeArray) <= int(element[0]):
            currNode = Node()
            currNode.addchild(nodeArray[int(element[1])])
            nodeArray.append(currNode)
        else:
            currNode = nodeArray[int(element[0])]
            currNode.addchild(nodeArray[int(element[1])])

        # Tree should be built at this point
    for k in range(len(nodeArray[0].getData())):
        for v in nodeArray:
            v.tag = 0
            if v.data != None:
                v.tag = 1
                if 'A' == v.data[k]:
                    v.skA = 0
                else:
                    v.skA = float("inf")
                if 'C' == v.data[k]:
                    v.skC = 0
                else:
                    v.skC = float("inf")
                if 'G' == v.data[k]:
                    v.skG = 0
                else:
                    v.skG = float("inf")
                if 'T' == v.data[k]:
                    v.skT = 0
                else:
                    v.skT = float("inf")
        # ripen nodes
        for node in nodeArray:
            if (node.child1 != None) and (node.child2 != None) and (node.tag == 0):
                if (node.child1.tag == 1) and (node.child2.tag == 1) and (node.tag == 0):
                    node.isRipe = True
        # loop through ripe nodes
        while (findRipeNode(nodeArray) != False):
            currNode = findRipeNode(nodeArray)
            currNode.tag = 1
            currNode.isRipe = False

            # ripen nodes again at the end of each loop
            for node in nodeArray:
                if (node.child1 != None) and (node.child2 != None) and (node.tag == 0):
                    if (node.child1.tag == 1) and (node.child2.tag == 1) and (node.tag == 0):
                        node.isRipe = True


def findRipeNode(nodeArray):
    for node in nodeArray:
        if node.isRipe == True:
            return node
    return False


# def getMinimum(parent, child):


# implement this stuff


main('''4
4->CAAATCCC
4->ATTGCGAC
5->CTGCGCTG
5->ATGGACGA
6->4
6->5''')