from flask import jsonify, Blueprint, request
import uuid


blueprint = Blueprint(
    'users',
    __name__,
    url_prefix=''
)


@blueprint.route('/user', methods = ['POST', 'DELETE', 'HEAD'])
def user1():
    """
    content Body JSON:
    body = {
        "username": "string",
        "email": "string",
        "name": "string",
        "password": "string",
        "domain_name": "string"
        }
    """
    content = request.json

    """
        Cadastro de Usuário [POST]
    """
    if request.method == 'POST':
        response = {"user_id":  str(uuid.uuid4())}
        return jsonify(response), 201
        
    """
        Permite deletar um usuário [DELETE]
    """
    if request.method == 'DELETE':
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split()[1]
        response = {"deleted": True}
        return jsonify(response), 200

    """
        Busca de usuário [HEAD]
    """
    if request.method == 'HEAD':
        username = request.args.get('username')
        if username == "Teste":
            return "", 200
        else:
            return "", 404

@blueprint.route('/login', methods = ['POST'])
def user2():    
    """
    content Body JSON:
    body = {
        "username": "string",
        "password": "string",
        "domain_name": "string"
        }
    """
    content = request.json

    """
        Login de usuário [POST]
    """
    if request.method == 'POST':
        response = {
            "uuid": str(uuid.uuid4()),
            "email": "a@a.com",
            "token": "Bearer a77d338964b991bc8fbc0a090fbe0793796486d5"
            }
        return jsonify(response), 200

@blueprint.route('/user/edit', methods = ['PUT'])
def user3():    
    """
        Permite a edição de um usuário [PUT]
    """
    if request.method == 'PUT':
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split()[1]
        response = {"new_password": "string"}
        return jsonify(response), 200


@blueprint.route('/users')
def user4():    
    headers = request.headers
    bearer = headers.get('Authorization')    # Bearer YourTokenHere
    token = bearer.split()[1]
    response = [
        {
            "username": "lucasrc",
            "email": "a@a.com",
            "name": "Lucas Costa",
            "password": "123Mudar",
            "domain_name": "test_domain"
        }
        ]
    return jsonify(response), 200
