from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            # Redirect to success page if credentials match
            return redirect(url_for('index'))
        else:
            # Render login page again if credentials do not match
            return render_template('main.html')
    # Render login page for GET requests
    return render_template('main.html')

@app.route('/next')
def next():
    return render_template('temp.html')

@app.route('/run',methods=['POST'])
def Run():
    subprocess.run(['python', 'app.py'])
    return redirect(url_for('index'))


@app.route('/execute', methods=['POST'])
def execute():
    text_input = request.form['full_name']
    # text_input = request.form['text_input']
    print(text_input)

    # Execute label.py with input_received
    subprocess.run(['python', 'label.py', text_input])

    # Execute update.py

    subprocess.run(['python', 'update.py'])

    # Execute app.py
    subprocess.run(['python', 'app.py'])

    # Execute train.py
    subprocess.run(['python', 'train.py'])

    return redirect(url_for('next'))

if __name__ == '__main__':
    app.run(debug=True)
