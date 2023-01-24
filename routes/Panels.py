from flask import jsonify, Blueprint, request
import uuid


blueprint = Blueprint(
    'panels',
    __name__,
    url_prefix=''
)

@blueprint.route('/panel', methods = ['POST', 'DELETE', 'GET'])
def panel1():
    """
        Permite obter as informações básicas de um painel [GET]
    """
    if request.method == 'GET':
        id = request.args.get('id')
        response = {
            "id": "string",
            "name": "string",
            "domain_name": "string",
            "created_at": "string"
            }
        return jsonify(response), 200

    """
        Permite cadastrar um painel [POST]
    """
    if request.method == 'POST':
        """
        content Body JSON:
        body = {
            "name": "string"
            }
        """
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split()[1]
        response = {
            "id": "string",
            "name": "string",
            "domain_name": "string",
            "created_at": "string"
            }
        return jsonify(response), 200


    """
        Permite deletar um painel [DELETE]
    """
    if request.method == 'DELETE':
        pass
        #TODO
        return jsonify(""), 200

@blueprint.route('/panel/edit', methods = ['PUT'])
def panel2():
    """
        Permite editar um painel [PUT]
    """
    """
        content Body JSON:
        body = {
            "id": "string",
            "name": "string"
            }
    """
    return jsonify(""), 200

@blueprint.route('/panels')
def panel3():    
    """
        Permite listar todos os painéis cadastrados [GET]
    """
    headers = request.headers
    bearer = headers.get('Authorization')    # Bearer YourTokenHere
    token = bearer.split()[1]
    response = [
        {
            "id": "string",
            "name": "string",
            "domain_name": "string",
            "created_at": "string"
        }
        ]
    return jsonify(response), 200
