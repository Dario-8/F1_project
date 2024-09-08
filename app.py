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
    data = request.get_json()

    if not data or 'constructorRef' not in data:
        return jsonify({"error": "Missing required parameter: constructorRef"}), 400

    constructor_ref = data['constructorRef']

    query = "SELECT * FROM constructors WHERE constructorRef = %s"
    cursor.execute(query, (constructor_ref,))
    constructors = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(constructors), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
