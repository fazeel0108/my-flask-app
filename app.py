from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"].strip().lower()
        age = request.form["age"].strip()

        if not age.isdigit():
            return f"Hello {name}, please enter a valid age."

        age = int(age)
        if role == "student":
            return f"Hello {name}, your age is {age}, you got {age}% discount."
        elif role == "teacher":
            return f"Hello {name}, you can have it for free."
        else:
            return "Role not recognized."
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
