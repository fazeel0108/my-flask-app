from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        age = request.form['age']
        return render_template('3.html', name=name, role=role, age=age)
    return render_template ('form.html')  # Show the form on GET

if __name__ == '__main__':
    app.run(debug=True)
