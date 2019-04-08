from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def hello():
	return "Hello I am Running on localhost and 5000 point"
if __name__ == '__main__':
	app.run(port=8000)
