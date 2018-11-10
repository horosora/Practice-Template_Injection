from flask import Flask
from flask import render_template
from flask import render_template_string
from flask import request


app = Flask(__name__)
app.config["FLAG"] = "FLAG{hoge_fuga_piyo}"

def escape(s):
    return s.replace("config", "")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/confirm", methods=["GET", "POST"])
def confirm():
    html = "<p><b>Message:</b></p>"
    if request.method == "POST":
        html += escape(request.form["message"])
    return render_template_string(html)


if __name__ == "__main__":
    #app.debug = True
    app.run(host="localhost", port=8080)
