# -*- coding: utf-8 -*-
#
# FLASK API TO DISPLAY GEOJSON
# Alexander Danielson w/ assitance of Luke Zaruba
# GIS 5572: ArcGIS II - Lab 3
# 2023-04-13
#

from flask import Flask, request
from database import Database
import os

# Set up DB Connection
db = Database.initialize_from_env()

# Set Vars for Formatting
start_str = """{"type": "FeatureCollection", "features": """
end_str = "}"

# Set Up Flask App
app = Flask(__name__)

# Define Routes
@app.route("/")
def home():
    return "Alexander Danielson Lab 3"


@app.route("/temperature_point_accuracy")
def weather_point():
    # Make Connection
    db.connect()

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(aggMthWX_22023_point_diff)) FROM aggMthWX_22023_point_diff;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


@app.route("/temperature_h3")
def weather_h3():
    # Make Connection
    db.connect()

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(aggMthWX_22023_h3_6)) FROM aggMthWX_22023_h3_6;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


@app.route("/elevation_point_accuracy")
def elevation_point():
    # Make Connection
    db.connect()

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(RasterToPointDEM_point_diff)) FROM RasterToPointDEM_point_diff;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


@app.route("/elevation_h3")
def elevation_h3():
    # Make Connection
    db.connect()

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(RasterToPointDEM_h3_6)) FROM RasterToPointDEM_h3_6;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))