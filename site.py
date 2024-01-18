from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def send_file():
    return send_from_directory('.', 'site.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
