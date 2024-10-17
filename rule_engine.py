import unittest
from rule_engine import RuleEngine

class TestRuleEngine(unittest.TestCase):
    def setUp(self):
        self.rule_engine = RuleEngine()

    def test_create_and_evaluate_rule(self):
        # Create rule
        rule = "age > 30 AND salary > 50000"
        self.rule_engine.create_rule("rule1", rule)
        
        # Test evaluation
        user_data = {"age": 35, "salary": 60000}
        self.assertTrue(self.rule_engine.evaluate_rule("rule1", user_data))

        user_data = {"age": 25, "salary": 60000}
        self.assertFalse(self.rule_engine.evaluate_rule("rule1", user_data))

    def test_or_rule(self):
        # Create rule with OR
        rule = "age > 30 OR salary > 50000"
        self.rule_engine.create_rule("rule2", rule)

        # Test evaluation
        user_data = {"age": 25, "salary": 60000}
        self.assertTrue(self.rule_engine.evaluate_rule("rule2", user_data))

        user_data = {"age": 25, "salary": 40000}
        self.assertFalse(self.rule_engine.evaluate_rule("rule2", user_data))

if __name__ == '__main__':
    unittest.main()
