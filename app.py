from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My Python Website! This is displayed from Python."

if __name__ == "__main__":
    app.run(debug=True)

