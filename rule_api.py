from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule
from rule_storage import save_rule, load_rule

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule')
    rule_name = request.json.get('rule_name')
    rule_ast = create_rule(rule_string)
    save_rule(rule_name, rule_ast)
    return jsonify({"message": f"Rule '{rule_name}' created successfully", "rule_ast": rule_ast}), 201

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    rule_name = request.json.get('rule_name')
    user_data = request.json.get('user_data')
    rule_ast = load_rule(rule_name)
    if not rule_ast:
        return jsonify({"error": "Rule not found"}), 404
    result = evaluate_rule(rule_ast, user_data)
    return jsonify({"eligible": result}), 200

if __name__ == '__main__':
    app.run(debug=True)
