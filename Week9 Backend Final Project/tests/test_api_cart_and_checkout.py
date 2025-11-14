import sales_logic

ADMIN = {"Authorization": "Bearer admin"}

def test_see_cart_user(client):
    res = client.get("/shoppingcart", headers=ADMIN)
    assert res.status_code == 200
    body = res.get_json()
    assert isinstance(body, list) or "message" in body

def test_add_to_cart_validation_error(client):
    res = client.post("/shoppingcart", json={"items":[{"product_id":1}]}, headers=ADMIN)
    assert res.status_code == 400

def test_add_to_cart_success(client):
    payload = {
        "date_created": "2025-10-15",
        "items": [{"product_id":1,"quantity":1}]
    }
    res = client.post("/shoppingcart", json=payload, headers=ADMIN)
    assert res.status_code == 200

def test_modify_cart_item_qty_validation(client):
    res = client.patch("/shoppingcart", headers=ADMIN)  # missing params
    assert res.status_code == 400

def test_modify_cart_item_qty_success(client):
    res = client.patch("/shoppingcart?product_id=1&quantity=5", headers=ADMIN)
    assert res.status_code == 200

def test_delete_cart_success(client):
    res = client.delete("/shoppingcart", headers=ADMIN)
    assert res.status_code == 200

def test_checkout_calls_sales_logic(client, monkeypatch):
    called = {"ok": False}
    def fake_complete(sales_date, invoice_address, payment_method, user_id, shopping_cart_info, ioc):
        called["ok"] = True
    monkeypatch.setattr(sales_logic, "complete_sale", fake_complete, raising=True)

    payload = {"sales_date":"2025-10-20","invoice_address":"Somewhere","payment_method":1}
    res = client.post("/checkout", json=payload, headers=ADMIN)
    assert res.status_code == 200
    assert called["ok"] is True
