from collections import deque

# Define the capacities of the two jugs and the target amount of water.
jug1_capacity = 5
jug2_capacity = 3
target_amount = 2

# Create a state class to represent the state of the two jugs.
class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

    def __str__(self):
        return f"({self.jug1}, {self.jug2})"

# Define possible actions.
def pour_jug1_to_jug2(state):
    if state.jug1 > 0 and state.jug2 < jug2_capacity:
        amount = min(state.jug1, jug2_capacity - state.jug2)
        return State(state.jug1 - amount, state.jug2 + amount)
    return None

def pour_jug2_to_jug1(state):
    if state.jug2 > 0 and state.jug1 < jug1_capacity:
        amount = min(state.jug2, jug1_capacity - state.jug1)
        return State(state.jug1 + amount, state.jug2 - amount)
    return None

def fill_jug1(state):
    return State(jug1_capacity, state.jug2)

def fill_jug2(state):
    return State(state.jug1, jug2_capacity)

def empty_jug1(state):
    return State(0, state.jug2)

def empty_jug2(state):
    return State(state.jug1, 0)

# Define the BFS algorithm to solve the Water Jug Problem.
def solve_water_jug_problem():
    initial_state = State(0, 0)
    visited = set()
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()

        if current_state.jug1 == target_amount or current_state.jug2 == target_amount:
            return current_state

        visited.add(current_state)

        actions = [pour_jug1_to_jug2, pour_jug2_to_jug1, fill_jug1, fill_jug2, empty_jug1, empty_jug2]

        for action in actions:
            next_state = action(current_state)
            if next_state and next_state not in visited and next_state not in queue:
                queue.append(next_state)

    return None

# Find and print the solution.
solution_state = solve_water_jug_problem()

if solution_state:
    print("Solution found:")
    print(f"Jug 1: {solution_state.jug1} liters")
    print(f"Jug 2: {solution_state.jug2} liters")
else:
    print("No solution found.")
