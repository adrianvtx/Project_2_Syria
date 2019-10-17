# import os

# import pandas as pd
# import numpy as np

# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine

# from flask import Flask, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)


# #################################################
# # Database Setup
# #################################################

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:\\Users\\wcarn\\Desktop\\GitHub\\leaflet-challenge\\Project_2_Syria\\project_app\\db\\data.sqlite"
# db = SQLAlchemy(app)

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# Syria_Data = Base.classes.Syria_Data

# stmt = db.session.query(Syria_Data).statement
# df = pd.read_sql_query(stmt, db.session.bind)

