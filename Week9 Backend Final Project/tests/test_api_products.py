ADMIN = {"Authorization": "Bearer admin"}

def test_register_product_success(client):
    res = client.post("/products", json={
        "name":"Rubber Fetch Ball (Large)","price":6.50,"entry_date":"2025-10-24","stock_qty":150
    }, headers=ADMIN)
    assert res.status_code == 200
    assert "Product inserted successfully" in res.get_json()["message"]

def test_register_product_validation_error(client):
    res = client.post("/products", json={"name":"X"}, headers=ADMIN)
    assert res.status_code == 400
    assert "error:" in res.get_json()["message"]

def test_get_products_paged_through_cache(client, app_and_ioc):
    app, ioc = app_and_ioc
    # first call: fills cache
    res1 = client.get("/products/1", headers=ADMIN)
    assert res1.status_code == 200
    # second call should hit cache path and still succeed
    res2 = client.get("/products/1", headers=ADMIN)
    assert res2.status_code == 200

def test_get_products_by_id(client):
    res = client.get("/products/1?id=2", headers=ADMIN)
    assert res.status_code == 200
    body = res.get_json()
    assert body["id"] == 2
    assert body["name"]

def test_update_product_success(client):
    res = client.put("/products/1", json={
        "name":"Bowl XL","unit_price":9.99,"entry_date":"2025-10-11","stock_qty":200
    }, headers=ADMIN)
    assert res.status_code == 200

def test_update_product_missing_fields(client):
    res = client.put("/products/1", json={"name":"only"}, headers=ADMIN)
    assert res.status_code == 400

def test_delete_product_success(client):
    res = client.delete("/products/2", headers=ADMIN)
    assert res.status_code == 200
