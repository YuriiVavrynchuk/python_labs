from os import abort

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:kswtq1337@localhost:3306/iot-test-db'

ma = Marshmallow(app)
db = SQLAlchemy(app)


class MedicalProfession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(20))
    duration = db.Column(db.Integer)
    avgSalary = db.Column(db.String(10))
    maxAge = db.Column(db.Integer)

    def __init__(self, department, duration, avgSalary, maxAge):
        self.department = department
        self.duration = duration
        self.avgSalary = avgSalary
        self.maxAge = maxAge


class MedicalProfessionScheme(ma.Schema):
    class Meta:
        fields = ('department', 'duration', 'avgSalary', 'maxAge')


medical_profession_scheme = MedicalProfessionScheme()
medical_professions_scheme = MedicalProfessionScheme(many=True)


@app.route('/professions', methods=['GET'])
def get_all_professions():
    all_professions = MedicalProfession.query.all()
    result = medical_professions_scheme.dump(all_professions)
    return jsonify(result)


@app.route('/professions/<id>', methods=['GET'])
def get_profession(id):
    profession = MedicalProfession.query.get(id)
    if not profession:
        abort(404)
    return medical_profession_scheme.jsonify(profession)


@app.route('/professions', methods=['POST'])
def add_profession():
    department = request.json['department']
    duration = request.json['duration']
    avgSalary = request.json['avgSalary']
    maxAge = request.json['maxAge']

    new_profession = MedicalProfession(department, duration, avgSalary, maxAge)

    db.session.add(new_profession)
    db.session.commit()

    return medical_profession_scheme.jsonify(new_profession)


@app.route('/professions/<id>', methods=['PUT'])
def update_profession(id):
    profession = MedicalProfession.query.get(id)
    if not profession:
        abort(404)
    profession.department = request.json["department"]
    profession.duration = request.json["duration"]
    profession.avgSalary = request.json["avgSalary"]
    profession.maxAge = request.json["maxAge"]
    db.session.commit()

    return medical_profession_scheme.jsonify(profession)


@app.route('/professions/<id>', methods=['DELETE'])
def delete_profession(id):
    profession = MedicalProfession.query.get(id)
    if not profession:
        abort(404)
    db.session.delete(profession)
    db.session.commit()

    return medical_profession_scheme.jsonify(profession)


if __name__ == '__main__':
    app.run(debug=True)

