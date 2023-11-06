from flask import Flask, request, send_file, url_for, redirect, abort, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu/')
def menu_page():
    context = {
        "title": "Menu",
        "dishes": dishes
    }
    return render_template('menu.html', **context)


dishes = [
    {'pizza': 'Маргарита', 'price': 150},
    {'pizza': 'Гавайська', 'price': 200},
    {'pizza': 'Oderman', 'price': 250}
]

app.run(host='0.0.0.0', debug=True)