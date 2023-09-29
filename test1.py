from collections import defaultdict
class BfsTraverser:
  # Constructor
  def __init__(self):
    self.visited = []#this is an empty list, it is used to store nodes that have been visited
    self.end_search = False
  def BFS(self,graph, start_node, goal_node):
    queue = [] #this is an empty list, it will be used to track expanded nodes, for UCS replace this with priority queue
    queue.append(start_node)
    #print(queue)
    #set of visited nodes
    self.visited.append(start_node)
    while queue and not self.end_search: #loop as long as there are elements in the queue and you have not reached the goal node
      # Dequeue a vertex from
      s = queue.pop(0) #remove the node at the front of the queue

      # Get all adjacent vertices of the
      # dequeued vertex s (i.e. expand the node).
      # If an adjacent node has not been visited, then mark
      # it visited and enqueue it (i.e. add to visited list)
      for i in list(graph[s]):
        if i not in self.visited:
          #print ("Command; Drive from ",s," to " ,i, " Estate/Junction", end = "\n")
          #print("Current Node is",i, " but the goal Node is ",goal_node)
          print ("Command; Drive to " ,i, " Estate/Junction", end = "\n")
          if i is goal_node: #goal test
            print("We have reached ",i," the final destination")
            self.visited.append(i)
            self.end_search = True
            break
          else:
            #print("Here",self.end_search)
            queue.append(i)
            #visited[i] = True
            self.visited.append(i)

