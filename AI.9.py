import itertools

def calculate_total_distance(path, distances):
    total_distance = 0
    n = len(path)
    
    for i in range(n - 1):
        total_distance += distances[path[i]][path[i+1]]
    
    total_distance += distances[path[-1]][path[0]]
    
    return total_distance

def tsp_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    
    shortest_path = None
    shortest_distance = float('inf')
    
    for path in itertools.permutations(cities):
        total_distance = calculate_total_distance(path, distances)
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path
    
    return shortest_path, shortest_distance

distances = [
    [0, 29, 20, 21],
    [29, 0, 15, 16],
    [20, 15, 0, 28],
    [21, 16, 28, 0]
]

shortest_path, shortest_distance = tsp_bruteforce(distances)

if shortest_path:
    print("Shortest TSP Path:", shortest_path)
    print("Shortest TSP Distance:", shortest_distance)
else:
    print("No solution found")
