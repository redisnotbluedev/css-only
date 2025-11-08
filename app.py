from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
	response = Response("", mimetype="text/html")
	response.headers["Link"] = '</static/style.css>; rel="stylesheet"'
	return response

if __name__ == "__main__":
	app.run(debug=True, port=5000)