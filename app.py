from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
	response = Response("", mimetype="text/html")
	response.headers["Link"] = '</static/style.css>; rel="stylesheet"'
	return response

@app.route("/button_text.svg")
def button_text():
	text = "On"
	response = Response(f"""<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="black" font-size="24">
    {text}
  </text>
</svg>""", mimetype="image/svg+xml")
	return response

if __name__ == "__main__":
	app.run(debug=True, port=5000)