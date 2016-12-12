from flask import Flask, render_template, request
import yelp_access
import os
app = Flask(__name__)


@app.route("/")
def index():
	name = request.values.get('name')
	location = request.values.get('location')
	term = request.values.get('term')
	if location:
		businesses = yelp_access.get_businesses(location, term)
	else:
		businesses = None
	return render_template('index.html', businesses=businesses)


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)