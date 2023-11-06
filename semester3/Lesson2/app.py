from flask import Flask, render_template
import random as r

'''Відображення списку продуктів з розгортанням інформації:
 Створіть сторінку для відображення списку продуктів разом з додатковою інформацією про кожен продукт.
 Використовуйте Jinja для ітерації через список продуктів і відображення інформації,
 такої як ім'я продукту, ціна та опис. Використовуйте конструкцію {% for %} для цього. Наприклад:'''





app = Flask(__name__, template_folder='templates', static_folder='static')

hero = ['Warrior', 'Mag', 'Wizard', 'Archer', 'Orc']


max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Yaroslav", "score": 100},
    {"name": "Egor", "score": 59},
    {"name": "Nikita", "score": 93},
    {"name": "Illia", "score": 78},
    {"name": 'Kyrylo', "score": 99},
    {"name": "Alex", "score": 11},
    {"name": "Mia", "score": 82},
    {"name": "Polina", "score": 69}
]

@app.route("/")
def index():
    return render_template('base.html', title='All Work')

@app.route("/results/")
def results():
    context = {
        'title':'Results',
        'students': students,
        'test_name': test_name,
        'max_score': max_score
    }
    return render_template('results.html', **context)


posts = [
    {'status': 'В обробці'},
    {'status': 'Відправлено'}
]

products = [
    {'name': 'Cucumber', 'price': 100, 'description': 'Green vegetable'},
    {'name': 'Tomato', 'price': 150, 'description': 'Red vegetable'},
    {'name': 'Milk', 'price': 75, 'description': 'White drink'},
    {'name': 'Banana', 'price': 80, 'description': 'Yellow fruit'}
]

bam = {
    'posts': products
}

@app.route("/price/")
def price():
    return render_template('price.html', **bam)

context = {
    "post": posts
}
@app.route("/order_status/")
def order():
    return render_template('order.html', **context)



app.run(host="0.0.0.0", port=8080, debug=True)