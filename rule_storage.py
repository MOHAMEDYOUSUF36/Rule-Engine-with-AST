import sqlite3
import json

def init_db():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule_name TEXT,
        rule_ast TEXT
    )
    ''')
    conn.commit()
    conn.close()

def save_rule(rule_name, rule_ast):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    rule_ast_json = json.dumps(rule_ast, default=lambda o: o.__dict__)
    cursor.execute('INSERT INTO rules (rule_name, rule_ast) VALUES (?, ?)', (rule_name, rule_ast_json))
    conn.commit()
    conn.close()

def load_rule(rule_name):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('SELECT rule_ast FROM rules WHERE rule_name = ?', (rule_name,))
    result = cursor.fetchone()
    conn.close()
    return json.loads(result[0]) if result else None
