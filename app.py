from flask import Flask, request, jsonify
from rule_engine import RuleEngine

app = Flask(__name__)

# Initialize Rule Engine
rule_engine = RuleEngine()

@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.json
    rule = data.get("rule")
    rule_name = data.get("rule_name")
    
    if rule and rule_name:
        rule_engine.create_rule(rule_name, rule)
        return jsonify({"message": f"Rule '{rule_name}' created successfully"})
    return jsonify({"error": "Invalid input"}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    data = request.json
    rule_name = data.get("rule_name")
    user_data = data.get("user_data")

    if rule_name and user_data:
        eligible = rule_engine.evaluate_rule(rule_name, user_data)
        return jsonify({"eligible": eligible})
    return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
