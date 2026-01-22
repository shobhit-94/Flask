from flask import Flask,request,redirect,url_for,session,Response,render_template
from livereload import Server
app=Flask(__name__)
app.secret_key="supersecret"

#homepage login page
@app.route('/',methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=="admin" and password=="123":
            session['user']=username #store in session
            return redirect(url_for("welcome"))
        else:
            return Response("In-vaild credintals,Try again",mimetype="text/plain")#we are accepting only text which is plain with not html and any other things
    return  """
<h2>Login Page</h2>
<form method="POST">
  Usernsasme: <input type="text" name="username"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit" value="Login">
</form>
"""
 
 #welcome page
@app.route('/welcome')
def welcome():  
    if "user" in session:
        return f"""
    <h2>Welcome,{session["user"]}!</h2>
    <a href={url_for('logout')}>Logout</a>
    """          
    return redirect(url_for("login"))#login page pe dikhoge

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route('/homepage')
def home():
    return render_template("home.html")


@app.route('/submit',methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
    #  form me name="" likhan zaruri hai ,isse hi flask values lega
    # if username=="sagar" and password=="123":
    #     return render_template('welcome.html',name=username)  
    # else:
    #     return "Invalid credintals"    
    
    valid_users={
        'admin':'123',
        "sagar":"pass",
        "rajat":"raj",
        "rohit":"ready123"
    }            
    if username in valid_users and password==valid_users[username]:
        return render_template("Welcome.html",name=username)
    else :
        return "Invalid"                          
@app.route('/login')
def logins():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
    server = Server(app.wsgi_app)
    server.serve(debug=True)
    




























# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def home():
#     return ('Hello user! This is my first flask app')
# @app.route('/about')
# def about():
#     return ("This is about us page")
# @app.route("/contact")
# def contact():
#     return ("this is contact page")

# # print(app.url_map)

# if __name__ == "__main__":
#     app.run(debug=True)