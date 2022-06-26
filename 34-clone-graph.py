# solution by Rui Wang
# problem description link: https://leetcode.com/problems/clone-graph/

from utils import Node, construct_graph, dfs_print

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new_graph = Node(node.val)
        
        frontier = [node]
        visited = set([node])
        
        # new_frontier is the similar thing to frontier, storing copied nodes corresponding to 
        # original nodes in graph.
        new_frontier = [new_graph]
        # this is a dictionary that stores the nodes in new graph corresponding to values.
        val2Node = {new_graph.val: new_graph}
        
        while len(frontier):
            curNode = frontier.pop(0)
            
            newNode = new_frontier.pop(0)
            
            for neighbor in curNode.neighbors:
                
                # no matter visited or not, we need to add the new neighbor into the neighbors list
                # of new node.
                if neighbor not in visited:
                    visited.add(neighbor)

                    frontier.append(neighbor)
                    
                    newNeighbor = Node(neighbor.val)
                    newNode.neighbors.append(newNeighbor)
                    new_frontier.append(newNeighbor)

                    val2Node[neighbor.val] = newNeighbor
                else:
                    newNeighbor = val2Node[neighbor.val]
                    newNode.neighbors.append(newNeighbor)
        
        return new_graph

lst = [[2,4],[1,3],[2,4],[1,3]]
graph = construct_graph(lst)

sol = Solution()
dfs_print(sol.cloneGraph(graph))