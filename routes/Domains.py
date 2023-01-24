from flask import jsonify, Blueprint, request
import uuid


blueprint = Blueprint(
    'domains',
    __name__,
    url_prefix=''
)

@blueprint.route('/domain', methods = ['POST', 'DELETE', 'HEAD', 'GET'])
def domain1():
    """
        Permite cadastrar um novo domínio [POST]
    """
    """
        content Body JSON:
        body = {
            "name": "string"
            }
    """
    if request.method == 'POST':
        return jsonify(""), 200

    """
        Permite verificar se um domínio com determinado nome existe [HEAD]
    """
    if request.method == 'HEAD':
        name = request.args.get('name')
        response = {
            "exists": True
            }
        return jsonify(response), 200

    """
        Permite obter as informações de um domínio específico [GET]
    """
    if request.method == 'GET':
        id = request.args.get('id')
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split()[1]
        response = {
            "exists": True
            }
        return jsonify(""), 200

    
    """
        Permite apagar um domínio [DELETE]
    """
    if request.method == 'DELETE':
        pass
        #TODO
        return jsonify(""), 200

@blueprint.route('/domains')
def domain2():    
    """
        Permite listar todos os domínios cadastrados [GET]
    """
    response = [
        {
            "id": 0,
            "name": "string",
            "created_at": "string",
            "updated_at": "string",
            "active": True
        }
        ]
    return jsonify(response), 200