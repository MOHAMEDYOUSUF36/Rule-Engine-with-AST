import unittest
from rule_engine import create_rule, combine_rules, evaluate_rule

class TestRuleEngine(unittest.TestCase):
    
    def test_create_rule(self):
        rule = "age > 30"
        ast = create_rule(rule)
        self.assertEqual(ast.value, ">")
        self.assertEqual(ast.left.value, "age")
        self.assertEqual(ast.right.value, "30")
    
    def test_combine_rules(self):
        rules = ["age > 30", "salary > 50000"]
        combined_ast = combine_rules(rules)
        self.assertEqual(combined_ast.value, "AND")
    
    def test_evaluate_rule(self):
        rule = "age > 30"
        ast = create_rule(rule)
        data = {"age": 35}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
