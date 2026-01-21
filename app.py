from flask import Flask,request,redirect,url_for,session,Response
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