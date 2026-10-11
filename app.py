
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        event = request.form.get("event", "").strip()

        if not name or not email or not event:
            return render_template(
                "index.html",
                error="Please fill in all fields."
            ), 400

        return render_template(
            "index.html",
            success=True,
            name=name,
            event=event
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
