from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/<name>') # <name> positional argument
def index(name = None):
    if request.method == 'GET':
        return render_template('input_name.html')
    elif request.method == 'POST':
        name = request.form.get('firstname')
        surname = request.form.get('surname')
        return render_template('index.html', name=name, fixed='some string')

if __name__ == '__main__':
    app.run(port=4999, debug=True)
