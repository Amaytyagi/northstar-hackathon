from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'landing.html')

@app.route('/landing')
def landing():
    return send_from_directory('.', 'landing.html')

@app.route('/app')
def app_view():
    return send_from_directory('.', 'app.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
