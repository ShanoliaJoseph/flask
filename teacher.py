from flask import*
from database import DB,CR
teacher=Blueprint("teacher",__name__)

@teacher.route("/")
def TeacherHome():
    return render_template("teacherhome.html")

@teacher.route("/answerquestion",methods=["post","get"])
def AnswerQuestion():
    CR.execute("SELECT * FROM sdatabase")
    qanda=CR.fetchall()
    if 'submit' in request.form:
        answer=request.form['ans']
        id=request.form['submit']
        sql="UPDATE sdatabase SET answer=%s WHERE id=%s"
        val=(answer,id)
        CR.execute(sql,val)
        DB.commit()
        flash("Answer submited")
        return redirect(url_for("teacher.AnswerQuestion"))
    return render_template('answerquestion.html',qanda=qanda)

@teacher.route("/deletesdatabase",methods=["post","get"])
def deletesdatabase():
    CR.execute("SELECT *FROM sdatabase ")
    res=CR.fetchall()
    if "submit" in request.form:
        id=request.form['submit']
        CR.execute("DELETE FROM sdatabase WHERE id=%s",(id,))
        DB.commit()
        flash("Items Delete")
        return redirect(url_for('teacher.deletesdatabase'))
    return render_template('deletesdatabase.html',res=res)