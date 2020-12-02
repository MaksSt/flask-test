from flask import \
   Flask, \
   render_template, \
   request, \
   redirect, \
   url_for

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def index():
    return redirect( url_for('main') )

@app.route("/main")
def main():
   return render_template("main.html")

@app.route("/gg")
def gg():
   return render_template("gg.html")

@app.route("/first")
def first():
   return render_template("first.html")

@app.route("/second")
def second():
   return render_template("second.html")

@app.route("/three")
def three():
   return render_template("three.html")