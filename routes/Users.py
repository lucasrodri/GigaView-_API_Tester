from flask import jsonify, Blueprint, request

blueprint = Blueprint(
    'users',
    __name__,
    url_prefix=''
)

@blueprint.route('/user')
def user1():    
    """
        Cadastro de Usuário [POST]
    """
    if request.method == 'GET':
        query = {'test1': 'test2'}
        return jsonify(query), 500
    """
        Permite deletar um usuário [DELETE]
    """
    if request.method == 'DELETE':
        pass
    """
        Busca de usuário [HEAD]
    """
    if request.method == 'HEAD':
        pass

@blueprint.route('/login')
def user2():    
    return "Teste usuário 2"

@blueprint.route('/user/edit')
def user3():    
    return "Teste usuário edit"


@blueprint.route('/users')
def user4():    
    return "Teste usuário users"