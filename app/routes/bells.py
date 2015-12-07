from app import app, db
from app.models import bell
from flask import abort, jsonify, request
import datetime
import json

@app.route('/bell/bells', methods = ['GET'])
def get_all_bells():
    entities = bell.Bell.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/bell/bells/<int:id>', methods = ['GET'])
def get_bell(id):
    entity = bell.Bell.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/bell/bells', methods = ['POST'])
def create_bell():
    entity = bell.Bell(
        create_time = datetime.datetime.strptime(request.json['create_time'], "%Y-%m-%d").date()
        , update_time = datetime.datetime.strptime(request.json['update_time'], "%Y-%m-%d").date()
        , request_time = datetime.datetime.strptime(request.json['request_time'], "%Y-%m-%d").date()
        , is_played = request.json['is_played']
        , repeat_times = request.json['repeat_times']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/bell/bells/<int:id>', methods = ['PUT'])
def update_bell(id):
    entity = bell.Bell.query.get(id)
    if not entity:
        abort(404)
    entity = bell.Bell(
        create_time = datetime.datetime.strptime(request.json['create_time'], "%Y-%m-%d").date(),
        update_time = datetime.datetime.strptime(request.json['update_time'], "%Y-%m-%d").date(),
        request_time = datetime.datetime.strptime(request.json['request_time'], "%Y-%m-%d").date(),
        is_played = request.json['is_played'],
        repeat_times = request.json['repeat_times'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/bell/bells/<int:id>', methods = ['DELETE'])
def delete_bell(id):
    entity = bell.Bell.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
