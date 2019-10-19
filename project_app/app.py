import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# #################################################
# # Database Setup
# #################################################
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/data.sqlite"
db = SQLAlchemy(app)
# engine = create_engine("sqlite:///C:\\Users\\wcarn\\Desktop\\GitHub\\leaflet-challenge\\Project_2_Syria\\project_app\\db\\data.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
# data1 = Base.classes.data1
data1 = Base.classes.data_drop

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route('/syria_CLUSTE.html')
def main():
    return render_template('syria_CLUSTE.html')


@app.route("/names")
def names():
    """Return a list of input names."""

    # Use Pandas to perform the sql query
    stmt = session.query(data1).statement
    df = pd.read_sql_query(stmt, db.session.bind)

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

    results = db.session.query(*sel).all()

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

    results1 = db.session.query(*sel).\
    group_by(data1.event_date).\
    order_by(data1.event_date).all()

    df3 = pd.DataFrame(results1, columns=['data_id', 'event_date', 'event_type', 'sub_event_type', 'actor1',
       'assoc_actor_1', 'actor2', 'assoc_actor_2', 'admin1', 'admin2',
       'admin3', 'location', 'latitude', 'longitude', 'notes', 'source',
       'fatalities'])

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

@app.route("/syria2")
def syria2():

    sel = [
        data1.admin1,
        data1.sub_event_type,
        func.sum(data1.fatalities),
    ]

    results2 = db.session.query(*sel).\
    group_by(data1.sub_event_type).\
    group_by(data1.admin1).\
    order_by(data1.admin1).all()

    df2 = pd.DataFrame(results2,
                       columns=['admin1', 'sub_event_type', 'fatalities'])

    event_data = df2[df2["fatalities"] > 1]
    new_event_data = pd.DataFrame(event_data)
    new_event_data.sort_values(by="fatalities", ascending=False, inplace=True)
    new_event_data.reset_index(drop = True)

    Idleb = new_event_data[new_event_data["admin1"] == "Idleb"]
    nIdleb = pd.DataFrame(Idleb)
    nIdleb.sort_values(by="fatalities", ascending=False, inplace=True)
    nIdleb.reset_index(drop = True)

    Hama = new_event_data[new_event_data["admin1"] == "Hama"]
    nHama = pd.DataFrame(Hama)
    nHama.sort_values(by="fatalities", ascending=False, inplace=True)
    nHama.reset_index(drop = True)

    DeirezZor = new_event_data[new_event_data["admin1"] == "Deir-ez-Zor"]
    nDeirezZor = pd.DataFrame(DeirezZor)
    nDeirezZor.sort_values(by="fatalities", ascending=False, inplace=True)
    nDeirezZor.reset_index(drop = True)

    AlHasakeh = new_event_data[new_event_data["admin1"] == "Al-Hasakeh"]
    nAlHasakeh = pd.DataFrame(AlHasakeh)
    nAlHasakeh.sort_values(by="fatalities", ascending=False, inplace=True)
    nAlHasakeh.reset_index(drop = True)

    ArRaqqa = new_event_data[new_event_data["admin1"] == "Ar-Raqqa"]
    nArRaqqa = pd.DataFrame(ArRaqqa)
    nArRaqqa.sort_values(by="fatalities", ascending=False, inplace=True)
    nArRaqqa.reset_index(drop = True)

    Dara = new_event_data[new_event_data["admin1"] == "Dar'a"]
    nDara = pd.DataFrame(Dara)
    nDara.sort_values(by="fatalities", ascending=False, inplace=True)
    nDara.reset_index(drop = True)

    AsSweida = new_event_data[new_event_data["admin1"] == "As-Sweida"]
    nAsSweida = pd.DataFrame(AsSweida)
    nAsSweida.sort_values(by="fatalities", ascending=False, inplace=True)
    nAsSweida.reset_index(drop = True)

    Homs = new_event_data[new_event_data["admin1"] == "Homs"]
    nHoms = pd.DataFrame(Homs)
    nHoms.sort_values(by="fatalities", ascending=False, inplace=True)
    nHoms.reset_index(drop = True)

    RuralDamascus = new_event_data[new_event_data["admin1"] == "Rural Damascus"]
    nRuralDamascus = pd.DataFrame(RuralDamascus)
    nRuralDamascus.sort_values(by="fatalities", ascending=False, inplace=True)
    nRuralDamascus.reset_index(drop = True)

    Aleppo = new_event_data[new_event_data["admin1"] == "Aleppo"]
    nAleppo = pd.DataFrame(Aleppo)
    nAleppo.sort_values(by="fatalities", ascending=False, inplace=True)
    nAleppo.reset_index(drop = True)

    Damascus = new_event_data[new_event_data["admin1"] == "Damascus"]
    nDamascus = pd.DataFrame(Damascus)
    nDamascus.sort_values(by="fatalities", ascending=False, inplace=True)
    nDamascus.reset_index(drop = True)

    Quneitra = new_event_data[new_event_data["admin1"] == "Quneitra"]
    nQuneitra = pd.DataFrame(Quneitra)
    nQuneitra.sort_values(by="fatalities", ascending=False, inplace=True)
    nQuneitra.reset_index(drop = True)

    Lattakia = new_event_data[new_event_data["admin1"] == "Lattakia"]
    nLattakia = pd.DataFrame(Lattakia)
    nLattakia.sort_values(by="fatalities", ascending=False, inplace=True)
    nLattakia.reset_index(drop = True)

    Tartous = new_event_data[new_event_data["admin1"] == "Tartous"]
    nTartous = pd.DataFrame(Tartous)
    nTartous.sort_values(by="fatalities", ascending=False, inplace=True)
    nTartous.reset_index(drop = True)



    # Format the data to send as json
    data5 = {
        "sub_event_type": new_event_data.sub_event_type.tolist(),
        "admin1": new_event_data.admin1.tolist(),
        "fatalities": new_event_data.fatalities.tolist(),
        "Idleb_sub_event_type": nIdleb.sub_event_type.tolist(),
        "Idleb_admin1": nIdleb.admin1.tolist(),
        "Idleb_fatalities": nIdleb.fatalities.tolist(),
        "Hama_sub_event_type": nHama.sub_event_type.tolist(),
        "Hama_admin1": nHama.admin1.tolist(),
        "Hama_fatalities": nHama.fatalities.tolist(),
        "DeirezZor_sub_event_type": nDeirezZor.sub_event_type.tolist(),
        "DeirezZor_admin1": nDeirezZor.admin1.tolist(),
        "DeirezZor_fatalities": nDeirezZor.fatalities.tolist(),
        "AlHasakeh_sub_event_type": nAlHasakeh.sub_event_type.tolist(),
        "AlHasakeh_admin1": nAlHasakeh.admin1.tolist(),
        "AlHasakeh_fatalities": nAlHasakeh.fatalities.tolist(),
        "ArRaqqa_sub_event_type": nArRaqqa.sub_event_type.tolist(),
        "ArRaqqa_admin1": nArRaqqa.admin1.tolist(),
        "ArRaqqa_fatalities": nArRaqqa.fatalities.tolist(),
        "Dara_sub_event_type": nDara.sub_event_type.tolist(),
        "Dara_admin1": nDara.admin1.tolist(),
        "Dara_fatalities": nDara.fatalities.tolist(),
        "AsSweida_sub_event_type": nAsSweida.sub_event_type.tolist(),
        "AsSweida_admin1": nAsSweida.admin1.tolist(),
        "AsSweida_fatalities": nAsSweida.fatalities.tolist(),
        "Homs_sub_event_type": nHoms.sub_event_type.tolist(),
        "Homs_admin1": nHoms.admin1.tolist(),
        "Homs_fatalities": nHoms.fatalities.tolist(),
        "RuralDamascus_sub_event_type": nRuralDamascus.sub_event_type.tolist(),
        "RuralDamascus_admin1": nRuralDamascus.admin1.tolist(),
        "RuralDamascus_fatalities": nRuralDamascus.fatalities.tolist(),
        "Aleppo_sub_event_type": nAleppo.sub_event_type.tolist(),
        "Aleppo_admin1": nAleppo.admin1.tolist(),
        "Aleppo_fatalities": nAleppo.fatalities.tolist(),
        "Damascus_sub_event_type": nDamascus.sub_event_type.tolist(),
        "Damascus_admin1": nDamascus.admin1.tolist(),
        "Damascus_fatalities": nDamascus.fatalities.tolist(),
        "Quneitra_sub_event_type": nQuneitra.sub_event_type.tolist(),
        "Quneitra_admin1": nQuneitra.admin1.tolist(),
        "Quneitra_fatalities": nQuneitra.fatalities.tolist(),
        "Lattakia_sub_event_type": nLattakia.sub_event_type.tolist(),
        "Lattakia_admin1": nLattakia.admin1.tolist(),
        "Lattakia_fatalities": nLattakia.fatalities.tolist(),
        "Tartous_sub_event_type": nTartous.sub_event_type.tolist(),
        "Tartous_admin1": nTartous.admin1.tolist(),
        "Tartous_fatalities": nTartous.fatalities.tolist()
    }

    return jsonify(data5)




if __name__ == "__main__":
    app.run()
