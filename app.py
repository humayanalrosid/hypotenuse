from flask import Flask, request, render_template

app = Flask("__main__")

@app.route("/")
def home():
    return render_template("hypotenuse.html")

@app.route("/hypotenuse", methods=["get", "post"])
def find_hypo():
    length = float(request.form.get("user_length"))
    base = float(request.form.get("user_base"))

    hypotenuse = (length **2 + base ** 2) ** 0.5

    return render_template("hypotenuse.html", hypotenuse=hypotenuse)

if __name__ == "__main__":
    app.run(debug=True)