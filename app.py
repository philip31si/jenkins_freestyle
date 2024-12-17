from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route for rendering the calculator interface
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the calculation
@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    try:
        # Parse the JSON data from the frontend
        data = request.get_json()
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))
        operation = data.get('operation')

        # Perform the calculation based on the operation
        if operation == 'addition':
            result = num1 + num2
        elif operation == 'subtraction':
            result = num1 - num2
        elif operation == 'multiplication':
            result = num1 * num2
        elif operation == 'division':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed.'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation.'}), 400

        # Return the result as JSON
        return jsonify({'result': result})

    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)}), 500




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
#this will run in local only and i need to run in public also
