from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    name = ''
    if request.method == "POST" and "fname" in request.form:
        name= request.form.get('fname')
    return render_template("index.html",name=name)

@app.route("/login")
def login():
	return render_template("login.html")

app.run(debug=True)
