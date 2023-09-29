import heapq
class UcsTraverser:
    def __init__(self):
        self.visited = set()
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


        return self.visited