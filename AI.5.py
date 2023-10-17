from collections import deque
initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

def is_valid_state(state):
    m, c, b = state
    if 0 <= m <= 3 and 0 <= c <= 3:
        if m < c and m > 0:
            return False
        if 3 - m < 3 - c and 3 - m > 0:
            return False
        return True
    return False

def get_next_states(state):
    next_states = []
    m, c, b = state

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for move in moves:
        if b == 1:  
            new_state = (m - move[0], c - move[1], 0)
        else:
            new_state = (m + move[0], c + move[1], 1)
        
        if is_valid_state(new_state):
            next_states.append(new_state)

    return next_states

def solve_missionaries_cannibals(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        visited.add(current_state)

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))

    return None
solution_path = solve_missionaries_cannibals(initial_state, goal_state)

if solution_path:
    print("Solution found:")
    for i, state in enumerate(solution_path):
        print(f"Step {i + 1}: {state}")
else:
    print("No solution found.")
