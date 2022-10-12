from ast import If
from distutils.log import debug
from email import message
from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import render_template
from flask import url_for

app=Flask(__name__)
app.secret_key="key"
@app.route("/")
def home():
    if "logged_in" in session:
        return redirect("/member")
    return render_template("home.html")

@app.route("/member")
def member():
    
    if "logged_in" in session:
        return render_template("member.html")
    else:
        return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    account=request.form["account"]
    password=request.form["password"]
    if request.method=="POST":
        if account=="" or password=="":
            return redirect(url_for("error", message="請輸入帳號、密碼"))
        elif account!="test" or password!="test":
            return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
        else:
            session["logged_in"]=True
            return redirect("/member")


@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("error.html", message=message)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect("/")

@app.route("/getnum/")
def getnum():
    number=request.args.get("num","")
    number=int(number)
    return redirect(url_for("square", number=number))
@app.route("/square/<int:number>")
def square(number):
    number=number**2
    return render_template("square.html", number=number)

if __name__=="__main__":
    app.run(port=3000, debug=True)