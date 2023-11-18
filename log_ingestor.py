from flask import Flask, request, jsonify
import sqlite3
from elasticsearch import Elasticsearch

app = Flask(__name__)
db_path = "logs.db"

# Initialize Elasticsearch connection
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])  # Adjust host and port as needed

# Endpoint for log ingestion
@app.route('/ingest', methods=['POST'])
def ingest_log():
    try:
        log_data = request.get_json()

        # Validate log format
        validate_log(log_data)

        # Store log in database
        store_log_sqlite(log_data)
        store_log_elasticsearch(log_data)

        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Validate log format
def validate_log(log_data):
    required_fields = ["level", "message", "resourceId", "timestamp", "traceId", "spanId", "commit", "metadata"]
    
    # Check if all required fields are present
    for field in required_fields:
        if field not in log_data:
            raise ValueError(f"Missing required field: {field}")

    # Check the data types and formats of individual fields
    if not isinstance(log_data["level"], str):
        raise ValueError("Field 'level' must be a string")
    
    if not isinstance(log_data["message"], str):
        raise ValueError("Field 'message' must be a string")
    
    if not isinstance(log_data["resourceId"], str):
        raise ValueError("Field 'resourceId' must be a string")
    
    # Add similar checks for other fields
    # Check the format of the timestamp using a regular expression
    timestamp_pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"
    if not re.match(timestamp_pattern, log_data["timestamp"]):
        raise ValueError("Invalid timestamp format")

    # Validate metadata field
    if "metadata" in log_data:
        if not isinstance(log_data["metadata"], dict):
            raise ValueError("Field 'metadata' must be a dictionary")

        # Check for the presence of the parentResourceId field in metadata
        if "parentResourceId" not in log_data["metadata"]:
            raise ValueError("Missing required field 'parentResourceId' in metadata")
        if not isinstance(log_data["metadata"]["parentResourceId"], str):
            raise ValueError("Field 'parentResourceId' in metadata must be a string")

# Store log in SQLite database
def store_log_sqlite(log_data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Create a table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS logs
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           level TEXT,
                           message TEXT,
                           resourceId TEXT,
                           timestamp TEXT,
                           traceId TEXT,
                           spanId TEXT,
                           commit TEXT,
                           parentResourceId TEXT)''')
        # Insert log into the table
        cursor.execute('''INSERT INTO logs (level, message, resourceId, timestamp, traceId, spanId, commit, parentResourceId)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (log_data['level'], log_data['message'], log_data['resourceId'],
                        log_data['timestamp'], log_data['traceId'], log_data['spanId'],
                        log_data['commit'], log_data['metadata']['parentResourceId']))

        conn.commit()
        print("Log stored in SQLite successfully.")
    except Exception as e:
        print(f"Error storing log in SQLite: {e}")
    finally:
        conn.close()

# Store log in Elasticsearch
def store_log_elasticsearch(log_data):
    try:
        # Index log in Elasticsearch
        es.index(index='logs', body=log_data)
        print("Log stored in Elasticsearch successfully.")
    except Exception as e:
        print(f"Error storing log in Elasticsearch: {e}")


if __name__ == '__main__':
    app.run(port=3000)
