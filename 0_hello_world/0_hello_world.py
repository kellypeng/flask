from flask import Flask

# instantiate an instance flask object
app = Flask(__name__)

@app.route('/') # decorator
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(port=5000, debug=True)

