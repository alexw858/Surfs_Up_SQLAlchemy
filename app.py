# use ins_flask_with_orm titanic exercise

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# adding connection to sqlite file into app.py (needs more code after engine)
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurements
Station = Base.classes.stations

session = Session(engine)



app = Flask(__name__)

@app.route("/")
def home():
    """List all available api routes."""
    print("Server received request for 'Home' page...")
    return("Welcome to Home Page<br>"
            "Available routes:<br>"
            "/api/v1.0/precipitation<br>"
            "/api/v1.0/stations<br>"
            "/api/v1.0/tobs<br>")



@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation' page...")
    # return "precipitation page"
    results = session.query(Measurement).all()

    all_measurement = []
    for measurement in results:
        measurement_dict = {}
        # measurement_dict["station"] = measurement.station
        measurement_dict["date"] = measurement.date
        measurement_dict["prcp"] = measurement.prcp
        # measurement_dict["tobs"] = measurement.tobs
        all_measurement.append(measurement_dict)

    return jsonify(all_measurement)

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'stations' page...")
    # return "stations page"
    results = session.query(Station.station).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs' page...")
    # return "tobs page"
    results = session.query(Measurement.tobs).all()
    a = [r[0] for r in results]
    #all_tobs = list(a.astype(int))
    return jsonify(a)

@app.route("/api/v1.0/<start>")
def start():
    start = input("Which date?")
    print("Server received request for date range page...")
    return "date range page"




if __name__ == "__main__":
    app.run(debug=True)