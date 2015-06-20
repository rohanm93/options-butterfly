import os
from flask import Flask, request, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.debug = True
# print app.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

class Options(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer, primary_key=True)
    dateTimeUpdated = db.Column('dateTimeUpdated', db.DateTime)
    stockName = db.Column('stockName', db.String)
    currentPrice = db.Column('currentPrice', db.String)
    strikePrice = db.Column('strikePrice', db.String)
    askPrice = db.Column('askPrice', db.String)
    askQty = db.Column('askQty', db.String)
    oi = db.Column('oi', db.String)
    # 'c' = call, 'p' = put
    cp = Column('callPut', String)


#all received texts
@app.route('/stock/<stock_name>')
def load_stock(stock_name):
    return render_template('main_page.html', option_list=Options.query.filter(Options.stockName==stock_name).order_by(Options.strikePrice.desc()).all(), stock_name_template=stock_name)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    # print port
    app.run(host='0.0.0.0', port=port)
