# Начать разработку собственного pet-проекта: «Систем ведения вакансий», на Flask.
# Приготовить вёрстку, стили, js, и логику отправки вакансий в базу данных.
import datetime
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/api")
def api():
    return "jjj"
class Worker:

    def __init__(self,first_name, last_name, iin, gender, email,address, education, age, position, date_time, status):
        self.status = status
        self.date_time = date_time
        self.position = position
        self.age = age
        self.education = education
        self.address = address
        self.email = email
        self.gender = gender
        self.iin = iin
        self.last_name = last_name
        self.first_name=first_name


    def get_parametres(self):
        return self.first_name,self.last_name,self.iin,self.gender,self.email,self.address,self.education,self.age,self.position,self.date_time,self.status



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        first_name = form.get("firstName")
        last_name = form.get("lastName")
        iin = form.get("iin")
        gender = form.get("gender")
        email = form.get("email")
        address = form.get("address")
        education = form.get("education")
        age = form.get("age")
        position = form.get("position")
        date_time: datetime = datetime.datetime.now()
        status: bool = True
        print(type(first_name), first_name)
        print(type(last_name), last_name)
        print(type(iin), iin)
        print(type(gender), gender)
        print(type(email), email)
        print(type(address), address)
        print(type(education), education)
        print(type(age), age)
        print(type(position), position)

        worker=Worker(
            first_name=first_name,
            last_name=last_name,
            iin=iin,gender=gender,
            email=email,
            address=address,
            education=education,
            date_time=date_time,
            status=status,
            age=age,position=position)

        BaseOfData.create_worker(worker=worker)

        return render_template("register.html", result="It is cool!")


class BaseOfData:

    @staticmethod
    def create_db_file():
        query = """CREATE TABLE IF NOT EXISTS Worker
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         first_name TEXT,
         last_name TEXT,
         iin INTEGER UNIQUE NOT NULL,
         gender TEXT,
         email TEXT,
         address TEXT,
         education TEXT,
         age INTEGER,
         position TEXT,
         date_time TEXT default NOW(),
         status INTEGER
         """

        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query, ())
            connection.commit()


    @staticmethod
    def create_worker(worker:Worker):
        query="""
    INSERT INTO Worker(first_name, last_name, iin, gender, email, address, education, age, position, date_time, status)
    VALUES (             ?,           ?,       ?,    ?,     ?,       ?,       ?,       ?,     ?,       ?,          ?)
    """
        with sqlite3.connect("database.db") as connection:
            cursor=connection.cursor()
            cursor.execute(query, worker.get_parametres())


    @staticmethod
    def get_all_workers():
        query="""
        SELECT * from Worker
        """

        with sqlite3.connect("database.db") as connection:
            cursor=connection.cursor()
            cursor.execute(query, ())
            rows=cursor.fetchall()
            return rows








if __name__ == '__main__':
    app.run()
    # BaseOfData.create_db_file()
    # workers=BaseOfData.get_all_workers()
    # print(workers)
