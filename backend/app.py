###############################################
# APP Routes
# --------------------
# This file houses all the routes that hit the API and returns datbaase queries 
#
###############################################
from imported.patterns import expanding_circle, rectangle, goacross, flow, strobe, circle, leaf1, leaf2, duelrectangle, infinity, zigzag, scan, scans, alarm1, alarm2, test1
from flask import Flask, jsonify, make_response, request
from classes.patternclass import Pattern
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from createapp import create_app,db
from dotenv import load_dotenv
from createapp import create_app, db, ma
from classes.zenbedclass import Zenbed
from threading import Thread

app = create_app()
zenbed = Zenbed()
threads = []

@app.route("/zenbed/start_pattern", methods=["POST"])
def zenbed_start_pattern():
    pattern = Pattern()
    pattern.sequence = request.get_json()['sequence']
    zenbed.pattern(pattern)
    return {
        "zenbed": "Zenbed started"
    }

@app.route("/zenbed/stop_pattern", methods=['POST'])
def zenbed_stop_pattern():
    zenbed.stop()
    return {
        "zenbed": "Zenbed stopped"
    }

@app.route("/zenbed/add_pattern", methods=["POST"])
def zenbed_add_pattern():
    id = len(db.engine.execute("SELECT * FROM patterns"))
    name = str(request.get_json()['name'])
    intervals_per_second = int(request.get_json()['intervals_per_second'])
    percent_power = float(request.get_json()['percent_power'])
    start_power = int(request.get_json()['start_power'])
    max_power = int(request.get_json()['max_power'])
    interval_power = int(request.get_json()['interval_power'])
    hold = int(request.get_json()['hold'])
    interval_power = str(request.get_json()['sequence'])

    db.engine.execute(f"""
        INSERT INTO pattern
        VALUES (
            {id},
            '{name}',
            {intervals_per_second},
            {percent_power}

        )
    
    """)

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)