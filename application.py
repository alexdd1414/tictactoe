from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
 
app = Flask(__name__)
 
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
 
@app.route("/")
def index():
 
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
    else:
        if session["turn"] == "X":
                session["turn"] = "O"
        else:
                session["turn"] = "X"
 
    return render_template("game.html", game=session["board"], turn=session["turn"])
 
@app.route("/play/<int:row>/<int:col>")
def play(row, col):

        session["board"][row][col] = session["turn"]

        # if (session["board"][0][0] && session["board"][0][1] && session["board"][0][2]) == "X": 
        # elif (session["board"][1][0] && session["board"][1[1] && session["board"][1][2]) == "X": 
        # elif (session["board"][2][0] && session["board"][2][1] && session["board"][2][2]) == "X": 
        # elif (session["board"][0][0] && session["board"][1][0] && session["board"][2][0]) == "X": 
        # elif (session["board"][0][1] && session["board"][0][0] && session["board"][0][0]) == "X": 
        # elif (session["board"][0][0] && session["board"][0][0] && session["board"][0][0]) == "X": 
        # elif (session["board"][0][0] && session["board"][0][0] && session["board"][0][0]) == "X": 
        # else (session["board"][0][0] && session["board"][0][0] && session["board"][0][0]) == "X": 


        return redirect(url_for("index"))
