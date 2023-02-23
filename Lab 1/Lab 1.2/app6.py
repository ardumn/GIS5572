import psycopg2
from flask import Flask, jsonify
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/get_polygon', methods=['GET'])
def get_polygon():
    connection= psycopg2.connect(host = '107.178.210.122',
                             database = 'lab0',
                             user = 'postgres',
                             password = 'ARDGISumn1994123')

    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(sql.SQL("SELECT table2, ST_AsGeoJSON(polygon)::json AS geometry FROM table2"), (1,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify(result)