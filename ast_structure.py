class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # 'operator' or 'operand'
        self.value = value     # Operand condition or operator type ('AND', 'OR')
        self.left = left       # Left child for operator nodes
        self.right = right     # Right child for operator nodes

    def __repr__(self):
        if self.type == "operand":
            return f"Operand({self.value})"
        else:
            return f"Operator({self.value}, left={self.left}, right={self.right})"
