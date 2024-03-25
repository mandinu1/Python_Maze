import heapq
import random

def finding_the_coordinate(node, columns):
    y = node // columns  # finding the row
    x = node % columns  # finding the column
    return x, y

def valid_move(x, y):
    return 0 <= x < rows and 0 <= y < columns and Maze[y][x] != "B"  # Adjusted indices

def finding_neighbors(x, y):
    neighbors = []
    for ix in [-1, 0, 1]:
        for iy in [-1, 0, 1]:
            if ix == 0 and iy == 0:
                continue
            new_x, new_y = x + ix, y + iy
            if valid_move(new_x, new_y):
                neighbors.append((new_x, new_y))
    return neighbors

def depth_first_search(current_node, goal_node, columns, rows):
    stack = [(current_node, [current_node])]
    visited = set()

    while stack:
        node, path = stack.pop()
        x, y = finding_the_coordinate(node, columns)

        if node == goal_node:
            return path

        if node not in visited:
            visited.add(node)
            neighbors = finding_neighbors(x, y)
            neighbors.sort()  # Sort neighbors in increasing order


            for neighbor_x, neighbor_y in neighbors:
                neighbor_node = neighbor_y * columns + neighbor_x  # Adjusted indices
                if neighbor_node not in visited:
                    stack.append((neighbor_node, path + [neighbor_node]))

    return []
def heuristic(node, goal_node, columns):
    x1, y1 = finding_the_coordinate(node, columns)
    x2, y2 = finding_the_coordinate(goal_node, columns)
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(start_node, goal_node, columns, rows):
    heap = [(0, start_node, [start_node])]
    visited = set()

    while heap:
        _, node, path = heapq.heappop(heap)

        if node == goal_node:
            return path

        if node not in visited:

            visited.add(node)
            x, y = finding_the_coordinate(node, columns)
            neighbors = finding_neighbors(x, y)
            neighbors.sort()  # Sort neighbors in increasing order

            for neighbor_x, neighbor_y in neighbors:
                neighbor_node = neighbor_y * columns + neighbor_x
                if neighbor_node not in visited:
                    new_path = path + [neighbor_node]
                    cost = len(new_path) + heuristic(neighbor_node, goal_node, columns)
                    heapq.heappush(heap, (cost, neighbor_node, new_path))
                    #print(f"Heuristic for Node {neighbor_node}: {heuristic(neighbor_node, goal_node, columns)}")

    return []

Maze = [
    ["0", "6", "12", "18", "24", "30"],
    ["1", "7", "13", "19", "25", "31"],
    ["2", "8", "14", "20", "26", "32"],
    ["3", "9", "15", "21", "27", "33"],
    ["4", "10", "16", "22", "28", "34"],
    ["5", "11", "17", "23", "29", "35"]
]

columns = 6
rows = 6
start_node = random.randint(0, 11)
x, y = finding_the_coordinate(start_node, columns)
Maze[x][y] = "S"  # Adjusted indices
goal_node = random.randint(24, 35)
x, y = finding_the_coordinate(goal_node, columns)
Maze[x][y] = "G"  # Adjusted indices
Available_nodes = []
for i in range(36):
    if i != start_node and i != goal_node:
        Available_nodes.append(i)
barrier_nodes = random.sample(Available_nodes, 4)
print(barrier_nodes)
print(f"start{start_node} goal {goal_node}")
for b_node in barrier_nodes:
    x, y = finding_the_coordinate(b_node, columns)
    Maze[x][y] = "B"  # Adjusted indices
for row in Maze:  # Adjusted variable name to avoid conflict
    print(row)

visited_nodes = set()

# Perform DFS
path = depth_first_search(start_node, goal_node, columns, rows)
visited_nodes = set(path)
time_to_find_goal = len(visited_nodes)  # Each node takes 1 minute


path_a_star = a_star_search(start_node, goal_node, columns, rows)
visited_nodes_a_star = set(path_a_star)
time_to_find_goal_a_star = len(visited_nodes_a_star)

# Display results
print("Visited nodes:", visited_nodes)
print("Time to find goal:", time_to_find_goal, "minutes")
print("Final Path:", path)

print("\nA* Search - Visited nodes:", visited_nodes_a_star)
print("A* Search - Time to find goal:", time_to_find_goal_a_star, "minutes")
print("A* Search - Final Path:", path_a_star)