

from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "abcddcba1234"

def wrapper(func):
    def inner(*args,**kwargs):
        if not session.get("user_info"):
            return redirect("/login")

        ret = func(*args,**kwargs)
        return ret
    return inner()

@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "test" and password == "123456":
            session["user_info"] = username
            return redirect("/index")
        else:
            return render_template("login.html",msg = "username or password error")

@app.route("/index",methods = ["GET","POST"])
@wrapper
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)