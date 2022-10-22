from flask import Flask , render_template , request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database


app = Flask(__name__,template_folder='templates' )


db = SQLAlchemy(app)
DB_USER ='ubu'
DB_PASSWORD = '11'
DB_NAME = 'bobdb'
DB_ECHO = True 


app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200),nullable = False)
    price = db.Column(db.Integer, nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.String(250),nullable = True)

    def __repr__(self):
        return self.name

def __init__(self,name,price,amount,comment):
    self.name = name
    self.price = price
    self.amount = amount
    self.comment = comment

if not database_exists(db.engine.url):
    create_database(db.engine.url)
db.init_app(app)
db.create_all()

students = Item.query.filter_by().all()
print(students)

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', data=items)


@app.route('/about',methods=['POST','GET'])
def about():
    if request.method == 'POST':
        nam = request.form['name']
        pric = request.form['price']
        amoun = request.form['amount']
        commen = request.form['comment']

        item = Item(name=nam,price=pric,amount=amoun,comment=commen)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Ошибка'
    return render_template('about.html')


    

if __name__ == '__main__':
   app.run(debug = True)




# app.run(host='127.0.0.1', port='5000')







# @app.route('/name',methods=['POST','GET'])
# def name():
#     if request.method == 'POST': 
#         name = request.form['Name']
#         second_name = request.form['Second_name']
#         third_name = request.form['Third_name']
#         age =  request.form['Age']

#         print(name,second_name,third_name,age, sep=" ")
#         # return redirect(url_for('/name'))
#         with open('aaa.csv', 'w')as file:
#             writer = csv.writer(file)
#             writer.writerow([name,second_name,third_name,age])
#     return render_template('1.html')



# @app.route('/')
# def date():
#     return render_template("1.html")

# DATABASE = 'Untitled'
# def getdb():
#     db = getattr(g,'_database',None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db


# app = Flask(__name__,template_folder='templates')



# class Student(db.Model):
#    id = db.Column('student_id', db.Integer, primary_key=True)
#    name = db.Column(db.String(100))
#    city = db.Column(db.String(50))
#    address = db.Column(db.String(200))
#    pin = db.Column(db.String(10))

# def __init__(self, name, city, address, pin):
#        self.name = name
#        self.city = city
#        self.address = address
#        self.pin = pin

# if not database_exists(db.engine.url):
#   create_database(db.engine.url)
# db.init_app(app)
# db.create_all()

# students = Student.query.filter_by().all()
# print(students)

# @app.route('/myword/<word>')
# def myword(word):
    
#     if len(word) % 2 == 0:
#         word = word[::2]

#     return render_template('5.html',word = word)