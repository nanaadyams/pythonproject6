# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 06:38:58 2021

@author: HP
"""
import dash
import dash_daq as daq
import dash_html_components as html
import pymysql
import mysql.connector

#DATABASE SERVER
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="motordaq"
)

cursor = db.cursor()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Knob(
        id='my-knob',
        size=140,
          min=0,
          max=5,
          value=0
    ),
    html.Div(id='knob-output')
])

@app.callback(
    dash.dependencies.Output('knob-output', 'children'),
    [dash.dependencies.Input('my-knob', 'value')])


def update_output(value):
    sql = "INSERT INTO tb_knob (voltase) VALUES (" + str(value) + ")"
    cursor.execute(sql)
    db.commit()
    print(value)
    return 'The knob value is {}.'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
