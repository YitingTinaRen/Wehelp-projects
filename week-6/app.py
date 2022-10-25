from distutils.log import debug
from email import message
from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import render_template
from flask import url_for
import mysql.connector

def checkMember(item):
    sql="select *from member where username = %s"
    val=(item,)
    mycursor.execute(sql, val)
    myresult=mycursor.fetchall()
    return myresult

def showAllData(table):
    sql="select *from "+ table
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    print(myresult)
    return myresult

def connect2DB(thedatabase):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",
        database=thedatabase
    )
    mycursor=mydb.cursor()
    return [mydb, mycursor]

app=Flask(__name__)
app.secret_key="key"
@app.route("/")
def home():
    if "logged_in" in session:
        return redirect("/member")
    return render_template("home.html")

@app.route("/member", methods=["GET","POST"])
def member():

    if "logged_in" in session:
        if request.method=='POST':
            newmsg=request.form["msg"]
            sql="insert into message (member_id, content)values(%s, %s)"
            val=(session["id"],newmsg,)
            mycursor.execute(sql,val)
            mydb.commit()

        sql="select message.content, member.name from message inner join member on message.member_id=member.id order by message.time desc"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template("member.html", name=session.get("name"), oldmsg=myresult)
    else:
        return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    usrname=request.form["usrname"]
    password=request.form["password"]

    myresult=checkMember(usrname)
    if not myresult:
        myresult=checkMember(password)

    if request.method=="POST":
        if usrname=="" or password=="":
            return redirect(url_for("error", message="請輸入帳號、密碼"))
        elif not myresult:
            return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
        else:
            session["logged_in"]=True
            session["id"]=myresult[0][0]
            session["name"]=myresult[0][1]
            session["usrname"]=usrname
            session["password"]=password
            return redirect("/member")


@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("error.html", message=message)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session["name"]=False
    session["usrname"]=False
    session["password"]=False
    return redirect("/")

@app.route("/signup", methods=["POST"])
def signup():
    name=request.form["name"]
    usrname=request.form["usrname"]
    password=request.form["password"]

    myresult=checkMember(usrname)
    if not myresult:
        sql="insert into member (name, username,password) values (%s, %s, %s)"
        val=(name, usrname,password)
        mycursor.execute(sql, val)
        mydb.commit()

        return render_template("home.html")
    else:
        return redirect(url_for("error", message="帳號已經被註冊"))

if __name__=="__main__":
    [mydb, mycursor]=connect2DB("website")
    showAllData("member")
    app.run(port=3000, debug=True)