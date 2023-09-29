import heapq
class UcsTraverser:
    def __init__(self):
        self.visited = set()
        self.shortest_path = []
        self.end_search = False

    def UCS(self, graph, start_node, goal_node):
        priority_queue = [(0, start_node)]


        while priority_queue and not self.end_search:
            print(priority_queue)
            cost, current = heapq.heappop(priority_queue)

            if current in self.visited:
                continue

            print(f"Command: Drive to {current} with cost {cost}")

            if current is goal_node:
                print("We have reached", current, "the final destination")
                self.end_search = True
                self.visited.add(current)
                break

            self.visited.add(current)

            for neighbor, neighbor_cost in graph[current].items():
                if neighbor not in self.visited:
                    neighbor_cost = int(graph[current][neighbor]['weight'])
                    total_cost = cost + neighbor_cost
                    heapq.heappush(priority_queue, (total_cost, neighbor))

        # Create the shortest path from visited nodes
        # we notice that paths taken have the edge existing 
        # in the tuple form (a[0],a[1]), i.e the current and next items 
        # exist as an edge
        shortest_path = self.visited
        visited_tuples = zip(self.visited, self.visited[1:])

        for (pos, i) in enumerate(visited_tuples):
            if i not in graph.edges():
                # delete that index, it's a node pattern that is impossible
                # two nodes that don't have an edge in between them
                del shortest_path[pos]
        # now set up the new visited to be the code
        self.shortest_path = shortest_path

        return self.visited