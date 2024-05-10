from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Specify the port number here
    port = 443  # Example port number for HTTPS traffic
    app.run(port=port)
