from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize global variables to store coordinates
coordinates = {'x': 300, 'y': 200}  # Default position

# Route to update coordinates via POST request
@app.route('/update_coordinates', methods=['POST'])
def update_coordinates():
    global coordinates
    data = request.get_json()
    if 'x' in data and 'y' in data:
        coordinates['x'] = data['x']
        coordinates['y'] = data['y']
        return jsonify({'message': 'Coordinates updated successfully'}), 200
    else:
        return jsonify({'error': 'Invalid coordinates'}), 400

# Route to get the current coordinates via GET request
@app.route('/get_coordinates', methods=['GET'])
def get_coordinates():
    return jsonify(coordinates), 200

if __name__ == '__main__':
    app.run(debug=True)
