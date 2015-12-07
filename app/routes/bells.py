from app import app, db
from app.models import bell
from flask import abort, jsonify, request
import datetime
import json

@app.route('/bell/lastest', methods = ['GET'])
def get_lastest_bell():
    entities = bell.Bell.query.order_by(bell.Bell.id.desc()).limit(1).all()
    if(len(entities) > 0):
        return jsonify(entities[0].to_dict())
    else:
        return jsonify("")

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
        create_time =  datetime.datetime.now()
        , update_time =  datetime.datetime.now()
        , request_time =  datetime.datetime.now()
        , is_played = False
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
        update_time = datetime.datetime.now(),
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
