def test_register_success(client):
    payload = {"full_name":"Steve","email":"steve@x.com","username":"steve2","password":"secret","role_id":1}
    res = client.post("/register", json=payload)
    assert res.status_code == 200
    assert "token" in res.get_json()

def test_register_missing_fields(client):
    res = client.post("/register", json={"username":"x"})
    assert res.status_code == 400

def test_login_success(client, app_and_ioc):
    app, ioc = app_and_ioc
    res = client.post("/login", json={"username":"steve","password":"secret"})
    assert res.status_code == 200
    assert "token" in res.get_json()

def test_login_invalid(client):
    res = client.post("/login", json={"username":"nope","password":"nope"})
    assert res.status_code == 403
