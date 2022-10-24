from ast import If
from distutils.log import debug
from email import message
from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import render_template
from flask import url_for
import mysql.connector

def checkData(item):
    sql="select *from member where account = %s"
    val=(item,)
    mycursor.execute(sql, val)
    myresult=mycursor.fetchall()
    return myresult

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
        return render_template("member.html", usrname=session.get("usrname"))
    else:
        return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    account=request.form["account"]
    password=request.form["password"]

    myresult=checkData(account)
    if not myresult:
        myresult=checkData(password)

    if request.method=="POST":
        if account=="" or password=="":
            return redirect(url_for("error", message="請輸入帳號、密碼"))
        elif not myresult:
            return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
        else:
            session["logged_in"]=True
            session["id"]=myresult[0][0]
            session["usrname"]=myresult[0][1]
            session["account"]=account
            session["password"]=password
            return redirect("/member")


@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("error.html", message=message)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session["usrname"]=False
    session["account"]=False
    session["password"]=False
    return redirect("/")

@app.route("/signup", methods=["POST"])
def signup():
    usrname=request.form["usrname"]
    account=request.form["account"]
    password=request.form["password"]

    myresult=checkData(account)
    if not myresult:
        sql="insert into member (usrname, account,password) values (%s, %s, %s)"
        val=(usrname, account,password)
        mycursor.execute(sql, val)
        mydb.commit()

        return render_template("home.html")
    else:
        return redirect(url_for("error", message="帳號已經被註冊"))

if __name__=="__main__":
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",
        database="hw6"
    )
    mycursor=mydb.cursor()
  
    app.run(port=3000, debug=True)