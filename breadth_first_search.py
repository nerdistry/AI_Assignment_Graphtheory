from collections import defaultdict
class BfsTraverser:
    def __init__(self):
        self.visited = []
        self.end_search = False

    def BFS(self, graph, start_node, goal_node):
        queue = [start_node]

        self.visited.append(start_node)

        while queue and not self.end_search:
            current  = queue.pop(0)

            for i in list(graph[current]):
                if i not in self.visited:
                    print("Command; Drive to ", i , "Junction",end = "\n")
                    if i is goal_node:
                        print("We have reached ",i," the final destination")
                        self.visited.append(i)
                        self.end_search = True
                        break
                    else:
                        print("Here ",self.end_search)
                        queue.append(i)
                        self.visited.append(i)
