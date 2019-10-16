import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:\\Users\\wcarn\\Desktop\\GitHub\\leaflet-challenge\\Project_2_Syria\\project_app\\db\\data.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Syria_Data = Base.classes.Syria_Data


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Syria_Data).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


@app.route("/metadata/<sample>")
def data(sample):
    """Return the MetaData for a given sample."""
    sel = [
        Syria_Data.sample,
        Syria_Data.ETHNICITY,
        Syria_Data.GENDER,
        Syria_Data.AGE,
        Syria_Data.LOCATION,
        Syria_Data.BBTYPE,
        Syria_Data.WFREQ,
    ]

    results = db.session.query(*sel).filter(
        Syria_Data.sample == sample).all()

    # Create a dictionary entry for each row of metadata information
    data = {}
    for result in results:
        data["sample"] = result[0]
        data["ETHNICITY"] = result[1]
        data["GENDER"] = result[2]
        data["AGE"] = result[3]
        data["LOCATION"] = result[4]
        data["BBTYPE"] = result[5]
        data["WFREQ"] = result[6]

    print(data)
    return jsonify(data)


@app.route("/Syria_Data/<sample>")
def Syria_Data(sample):
    """Return `otu_ids`, `otu_labels`,and `sample_values`."""
    stmt = db.session.query(Syria_Data).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]

    # Sort by sample
    sample_data.sort_values(by=sample, ascending=False, inplace=True)

    # Format the data to send as json
    data = {
        "otu_ids": sample_data.otu_id.values.tolist(),
        "sample_values": sample_data[sample].values.tolist(),
        "otu_labels": sample_data.otu_label.tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()