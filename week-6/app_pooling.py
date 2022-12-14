from distutils.log import debug
from email import message
from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import render_template
from flask import url_for
import mysql.connector

def checkData(sql, val=()):
    # [mydb, mycursor]=connect2DB('website')
    mydb=mysql.connector.connect(pool_name="mypool")
    print(mydb.pool_name)
    mycursor=mydb.cursor()
    mycursor.execute(sql, val)
    myresult=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return myresult

def writeData(sql, val):
    # [mydb, mycursor]=connect2DB('website')
    mydb=mysql.connector.connect(pool_name="mypool")
    mycursor=mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()


def connect2DB():
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
            writeData(sql, val)

        sql="select message.content, member.name from message inner join member on message.member_id=member.id order by message.time desc"
        myresult=checkData(sql)
        print(myresult)
        return render_template("member.html", name=session.get("name"), oldmsg=myresult)
    else:
        return render_template("home.html")

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