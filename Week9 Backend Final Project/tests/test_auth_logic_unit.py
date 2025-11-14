from auth_logic import check_auth, get_logged_in_user_id

class DummyIOC:
    class JM:
        def decode(self, token):
            if token == "admin":
                return {"id":1, "role":1}
            if token == "user":
                return {"id":2, "role":2}
            return None
    jwt_manager = JM()

def test_check_auth_ok_admin():
    status = check_auth("Bearer admin", [1,2], DummyIOC())
    assert status == 0

def test_check_auth_unauthorized_role():
    status = check_auth("Bearer user", [1], DummyIOC())
    assert status == 2

def test_check_auth_invalid_token():
    status = check_auth("Bearer nope", [1,2], DummyIOC())
    assert status == 1

def test_get_logged_in_user_id():
    user_id = get_logged_in_user_id("Bearer admin", DummyIOC())
    assert user_id == 1
