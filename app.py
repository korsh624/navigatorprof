from flask import Flask, render_template, request
from db import DatabaseManager

app = Flask(__name__)
name='Имя'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/allinfo")
def allinfo():
    return render_template('allinfo.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/read_form", methods=['POST'])
def read_form():
    users = DatabaseManager('users.db')
    users.create_tables()
    data=request.form
    userEmail = data['userEmail']
    userNmae = data['name']
    userLastname = data['lastname']
    dictsend = (userEmail, userNmae, userLastname)
    users.query('''INSERT INTO Users VALUES (?,?,?)''',dictsend)
    return render_template('read_form.html')


@app.route("/addcolledg")
def addcolledg():
    colledg=DatabaseManager("colledg3.db")
    testinfo=("Юрьев-Польский индустриально-гуманитарный колледж",
              'Государственное бюджетное профессиональное образовательное учреждение Владимирской области "Юрьев-Польский индустриально-гуманитарный колледж"',
             '601800, г. Юрьев-Польский, пл. Советская, д. 5',
             '<a href="tel:+74924622660">8 (49246) 2-26-60</a>',
              '< a href="mailto:post@jpsped.elcom.ru" > post@jpsped.elcom.ru < / a >',
              'https://навигатор.владпрофобр.рф/assets/img/colledg/yupigk.jpg')
    colledg.query('''CREATE TABLE IF NOT EXISTS Colldgs(id int auto_increment primary key, title text, full_name text,addres text, tel text, email text, link_to_pict text)''')
    colledg.query('''INSERT INTO Colldgs VALUES(title, full_name, addres, tel, email, link_to_pict)''', testinfo)
    return render_template('read_form.html')



@app.route("/show")
def show():
    try:
        users = DatabaseManager('users.db')
        listuser=users.fetchall("""SELECT * FROM users""")
        print(listuser)
    except:
        listuser=[('В базе','нет','пользователей')]
    return render_template('show.html', listuser=listuser)


if __name__=="__main__":
    app.run(debug=True)


