###############################################
# Models
# --------------------
# This file houses the definitions for all the database models via SQLAlchemy.
#
###############################################

from createapp import db,ma

# Database classes
class Patterns(db.Model):
    id = db.Column(db.Integer, primary_key=True) # authentication token
    name = db.Column(db.Text,nullable=False)
    intervals_per_second = db.Column(db.Integer, nullable=False)
    percent_power = db.Column(db.Integer, nullable=False)
    start_power = db.Column(db.Integer, nullable=False)
    max_power = db.Column(db.Integer, nullable=False)
    interval_power = db.Column(db.Integer, nullable=False)
    hold = db.Column(db.Integer,nullable=False)
    sequence = db.Column(db.Text,nullable=False)

    def __rep__(self):
        return f"Name: {self.first_name}, {self.last_name}"

# Database schemas
class PatternsSchema(ma.Schema):
    class Meta: # symptom number, symptom, symptom value
        fields = ('id', 'name', 'intervals_per_second', 'percent_power', 'start_power', 'max_power', 'interval_power', 'hold', 'sequence')

####################################
#
# Schema for Exporting
#
####################################
result_schema = PatternsSchema()
results_schema = PatternsSchema(many=True)