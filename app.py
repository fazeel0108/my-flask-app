from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        age = request.form['age']
        return render_template('3.html', name=name, role=role, age=age)
    return render_template('form.html')  # Serving the form initially

if __name__ == '__main__':
    app.run(debug=True)
