def printMatrix(matrix):
        for row in matrix:
            print(row)
        print()

# TreeNode structure.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Greph Node structure
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# LinkedList Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# helper function to construct binary tree from a list by BFS.
def construct_bin_tree(lst):
        root = TreeNode(lst[0])

        frontier = [root]
        l_idx = 1

        while len(frontier):
            node = frontier.pop(0)

            if l_idx < len(lst) and lst[l_idx] != None:
                node.left = TreeNode(lst[l_idx])
                frontier.append(node.left)
            
            l_idx += 1

            if l_idx < len(lst) and lst[l_idx] != None:
                node.right = TreeNode(lst[l_idx])
                frontier.append(node.right)

            l_idx += 1
        
        return root

# helper function to convert an adjacency matrix to a Graph
def construct_graph(adj_mat):
    val2Node = {}

    idx = 0
    for adj_lst in adj_mat:
        nval = idx + 1

        newNode = None
        if nval in val2Node.keys():
            newNode = val2Node[nval]
        else:
            newNode = Node(nval)
            val2Node[nval] = newNode
        
        for adj_val in adj_lst:
            adjNode = None
            if adj_val in val2Node.keys():
                adjNode = val2Node[adj_val]
            else:
                adjNode = Node(adj_val)
                val2Node[adj_val] = adjNode
            
            newNode.neighbors.append(adjNode)
        
        idx += 1
        
    return val2Node[1]

def dfs_print(node):
    visited = set()

    def dfs(rootNode):
        if rootNode in visited:
            return 
        visited.add(rootNode)
        
        print(rootNode.val)
        for childNode in rootNode.neighbors:
            dfs(childNode)
    
    dfs(node)

def construct_LL_from_lst(lst):
    head = ListNode(lst[0])
    temp = head

    for n in lst[1:]:
        temp.next = ListNode(n)
        temp = temp.next
    
    return head

def print_LL(node):
    s = str(node.val)
    node = node.next
    
    while node != None:
        s += "-> " + str(node.val)
        node = node.next
    print(s)