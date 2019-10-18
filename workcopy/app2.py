import os

import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# Database Setup
#################################################

engine = create_engine(
    "sqlite:///C:\\Users\\wcarn\\Desktop\\GitHub\\leaflet-challenge\\Project_2_Syria\\project_app\\db\\data.sqlite"
)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
data1 = Base.classes.data1
session = Session(engine)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
    """Return a list of input names."""

    # Use Pandas to perform the sql query
    stmt = session.query(data1).statement
    df = pd.read_sql_query(stmt, session.bind)

    # Return a list of the column names (input names)
    return jsonify(list(df.columns)[:17])


@app.route("/S_Data")
def S_Data():
    sel = [
        data1.data_id,
        data1.event_date,
        data1.event_type,
        data1.sub_event_type,
        data1.actor1,
        data1.assoc_actor_1,
        data1.actor2,
        data1.assoc_actor_2,
        data1.admin1,
        data1.admin2,
        data1.admin3,
        data1.location,
        data1.latitude,
        data1.longitude,
        data1.notes,
        data1.source,
        data1.fatalities,
    ]

    results = session.query(*sel).all()
    # .filter(data1.event_date == event_date)
    # #
    S_Data = {}
    for result in results:
        S_Data["data_id"] = result[0]
        S_Data["event_date"] = result[1]
        S_Data["event_type"] = result[2]
        S_Data["sub_event_type"] = result[3]
        S_Data["actor1"] = result[4]
        S_Data["assoc_actor_1"] = result[5]
        S_Data["actor2"] = result[6]
        S_Data["assoc_actor_2"] = result[7]
        S_Data["admin1"] = result[8]
        S_Data["admin2"] = result[9]
        S_Data["admin3"] = result[10]
        S_Data["location"] = result[11]
        S_Data["latitude"] = result[12]
        S_Data["longitude"] = result[13]
        S_Data["notes"] = result[14]
        S_Data["source"] = result[15]
        S_Data["fatalities"] = result[16]
    print(S_Data)
    return jsonify(S_Data)


@app.route("/syria")
def syria():

    sel = [
        data1.data_id,
        data1.event_date,
        data1.event_type,
        data1.sub_event_type,
        data1.actor1,
        data1.assoc_actor_1,
        data1.actor2,
        data1.assoc_actor_2,
        data1.admin1,
        data1.admin2,
        data1.admin3,
        data1.location,
        data1.latitude,
        data1.longitude,
        data1.notes,
        data1.source,
        func.sum(data1.fatalities),
    ]

    results1 = session.query(*sel).\
    group_by(data1.event_date).\
    order_by(data1.event_date).all()

    df3 = pd.DataFrame(results1,
                       columns=[
                           'data_id', 'event_date', 'event_type',
                           'sub_event_type', 'actor1', 'assoc_actor_1',
                           'actor2', 'assoc_actor_2', 'admin1', 'admin2',
                           'admin3', 'location', 'latitude', 'longitude',
                           'notes', 'source', 'fatalities'
                       ])

    stmt = session.query(data1).statement
    df = pd.read_sql_query(stmt, session.bind)

    data2 = df3

    # Format the data to send as json
    data = {
        "data_id": data2.data_id.tolist(),
        "event_date": data2.event_date.tolist(),
        "event_type": data2.event_type.tolist(),
        "sub_event_type": data2.sub_event_type.tolist(),
        "actor1": data2.actor1.tolist(),
        "assoc_actor_1": data2.assoc_actor_1.tolist(),
        "actor2": data2.actor2.tolist(),
        "assoc_actor_2": data2.assoc_actor_2.tolist(),
        "admin1": data2.admin1.tolist(),
        "admin2": data2.admin2.tolist(),
        "admin3": data2.admin3.tolist(),
        "location": data2.location.tolist(),
        "latitude": data2.latitude.tolist(),
        "longitude": data2.longitude.tolist(),
        "notes": data2.notes.tolist(),
        "source": data2.source.tolist(),
        "fatalities": data2.fatalities.tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()