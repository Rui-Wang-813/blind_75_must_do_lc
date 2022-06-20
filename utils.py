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