from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


def create_table():
    conn = sqlite3.connect('vacancies.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vacancies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    create_table()
    conn = sqlite3.connect('vacancies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vacancies')
    vacancies = cursor.fetchall()
    conn.close()
    return render_template('index.html', vacancies=vacancies)


@app.route('/add_vacancy', methods=['POST'])
def add_vacancy():
    title = request.form.get('title')
    description = request.form.get('description')

    if title and description:
        conn = sqlite3.connect('vacancies.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO vacancies (title, description) VALUES (?, ?)', (title, description))
        conn.commit()
        conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <title>Система ведения вакансий</title>
</head>
<body>
    <h1>Список вакансий</h1>
    <ul id="vacancies-list">
        {% for vacancy in vacancies %}
            <li>{{ vacancy[1] }} - {{ vacancy[2] }}</li>
        {% endfor %}
    </ul>

    <h2>Добавить вакансию</h2>
    <form id="add-vacancy-form">
        <label for="title">Название:</label>
        <input type="text" name="title" id="title" required>
        <br>
        <label for="description">Описание:</label>
        <textarea name="description" id="description" required></textarea>
        <br>
        <button type="submit">Добавить</button>
    </form>

    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>



body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
}

h1 {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    background-color: #fff;
    border: 1px solid #ccc;
    margin: 5px 0;
    padding: 10px;
}

h2 {
    margin-top: 20px;
}

form {
    margin-top: 10px;
}

label, input, textarea, button {
    display: block;
    margin-bottom: 10px;
}
