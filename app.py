from flask import Flask, request, send_from_directory
from flask_cors import CORS
import subprocess
import os
import venv
import unittest

# Create a virtual environment
venv_dir = "./GPTvenv"
venv.create(venv_dir, with_pip=True)

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.get_json()
    code = data['code']
    # Use the Python interpreter from the virtual environment
    python_exe = os.path.join(venv_dir, 'bin', 'python')
    result = subprocess.run([python_exe, '-c', code], capture_output=True, text=True)
    return result.stdout or result.stderr

@app.route('/create', methods=['POST'])
def create_file():
    data = request.get_json()
    filename = data.get('filename') or data.get('file_name')
    code = data.get('code') or data.get('file_content')
    with open(filename, 'w') as f:
        f.write(code)
    return f'Successfully created {filename}'

@app.route('/install', methods=['POST'])
def install_package():
    data = request.get_json()
    package = data.get('package') or data.get('package_name')
    if package is None:
        return "No package provided", 400
    # Use the pip from the virtual environment
    pip_exe = os.path.join(venv_dir, 'bin', 'pip')
    result = subprocess.run([pip_exe, 'install', package], capture_output=True, text=True)
    return result.stdout or result.stderr

@app.route('/run-unit-tests', methods=['POST'])
def run_unit_tests():
    file = request.json['file']
    suite = unittest.TestLoader().loadTestsFromName(file)
    result = unittest.TextTestRunner().run(suite)
    return {
        'total': result.testsRun,
        'failures': len(result.failures),
        'errors': len(result.errors),
        'successes': result.testsRun - len(result.failures) - len(result.errors)
    }

@app.route('/.well-known/<path:filename>')
def well_known(filename):
    return send_from_directory('.well-known', filename)

@app.route('/<path:filename>')
def root_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(port=3333)
