from flask import Flask, Response
import random, time

app = Flask(__name__)

@app.route("/")
def index():
	response = Response("", mimetype="text/html")
	response.headers["Link"] = '</static/style.css>; rel="stylesheet"'
	return response

@app.route("/button_text.svg")
def button_text():
	response = Response(f"""<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
	<text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="black" font-size="24">
		{random.randint(1, 1000)}
	</text>
</svg>""", mimetype="image/svg+xml")
	response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
	response.headers["Pragma"] = "no-cache"
	response.headers["Expires"] = "0"
	response.headers["ETag"] = f'"{time.time()}"'
	return response

if __name__ == "__main__":
	app.run(debug=True, port=5000)