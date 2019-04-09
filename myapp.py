from flask import Flask, render_template, request
app= Flask(__name__)
@app.route('/')
def hello():
	return render_template("form.html")
@app.route('/fb')
def fb():
	return "Welcome to facebook"
@app.route('/form', methods=["post"])
def form():
	name= request.form["name"]
	enroll= request.form["eno"]
	email= request.form["email"]
	return render_template("normal.html",name=name,eno=enroll,email=email)
if __name__ == '__main__':
	app.run(port=5000, debug=True)

