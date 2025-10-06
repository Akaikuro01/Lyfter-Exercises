def check_auth(token, rights_scope, ioc_container):
    # This method will return a number between 0 to 2 depending on the "status" of the checks
    # 0 = All good, token's good, user is authorized
    # 1 = Token is invalid or None
    # 2 = User not authorized
    status = 0
    if(token is not None):
        token = token.replace("Bearer ","")
        decoded = ioc_container.jwt_manager.decode(token)
        if not decoded:
            return 1
        
        role = decoded['role']

        if role not in rights_scope:
            return 2
        
        return 0
    else:
        return 1
    
def get_logged_in_user_id(token, ioc_container):
    token = token.replace("Bearer ","")
    decoded = ioc_container.jwt_manager.decode(token)
    user_id = decoded['id']

    return user_id
