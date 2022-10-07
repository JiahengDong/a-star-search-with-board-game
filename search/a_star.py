"""
A brief introduction to the methodology behind the A* search algorithm
- A* search evaluation function f(n) = g(n) + h(n):
-     g(n) = cost so far to reach the current cell n (i.e. path cost)
-     h(n) = estimated cost to goal from n
"""


# The heuristic function used in the algorithm is:
# h(n) = [abs(n.r - goal.r) + abs(n.q - goal.q) + abs(n.z - goal.z)] / 2
# This computation method is equivalent to the Manhattan method in a hexagonal board
# This is an admissible heuristic -- h(n) <= h*(n) where h*(n) is the true cost from n
def h(curr, goal):
    # 0 -- row coordinate of a cell
    # 1 -- col coordinate of a cell
    z_axis_curr = -(curr[0] + curr[1])
    z_axis_goal = -(goal[0] + goal[1])
    return (abs(curr[0] - goal[0]) + abs(curr[1] - goal[1]) + abs(z_axis_curr - z_axis_goal)) / 2


# Find all adjacent cells of a given cell which are within the borders
def neighbors(curr, size):
    all_neighbors = []
    size = size - 1

    if 0 <= curr[0] <= size:
        if curr[1] + 1 <= size:
            # Add the neighbour to the right
            all_neighbors.append((curr[0], curr[1] + 1))
        if curr[1] - 1 >= 0:
            # Add the neighbour to the left
            all_neighbors.append((curr[0], curr[1] - 1))

    if curr[0] + 1 <= size:
        # Add the neighbour to the up right
        all_neighbors.append((curr[0] + 1, curr[1]))
        if curr[1] - 1 >= 0:
            # Add the neighbour to the up left
            all_neighbors.append((curr[0] + 1, curr[1] - 1))

    if curr[0] - 1 >= 0:
        # Add the neighbour to the bottom left
        all_neighbors.append((curr[0] - 1, curr[1]))
        if curr[1] + 1 <= size:
            # Add the neighbour to the bottom right
            all_neighbors.append((curr[0] - 1, curr[1] + 1))

    return all_neighbors


def a_star_algorithm(start, goal, occupation, size):
    # This list `visit` begins trivially with the starting node
    # In each iteration:
    # (1) One node with the lowest f-value (initially this is the starting node) is selected from `visit`
    # (2) The neighbours of this picked node are found and added to `visit`
    # (3) The node itself is removed from `visit` at the end of this iteration

    # Create a list `visit` to store the nodes to be visited while constructing the optimal path
    visit = set()
    visit.add(start)

    # Create a list `visited` to store nodes which have been fully expanded
    visited = set()

    # Create a dictionary to store the g-value of each node visited (i.e. the distance from start to the node)
    g = {start: 0}

    # Create a dictionary to store the previous/parent node of each node which has been generated or fully expanded
    parent = {start: None}

    # So long as there are nodes yet to be visited in `visit`, keep on with the iteration
    while len(visit) > 0:
        curr = None

        # Find the particular node in `visit` which has the smallest f-value
        for cell in visit:
            if curr is None or g[cell] + h(cell, goal) < g[curr] + h(curr, goal):
                curr = cell

        # Check if there is lack of the start position
        if curr is None:
            print(0)
            return None

        # If the goal has been found, recover the traversal path by using the information about 'parent' nodes
        # It begins with the goal node, and finds all 'parent' nodes iteratively until meeting the starting node
        if curr == goal:
            path = []
            while parent[curr] is not None:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            # Reverse the path because we are using a backward selection method previously
            path.reverse()
            # Finally, print out the required information about this optimal solution
            print(len(path))
            for cell in path:
                print(cell)
            return path

        # Find the neighbours of the current node
        for cell in neighbors(curr, size):
            # Check if the neighbour has been blocked or not
            if cell not in occupation:
                # If the neighbour is:
                # - neither in `visit` (i.e. has already been added in previous iterations to be visited later)
                # - nor in `visited` (i.e. has already been fully examined and removed from `visit`)
                # then add it to `visit` such that it will be examined at a later time based on f-values
                if cell not in visit and cell not in visited:
                    visit.add(cell)
                    parent[cell] = curr
                    g[cell] = g[curr] + 1
                # If the node is in the `visit` or `visited` list, we determine whether it is shorter from
                # the current to the node or not; if it is shorter, we update the g(n), parent and remove
                # it from the `visited` list if needed
                else:
                    if g[cell] > g[curr] + 1:
                        g[cell] = g[curr] + 1
                        parent[cell] = curr
                        if cell in visited:
                            visited.remove(cell)
                            visit.add(cell)

        visit.remove(curr)
        visited.add(curr)

    # If the list `visit` becomes empty, it means we have visited all nodes but cannot find a valid path
    print(0)
    return None
