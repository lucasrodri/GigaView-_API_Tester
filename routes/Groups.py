from flask import jsonify, Blueprint, request
import uuid


blueprint = Blueprint(
    'groups',
    __name__,
    url_prefix=''
)

@blueprint.route('/group', methods = ['POST', 'DELETE', 'PUT'])
def group1():
    """
        Permite editar o nome de um grupo [PUT]
    """
    """
        content Body JSON:
        body = {
            "name": "string"
            }
    """
    if request.method == 'PUT':
        response = {
            "group_id": "string",
            "name": "string",
            "created_at": "string",
            "domain": {
                "id": 0,
                "name": "string",
                "created_at": "string",
                "updated_at": "string",
                "active": True
            }
            }
        return jsonify(response), 200

    """
        Permite realizar o cadastro de um grupo [POST]
    """
    if request.method == 'POST':
        """
        content Body JSON:
        body = {
            "name": "string"
            }
        """
        response = {
            "group_id": "string",
            "name": "string",
            "created_at": "string",
            "domain": {
                "id": 0,
                "name": "string",
                "created_at": "string",
                "updated_at": "string",
                "active": True
            }
            }
        return jsonify(response), 200


    """
        Permite apagar um grupo [DELETE]
    """
    if request.method == 'DELETE':
        pass
        #TODO
        return jsonify(""), 200