from flask import jsonify, Blueprint, request
import uuid


blueprint = Blueprint(
    'devices',
    __name__,
    url_prefix=''
)


@blueprint.route('/device', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def device1():

    """
        Permite obter os dados de um dispositivo específico [GET]
    """
    if request.method == 'GET':
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split()[1]
        device_id = request.args.get('device_id')
        response = {
            "ok": True,
            "device": {
                "id": "string",
                "name": "string",
                "fps": 0,
                "fps_percent": 0,
                "detection_threshold": 0,
                "resolution": "string",
                "resolution_percent": 0,
                "event_length": 0,
                "trigger_timer": 0,
                "capture_path": "string",
                "category": {
                "id": 0,
                "name": "string"
                },
                "frame_encoder": {
                "id": 0,
                "name": "string"
                },
                "trigger": {
                "id": 0,
                "name": "string",
                "type": "string"
                },
                "md_threshold": {
                "id": 0,
                "name": "string",
                "chunk_lines": 0,
                "chunk_percent": 0,
                "motion_detection_threshold": 0
                },
                "domain": {
                "id": 0,
                "name": "string",
                "created_at": "string",
                "updated_at": "string",
                "active": True
                },
                "services": [
                {
                    "id": 0,
                    "name": "string"
                }
                ]
            }
            }
        return jsonify(response), 200

    """
        Permite editar algumas informações de um dispositivo [PUT]
    """
    if request.method == 'PUT':
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split()[1]
        content = request.json
        """
            {
            "device_id": "string",
            "trigger_id": 0,
            "trigger_timer": 0,
            "name": "string",
            "capture_path": "string",
            "requester_id": "string"
            }
        """
        response = {
                "id": "string",
                "name": "string",
                "fps": 0,
                "fps_percent": 0,
                "detection_threshold": 0,
                "resolution": "string",
                "resolution_percent": 0,
                "event_length": 0,
                "trigger_timer": 0,
                "capture_path": "string",
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "frame_encoder": {
                    "id": 0,
                    "name": "string"
                },
                "trigger": {
                    "id": 0,
                    "name": "string",
                    "type": "string"
                },
                "md_threshold": {
                    "id": 0,
                    "name": "string",
                    "chunk_lines": 0,
                    "chunk_percent": 0,
                    "motion_detection_threshold": 0
                },
                "domain": {
                    "id": 0,
                    "name": "string",
                    "created_at": "string",
                    "updated_at": "string",
                    "active": True
                },
                "services": [
                    {
                    "id": 0,
                    "name": "string"
                    }
                ]
                }
        return jsonify(response), 200


    """
        Permite cadastrar um dispositivo [POST]
    """
    if request.method == 'POST':
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split()[1]
        response = {
            "name": "string",
            "fps": 0,
            "fps_percent": 0,
            "detection_threshold": 0,
            "resolution": "string",
            "resolution_percent": 0,
            "event_length": 0,
            "trigger_timer": 0,
            "capture_path": "string",
            "category_id": 0,
            "frame_encode_id": 0,
            "trigger_id": 0,
            "md_threshold_id": 0,
            "domain_id": 0,
            "services": [
                0
            ]
            }
        return jsonify(response), 201

    """
        Permite deletar um dispositivo [DELETE]
    """
    if request.method == 'DELETE':
        pass
        #TODO
        return jsonify(""), 200
 

@blueprint.route('/device/encoders')
def device2():    
    response = [
        {
            "id": 0,
            "name": "string"
        }
        ]
    return jsonify(response), 200

@blueprint.route('/device/thresholds')
def device3():    
    response = [
        {
            "id": 0,
            "name": "string",
            "chunk_lines": 0,
            "chunk_percent": 0,
            "motion_detection_threshold": 0
        }
        ]
    return jsonify(response), 200

@blueprint.route('/device/triggers')
def device4():    
    response = [
        {
            "id": 0,
            "name": "string",
            "type": "string"
        }
        ]
    return jsonify(response), 200

@blueprint.route('/device/categories')
def device5():    
    response = [
        {
            "id": 0,
            "name": "string"
        }
        ]
    return jsonify(response), 200

@blueprint.route('/device/services')
def device6():    
    response = [
        {
            "id": 0,
            "name": "string"
        }
        ]
    return jsonify(response), 200

@blueprint.route('/devices')
def device7():    
    """
        Permite a edição de um usuário [PUT]
    """
    if request.method == 'PUT':
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split()[1]
        response = [
            {
                "id": "string",
                "name": "string",
                "fps": 0,
                "fps_percent": 0,
                "detection_threshold": 0,
                "resolution": "string",
                "resolution_percent": 0,
                "event_length": 0,
                "trigger_timer": 0,
                "capture_path": "string",
                "category": {
                "id": 0,
                "name": "string"
                },
                "frame_encoder": {
                "id": 0,
                "name": "string"
                },
                "trigger": {
                "id": 0,
                "name": "string",
                "type": "string"
                },
                "md_threshold": {
                "id": 0,
                "name": "string",
                "chunk_lines": 0,
                "chunk_percent": 0,
                "motion_detection_threshold": 0
                },
                "domain": {
                "id": 0,
                "name": "string",
                "created_at": "string",
                "updated_at": "string",
                "active": True
                },
                "services": [
                {
                    "id": 0,
                    "name": "string"
                }
                ]
            }
            ]
        return jsonify(response), 200

