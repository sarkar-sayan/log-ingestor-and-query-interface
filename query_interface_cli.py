import click
import sqlite3
import re
from datetime import datetime

db_path = "logs.db"

@click.group()
def cli():
    pass

@cli.command()
@click.option('--level', help='Filter logs by level')
@click.option('--message', help='Filter logs by message')
@click.option('--resourceId', help='Filter logs by resourceId')
@click.option('--timestamp', help='Filter logs by timestamp (format: YYYY-MM-DDTHH:MM:SSZ)')
@click.option('--traceId', help='Filter logs by traceId')
@click.option('--spanId', help='Filter logs by spanId')
@click.option('--commit', help='Filter logs by commit')
@click.option('--parentResourceId', help='Filter logs by parentResourceId in metadata')
@click.option('--date-range', help='Filter logs within a date range (format: YYYY-MM-DD to YYYY-MM-DD)')
@click.option('--regex', help='Use regular expression for flexible search')
def query_logs(level, message, resourceId, timestamp, traceId, spanId, commit, parentResourceId, date_range, regex):
    try:
        # Build query parameters
        query_params = {
            'level': level,
            'message': message,
            'resourceId': resourceId,
            'timestamp': timestamp,
            'traceId': traceId,
            'spanId': spanId,
            'commit': commit,
            'metadata.parentResourceId': parentResourceId
        }

        # Apply date range filter if provided
        if date_range:
            start_date, end_date = map(str.strip, date_range.split(' to '))
            query_params['timestamp'] = f'{start_date}T00:00:00Z AND {end_date}T23:59:59Z'

        # Apply regular expression filter if provided
        if regex:
            for key in query_params:
                if query_params[key]:
                    query_params[key] = {'$regex': regex}

        # Retrieve logs based on query parameters
        logs = search_logs(query_params)

        print_logs(logs)
    except Exception as e:
        print(f"Error querying logs: {e}")


def search_logs(query_params):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Build a SQL query based on the provided parameters
    query = "SELECT * FROM logs WHERE "
    conditions = []

    for key, value in query_params.items():
        if value:
            conditions.append(f"{key} = '{value}'")

    query += " AND ".join(conditions)

    # Execute the query
    cursor.execute(query)
    logs = cursor.fetchall()

    conn.close()
    return logs

def print_logs(logs):
    for log in logs:
        print(log)

if __name__ == '__main__':
    cli()