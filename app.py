from flask import flask, render_template
from flask_ngrok import run_with_ngrok

app = flask(__name__)

@app.route("/")
def halamanCV():
    return render_template("cv_elsa.html")

if __name__== "__main__":
    run_with_ngerok(app)
    app.run()