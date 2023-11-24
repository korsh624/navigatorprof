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


@app.route("/test")
def test():
    return render_template('test.html')

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


@app.route("/formcolledg", methods=['POST'])
def formcolledg():
    colledg = DatabaseManager("colledgs.db")
    colledg.query("""CREATE TABLE IF NOT EXISTS Colldgs(
	"id"	INTEGER UNIQUE,
	"title"	text,
	"full_name"	text,
	"addres"	text,
	"tel"	text,
	"email"	text,
	"link_to_pict"	text,
	PRIMARY KEY("id" AUTOINCREMENT)
);""")
    colledgs=request.form
    title=colledgs['title']
    full_name = colledgs['full_name']
    addres = colledgs['addres']
    tel = colledgs['tel']
    email = colledgs['userEmail']
    link_to_pict = colledgs['link_to_pict']
    info=(title,full_name,addres,tel,email,link_to_pict)
    colledg.query(
        '''INSERT INTO Colldgs(title, full_name, addres, tel, email, link_to_pict) VALUES (?, ?, ?, ?, ?, ?)''', info)
    return render_template('read_form.html')

@app.route("/additem")
def additem():
    return render_template('additem.html')



@app.route("/show")
def show():
    try:
        users = DatabaseManager('users.db')
        listuser=users.fetchall("""SELECT * FROM users""")
        print(listuser)
    except:
        listuser=[('В базе','нет','пользователей')]
    return render_template('show.html', listuser=listuser)



@app.route("/showcolledg")
def showcolledg():
    try:
        colledg = DatabaseManager('colledgs.db')
        listuser=colledg.fetchall("""SELECT * FROM Colldgs""")
        print(listuser)
    except:
        listuser=[('В базе','нет','пользователей')]
    return render_template('showcolledg.html', listuser=listuser)

id=7
alias="/getpage" +str(id)

@app.route("/getpage<page_id>")
def getpage(page_id):
    try:
        colledg = DatabaseManager('colledgs.db')
        listuser = colledg.fetchall(f"SELECT * FROM Colldgs WHERE id=={page_id}")
        print(listuser)
    except:
        return render_template("error.html")
    return render_template('test.html', listuser=listuser)



if __name__=="__main__":
    app.run(debug=True)



