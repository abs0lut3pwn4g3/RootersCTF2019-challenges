from flask import Flask, render_template_string, request

app = Flask(__name__)


app.secret_key = "fuk9dfuk5680fukbddbee2fuk"


@app.route('/', methods=['GET'])
def index():
	name = 'Flask' + ' & ' + request.args.get("name", default="Flask")
	template = """
	{% extends "layout.html" %}
	{% block content %}
	<div class="content-section">
	I &hearts; """ + name + """
 	</div>
	{% endblock %}""" 
	return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=False)
