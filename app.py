from flask import Flask,render_template
from livereload import server
app=Flask(__name__)

@app.route('/')
def student_profile():
    return render_template("profile1.html",name="Arun",is_topper=True,subjects=["Maths","hindi","english"])
if __name__ == "__main__":
    app.run(debug=True)
    server = Server(app.wsgi_app)
    server.serve(debug=True)
    