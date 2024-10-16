from ast_structure import Node

# Function to parse a rule string and return its AST
def create_rule(rule_string):
    # This is a simplified parser, more complex parsers can be implemented
    tokens = rule_string.split()  # For example, tokenize the rule string by space
    return parse_tokens(tokens)

def parse_tokens(tokens):
    if len(tokens) == 1:
        return Node(node_type="operand", value=tokens[0])
    
    operator = tokens[1]
    left_operand = Node(node_type="operand", value=tokens[0])
    right_operand = Node(node_type="operand", value=tokens[2])
    
    return Node(node_type="operator", value=operator, left=left_operand, right=right_operand)

# Function to combine multiple rules into a single AST
def combine_rules(rules):
    combined_ast = None
    for rule in rules:
        rule_ast = create_rule(rule)
        if combined_ast:
            combined_ast = Node(node_type="operator", value="AND", left=combined_ast, right=rule_ast)
        else:
            combined_ast = rule_ast
    return combined_ast

# Function to evaluate the AST against data
def evaluate_rule(ast, data):
    if ast.type == "operand":
        condition = ast.value.split(' ')
        field, operator, value = condition[0], condition[1], int(condition[2])

        if operator == '>':
            return data[field] > value
        elif operator == '<':
            return data[field] < value
        elif operator == '=':
            return data[field] == value
        else:
            raise Exception("Invalid operator")
    
    elif ast.type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
        else:
            raise Exception("Invalid operator in AST")
