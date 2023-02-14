###############################################
# APP Routes
# --------------------
# This file houses all the routes that hit the API and returns datbaase queries 
#
###############################################
from imported.patterns import expanding_circle, rectangle, goacross, flow, strobe, circle, leaf1, leaf2, duelrectangle, infinity, zigzag, scan, scans, alarm1, alarm2, test1
from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from createapp import create_app,db
from dotenv import load_dotenv
from createapp import create_app, db, ma
from classes.zenbedclass import Zenbed
from classes.patternclass import Pattern
from threading import Thread

app = create_app()
zenbed = Zenbed()
threads = []

@app.route("/zenbed/start_pattern", methods=["POST"])
def zenbed_start_pattern():


    requested_pattern = Pattern(
        name=request.get_json()['name'],
        intervals_per_second=request.get_json()['intervals_per_second'],
        percent_power=request.get_json()['percent_power'],
        start_power=request.get_json()['start_power'],
        max_power=request.get_json()['max_power'],
        interval_power=request.get_json()['interval_power'],
        hold=request.get_json()['hold'],
        reverse=request.get_json()['reverse'],
        sequence=request.get_json()['sequence']
    )

    zenbed.pattern(requested_pattern)
    return {
        "zenbed": "Zenbed started"
    }

@app.route("/zenbed/stop_pattern", methods=['POST'])
def zenbed_stop_pattern():
    zenbed.stop()
    return {
        "zenbed": "Zenbed stopped"
    }

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)