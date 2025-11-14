ADMIN = {"Authorization": "Bearer admin"}

def test_register_payment_method_success(client):
    res = client.post("/paymentmethods", json={
        "brand":"VISA","last4":"4242","exp_month":12,"exp_year":2030
    }, headers=ADMIN)
    assert res.status_code == 200

def test_register_payment_method_missing_field(client):
    res = client.post("/paymentmethods", json={"brand":"VISA"}, headers=ADMIN)
    assert res.status_code == 400

def test_get_payment_methods_success(client):
    res = client.get("/paymentmethods", headers=ADMIN)
    assert res.status_code == 200
    body = res.get_json()
    # could be None if no PM for user, but our Fake has one seeded for user_id=1
    assert body is None or "user_id" in body

def test_update_payment_method_success(client):
    res = client.put("/paymentmethods/1", json={
        "user_id":1,"brand":"MC","last4":"5555","exp_month":1,"exp_year":2031
    }, headers=ADMIN)
    assert res.status_code == 200

def test_delete_payment_method_success(client):
    res = client.delete("/paymentmethods/1", headers=ADMIN)
    assert res.status_code == 200
