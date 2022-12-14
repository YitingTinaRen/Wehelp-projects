from distutils.log import debug
from email import message
from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import render_template
from flask import url_for
from flask import jsonify
import mysql.connector
import json

def checkData(sql, val=()):
    mydb=mysql.connector.connect(pool_name="mypool")
    mycursor=mydb.cursor(dictionary=True)
    mycursor.execute(sql, val)
    myresult=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return myresult

def writeData(sql, val):
    try:
        mydb=mysql.connector.connect(pool_name="mypool")
        mycursor=mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return 1
    except:
        return 0


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
            writeData(sql, val)

        sql="select message.content, member.name from message inner join member on message.member_id=member.id order by message.time desc"
        myresult=checkData(sql)
        
        return render_template("member.html", name=session.get("name"), oldmsg=myresult)
    else:
        return render_template("home.html")

@app.route("/api/member", methods=["GET", "PATCH"])
def apiMember():
    if request.method =="GET":
        usrname=request.args.get("username","")
        sql="select *from member where username= %s"
        val=(usrname,)
        myresult=checkData(sql, val)
        result={"data":None}
        if not myresult or "logged_in" not in session:
            return jsonify(result)
        else:
            result["data"]=myresult[0]
            result["data"].pop("time")
            return jsonify(result)
    else:
        newname=request.get_json().get("name","")
        sql="update member set name= %s where id=%s"
        val=(newname,session["id"],)

        if "logged_in" not in session or not writeData(sql,val):
            return jsonify({"error":True})
        else:
            session["name"]=newname
            return jsonify({"ok":True})



@app.route("/login", methods=["POST"])
def login():
    usrname=request.form["usrname"]
    password=request.form["password"]

    sql="select *from member where username = %s"
    val=(usrname,)
    myresult=checkData(sql, val)
    if not myresult:
        val=(password,)
        myresult=checkData(sql, val)

    if request.method=="POST":
        if usrname=="" or password=="":
            return redirect(url_for("error", message="????????????????????????"))
        elif not myresult:
            return redirect(url_for("error", message="??????????????????????????????"))
        else:
            session["logged_in"]=True
            session["id"]=myresult[0]["id"]
            session["name"]=myresult[0]["name"]
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

    sql="select *from member where username = %s"
    val=(usrname,)
    myresult=checkData(sql, val)
    if not myresult:
        sql="insert into member (name, username,password) values (%s, %s, %s)"
        val=(name, usrname,password)
        writeData(sql, val)

        return render_template("home.html")
    else:
        return redirect(url_for("error", message="?????????????????????"))

if __name__=="__main__":
    dbconfig={
        "host":"localhost",
        "user":"root",
        "password":"0000",
        "database":"website"
    }
    mydb=mysql.connector.connect(
        pool_name="mypool",
        pool_size=3,
        **dbconfig
    )
    mydb.close()
    app.run(port=3000, debug=True)