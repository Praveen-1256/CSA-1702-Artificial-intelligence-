class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)
def alpha_beta(node, depth, alpha, beta, max_player):
    if depth == 0 or not node.children:
        return node.value
    if max_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
root = Node(0)
a = Node(5)
b = Node(3)
c = Node(9)
d = Node(6)
root.add_child(a)
root.add_child(b)
a.add_child(c)
a.add_child(d)
result = alpha_beta(root, 3, float('-inf'), float('inf'), True)
print("Optimal Value:", result)
