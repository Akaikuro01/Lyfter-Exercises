from flask import Blueprint, request, jsonify, Response, current_app

bp = Blueprint("auth", __name__)

@bp.post('/register',)
def register():
    ioc_container = current_app.ioc
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None or data.get('role_id') == None or data.get("email") == None or data.get('full_name') == None):
        return Response(status=400)
    else:
        result = ioc_container.users_repository.insert_user(data.get('full_name'), data.get('email'), data.get('username'), data.get('password'), data.get('role_id'))
        print(result)
        user_id = result[0]
        role = data.get('role_id')

        token = ioc_container.jwt_manager.encode({'id':user_id, 'role': role})
        
        return jsonify(token=token)

@bp.post('/login')
def login():
    ioc_container = current_app.ioc
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = ioc_container.users_repository.get_user(data.get('username'), data.get('password'))

        if(result == None):
            return Response(status=403)
        else:
            user_id = result[0]
            role = result[3]
            token = ioc_container.jwt_manager.encode({'id':user_id, 'role': role})
        
            return jsonify(token=token)