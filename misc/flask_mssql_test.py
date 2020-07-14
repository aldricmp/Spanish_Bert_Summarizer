from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = '''mssql+pyodbc://scientive:*&{a2$&[H#c@0"![>8I]+p5[n9/}38D%3(5<`R:hv4#+.]%2]>"m''=a,@6`'QU.@2]/Fm8hq7%1y)s|"`)bF7~2'?,<{yx\=@dbcontrol.mediasolutions.mx/MSGBLOBAL?driver=ODBC Driver 17 for SQL Server'''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)






class K_NOTA(db.Model):
    __tablename__ = 'K_NOTA'
    id = db.Column('N_ID', db.Integer, primary_key=True)
    data = db.Column('N_NOTA', db.Unicode)

test = K_NOTA.query.limit(5).all()
for notas in test:
    print(str(notas.data).encode('utf-8'))

@app.route('/')
def hello():
    return f'Hello! How are you today?'
    f'''doin' fine and dandy!!!'''


@app.route('/notas')
def first_five():


    news_text=[]
    texts = K_NOTA.query.limit(1).all()
    for text in texts:
        news_text.append(text.data)

    return '\r\n'.join(news_text)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')