from flask import Flask, jsonify, send_from_directory, render_template
import os

app = Flask(__name__)

# Path to your reports folder
REPORTS_FOLDER = os.path.join(os.getcwd(), 'reports')

# Function to get file creation time
def get_creation_time(file_path):
    return os.path.getctime(file_path)

# Route to get the list of HTML and video files
@app.route('/api/reports', methods=['GET'])
def get_reports():
    try:
        # List all .html and .webm files in the reports folder
        files = [f for f in os.listdir(REPORTS_FOLDER) if f.endswith(('.html', '.webm'))]
        files.sort(key=lambda f: get_creation_time(os.path.join(REPORTS_FOLDER, f)))
        return jsonify(files)
    except Exception as e:
        return jsonify({'error': str(e)})

# Route to serve a specific file
@app.route('/reports/<path:filename>', methods=['GET'])
def serve_report(filename):
    return send_from_directory(REPORTS_FOLDER, filename)

# Serve the HTML page (static)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
