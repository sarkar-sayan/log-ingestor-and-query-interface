from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
db_path = "logs.db"

# Endpoint for log queries
@app.route('/query', methods=['GET'])
def query_logs():
    try:
        # Extract query parameters from the request
        query_params = request.args

        # Retrieve logs based on query parameters
        logs = search_logs(query_params)

        return jsonify({"status": "success", "logs": logs}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Search logs based on query parameters
def search_logs(query_params):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Build a SQL query based on the provided parameters
    query = "SELECT * FROM logs WHERE "
    conditions = []

    for key, value in query_params.items():
        conditions.append(f"{key} = '{value}'")

    query += " AND ".join(conditions)

    # Execute the query
    cursor.execute(query)
    logs = cursor.fetchall()

    conn.close()
    return logs

if __name__ == '__main__':
    app.run(port=3000)  # You can choose a different port for the query interface