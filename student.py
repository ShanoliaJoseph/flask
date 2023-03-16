from flask import *
from database import DB,CR
from datetime import datetime
student=Blueprint("student",__name__)
@student.route("/")
def StudentHome():
    CR.execute("SELECT * FROM sdatabase")
    res=CR.fetchall()
    return render_template("studenthome.html",res=res)
@student.route("/askquestion",methods=["post","get"])
def askquestion():
    if "submit" in request.form:
        question =request.form['question']
        date=datetime.now()
        sql='INSERT INTO sdatabase(question,date)VALUES(%s,%s)'
        val=(question,date)
        CR.execute(sql,val)
        DB.commit()
        flash("Question submitted")
        return redirect(url_for('student.StudentHome'))
    return render_template("askquestion.html")