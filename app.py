from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return ('Hello user! This is my first flask app')
@app.route('/about')
def about():
    return ("This is about us page")
@app.route("/contact")
def contact():
    return ("this is contact page")

# print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)