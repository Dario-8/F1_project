from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="f1",
        database="ergastdb"
    )
    return connection

@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    return jsonify({"you_sent": data}), 201

@app.route('/constructor', methods=['GET'])
def get_constructor():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Get the JSON data from the request body
    constructor_ref = request.args.get('constructor_ref')

    if not constructor_ref:
        return jsonify({"error": "Missing required parameter: constructor_ref"}), 400


    query = "SELECT * FROM constructors WHERE constructorRef = %s"
    cursor.execute(query, (constructor_ref,))
    constructors = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(constructors), 200

@app.route('/lap_times', methods=['GET'])
def get_lap_times():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        raceId = request.args.get('raceId')
        driverId = request.args.get('driverId')

        query = "SELECT * FROM lapTimes lt WHERE lt.raceId = %s AND lt.driverId = %s"
        cursor.execute(query, (raceId, driverId))
        lap_times = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(lap_times), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}, 500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
