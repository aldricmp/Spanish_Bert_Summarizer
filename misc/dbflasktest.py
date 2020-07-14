from datetime import datetime
import sqlalchemy as sal
from flask import Flask
from sqlalchemy import create_engine
import pandas as pd
import pyodbc

server = 'tcp:dbcontrol.mediasolutions.mx'
database = 'MSGBLOBAL'
username = 'scientive'
password = '''*&{a2$&[H#c@0"![>8I]+p5[n9/}38D%3(5<`R:hv4#+.]%2]>"m''=a,@6`'QU.@2]/Fm8hq7%1y)s|"`)bF7~2'?,<{yx\='''
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)



df = pd.DataFrame(pd.read_sql_query('SELECT TOP 10 * from K_NOTA',cnxn)
                )
print(str(df).encode('utf-8'))

app = Flask(__name__)

@app.route("/")
@app.route("/dbcontest")
def conect():
    return df.to_html()
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
