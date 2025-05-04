from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        role = request.form.get("role").lower().strip()
        age = request.form.get("age").strip()

        if not age.isdigit():
            message = "Please enter a valid age."
        else:
            age = int(age)
            if role == "student":
                message = f"Hello {name}, your age is {age}, you got {age}% discount."
            elif role == "teacher":
                message = f"Hello {name}, you can have it for free."
            else:
                message = "Role not recognized."

    return render_template("form.htm", message=message)


if __name__ == "__main__":
    app.run(debug=True)


