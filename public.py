from flask import*
from database import DB,CR
# from flask import Flask,request, render_template,redirect,url_for,flash
public=Blueprint("public",__name__)

@public.route("/",methods=["post","get"])
def SignIn():
    if 'submit' in request.form:
        username=request.form["username"]
        password=request.form["password"]
        sql="SELECT * FROM user WHERE username=%s AND password=%s"
        val=(username,password)
        CR.execute(sql,val)
        result=CR.fetchall()
        if result:
            if result [0]['usertype']=='teacher':
                return redirect(url_for("teacher.TeacherHome"))
            if result[0]['usertype']=="Student":
                return redirect(url_for("student.StudentHome"))
            else:
                flash("username or password incorrect")
    return render_template("login.html")
@public.route("/register",methods=["post","get"])
def signup():
    if 'submit' in request.form:
        name=request.form["name"]
        username=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        usertype=request.form["utype"]

        sql="SELECT * FROM user WHERE  username=%s OR email=%s"
        val=(username,email)
        CR.execute(sql,val)
        result=CR.fetchall()

        if result:
            flash("Username or Email id exists")
        else:
            sql='INSERT INTO user(name,username,email,password,usertype)VALUES(%s,%s,%s,%s,%s)'
            val=(name,username,email,password,usertype)
            CR.execute(sql,val)
            DB.commit()
            return render_template("login.html")
    return render_template("register.html")
@public.route("/logout")
def logout():
    return redirect(url_for("public.SignIn"))