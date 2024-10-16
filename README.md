# Rule-Engine-with-AST
Tier Rule Engine Application

## Overview
This is a simple rule engine system using Abstract Syntax Trees (AST) to dynamically create, combine, and evaluate rules. The system determines user eligibility based on attributes like age, department, salary, etc.

## Setup

1. Clone the repository.
2. Install dependencies: `pip install flask`
3. Run the app: `python app.py`
4. The API will be available at `http://localhost:5000`.

## API Endpoints

- **POST /create_rule**
  - Request: `{ "rule": "age > 30", "rule_name": "rule1" }`
  - Response: `{ "message": "Rule 'rule1' created successfully" }`

- **POST /evaluate_rule**
  - Request: `{ "rule_name": "rule1", "user_data": { "age": 35, "salary": 60000 } }`
  - Response: `{ "eligible": true }`

## Testing

To run tests:
python -m unittest test_rule_engine.py

