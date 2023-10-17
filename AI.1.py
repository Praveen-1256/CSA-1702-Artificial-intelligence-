import heapq
goal_state = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
initial_state = ((2, 8, 3), (1, 6, 4), (7, 0, 5))
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

def solve_puzzle(initial_state):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(initial_state), 0, initial_state))
    
    while priority_queue:
        _, cost, current_state = heapq.heappop(priority_queue)
        
        if current_state == goal_state:
            return cost

        if current_state in visited:
            continue

        visited.add(current_state)

        empty_x, empty_y = None, None

        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    empty_x, empty_y = i, j

        for move in moves:
            new_x, new_y = empty_x + move[0], empty_y + move[1]

            if is_valid_move(new_x, new_y):
                new_state = list(map(list, current_state))
                new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
                new_state = tuple(map(tuple, new_state))
                if new_state not in visited:
                    heapq.heappush(priority_queue, (cost + 1 + heuristic(new_state), cost + 1, new_state))

    return -1

steps = solve_puzzle(initial_state)
if steps != -1:
    print(f"Number of steps to reach the goal: {steps}")
else:
    print("No solution found.")
