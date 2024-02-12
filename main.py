from flask import Flask, render_template


app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def about(word):
    definition = word.upper()
    return_variable = {"definition": definition, "word": word}
    return return_variable

if __name__ == "__main__":
    app.run(debug=True, port=5001)