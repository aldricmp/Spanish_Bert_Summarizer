from datetime import datetime
import sqlalchemy as sal
from flask import Flask
from sqlalchemy import create_engine
import pandas as pd
import pyodbc
app = Flask(__name__)

server = 'tcp:dbcontrol.mediasolutions.mx'
database = 'MSGBLOBAL'
username = 'scientive'
password = '''*&{a2$&[H#c@0"![>8I]+p5[n9/}38D%3(5<`R:hv4#+.]%2]>"m''=a,@6`'QU.@2]/Fm8hq7%1y)s|"`)bF7~2'?,<{yx\='''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()
cursor.execute("SELECT TOP 5 * from K_NOTA")
s = "<table style='border:1px solid red'>"
for row in cursor:
    s = s + "<tr>"
for x in row:
    s = s + "<td>" + str(x) + "</td>"
s = s + "</tr>"

print(s.encode('utf-8'))   #AQUÍ ME MARCABA EL ERROR "UnicodeEncodeError: 'ascii' codec can't encode character '\xe1' in position 163: ordinal not in range(128)"


app = Flask(__name__)

@app.route("/")
def conect():
    return s
if __name__ == "__main__":
    app.run(debug=True)