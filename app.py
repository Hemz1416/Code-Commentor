# app.py
from flask import Flask, request, jsonify, render_template
from ai_commentor import perform_ai_action
import os

# Initialize the Flask application
app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))

@app.route('/')
def index():
    """
    Serves the main HTML page of the application.
    """
    # Renders the index.html file located in the same directory
    return render_template('index.html')

@app.route('/action', methods=['POST'])
def handle_ai_action():
    """
    Handles AI action requests from the frontend.
    It expects a JSON payload with 'code' and 'action' keys.
    """
    data = request.get_json()
    if not data or 'code' not in data or 'action' not in data:
        return jsonify({'error': 'Missing code or action in request'}), 400

    code_from_request = data['code']
    action_from_request = data['action']

    # Call the correct AI function to get the processed code
    processed_code = perform_ai_action(code_from_request, action_from_request)
    
    # Return the result as JSON
    return jsonify({'processed_code': processed_code})

if __name__ == '__main__':
    # Run the Flask app
    # Use host='0.0.0.0' to make it accessible on your local network
    app.run(debug=True, port=5000)

