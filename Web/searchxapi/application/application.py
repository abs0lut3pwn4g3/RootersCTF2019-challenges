from flask import Flask, make_response, request, redirect, render_template, flash
import requests, re, json, os
from bs4 import BeautifulSoup

app = Flask(__name__)

app.secret_key = "fuk9dfuk511asddasd2130fukbddbee2fuk"

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		regex = re.compile(
        r'^(?:http)s?://' # http:// or https://
        r'(?:127.0.0.1)' #domain...
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
		url = request.form.get('url')
		search_term = request.form.get('search_term')
		if re.match(regex, url):
			r=requests.get(url, headers={"X-Flag":"rooters{Listen_to_this_bit.do/fccPs}ctf"})
			soup = BeautifulSoup(r.content, "html.parser")
			parsed_data = soup.findAll(search_term)
			if parsed_data:
				return render_template('index.html', data=parsed_data)
			else:
				flash('No results', 'info')
				return render_template('index.html')
		else:
			flash('Invalid URL!', 'danger')
			return render_template('index.html')
	else:
		return render_template('index.html')


@app.route('/redirect', methods=['GET'])
def redirect_fun():
    uri = request.args.get('uri')
    resp = make_response(redirect(uri))
    return resp

@app.route('/books', methods=['GET'])
def books():
	url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=%20fpTKnRGxYziX8AKYG9evaFLb7iKU569y&%20age-group=15"
	data = json.dumps(requests.get(url).json())
	resp = make_response(data)
	resp.headers['Content-Type'] = 'application/json'
	return resp

if __name__ == '__main__':
    app.run(debug=False)
