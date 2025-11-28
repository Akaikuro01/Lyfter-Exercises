import pytest
from types import SimpleNamespace
import main  # your Flask app module

# ---- Fakes / Stubs ----

class FakeJWT:
    def encode(self, data):
        # just return a simple token label
        role = data.get("role")
        if role == 1:
            return "admin"
        elif role == 2:
            return "user"
        return "unknown"

    def decode(self, token):
        # map back to payloads your API expects
        if token in ("admin",):
            return {"id": 1, "role": 1}
        if token in ("user",):
            return {"id": 2, "role": 2}
        return None  # invalid token

class FakeUsersRepo:
    def __init__(self):
        self.users = {
            ("steve", "secret"): (1, "steve", "secret", 1),  # id, username, password, role_id
        }
        self.by_id = {1: (1, "steve", "secret", 1)}

    def insert_user(self, full_name, email, username, password, role_id):
        # return tuple like your code uses
        new_id = max(self.by_id) + 1 if self.by_id else 1
        self.by_id[new_id] = (new_id, username, password, role_id)
        self.users[(username, password)] = (new_id, username, password, role_id)
        return (new_id,)

    def get_user(self, username, password):
        return self.users.get((username, password), None)

    def get_user_by_id(self, uid):
        return self.by_id.get(uid)

class FakeProductsRepo:
    def __init__(self):
        self.data = {
            1: {"id":1, "name":"Bowl", "unit_price":5.5, "entry_date":"2025-10-11", "stock_qty":110},
            2: {"id":2, "name":"Catnip", "unit_price":4.25, "entry_date":"2025-10-07", "stock_qty":150},
        }
        self.next_id = 3

    def insert_product(self, name, unit_price, entry_date, stock_qty):
        _id = self.next_id; self.next_id += 1
        self.data[_id] = {"id":_id,"name":name,"unit_price":unit_price,"entry_date":entry_date,"stock_qty":stock_qty}
        return (_id,)

    def get_products(self, page, size, _id=None):
        if _id is not None:
            return self.data.get(_id)
        # very simple paging
        items = list(sorted(self.data.values(), key=lambda x: x["id"]))
        start = (page-1)*size if page and size else 0
        end = start + (size or len(items))
        return items[start:end]

    def get_products_by_id(self, _id):
        return self.data.get(_id)

    def update_products_by_id(self, _id, name, unit_price, entry_date, stock_qty):
        if _id not in self.data:
            return SimpleNamespace(rowcount=0)
        self.data[_id].update({"name":name,"unit_price":unit_price,"entry_date":entry_date,"stock_qty":stock_qty})
        return SimpleNamespace(rowcount=1)

    def delete_products_by_id(self, _id):
        existed = _id in self.data
        if existed: del self.data[_id]
        return SimpleNamespace(rowcount=int(existed))

    def modify_stock_product(self, action, product_id, quantity):
        if product_id not in self.data:
            return SimpleNamespace(rowcount=0)
        if action == 0:
            self.data[product_id]["stock_qty"] -= int(quantity)
        else:
            self.data[product_id]["stock_qty"] += int(quantity)
        return SimpleNamespace(rowcount=1)

class FakePaymentRepo:
    def __init__(self):
        self.data = {1: {"id":1,"user_id":1,"brand":"VISA","last4":"1111","exp_month":12,"exp_year":2027}}

    def insert_payment_method(self, user_id, brand, last4, exp_month, exp_year):
        new_id = max(self.data) + 1
        self.data[new_id] = {"id":new_id, "user_id":user_id, "brand":brand, "last4":last4, "exp_month":exp_month, "exp_year":exp_year}
        return (new_id,)

    def get_payment_methods_by_user_id(self, user_id):
        # your main expects a single dict or None
        for pm in self.data.values():
            if pm["user_id"] == user_id:
                return pm
        return None

    def update_payment_methods_by_id(self, _id, user_id, brand, last4, exp_month, exp_year):
        if _id not in self.data:
            return SimpleNamespace(rowcount=0)
        self.data[_id] = {"id":_id,"user_id":user_id,"brand":brand,"last4":last4,"exp_month":exp_month,"exp_year":exp_year}
        return SimpleNamespace(rowcount=1)

    def delete_payment_methods_by_id(self, _id):
        existed = _id in self.data
        if existed: del self.data[_id]
        return SimpleNamespace(rowcount=int(existed))

class FakeCartRepo:
    def __init__(self, products_repo):
        self.products_repo = products_repo
        self.cart_by_user = {
            1: [  # list of lines
                {"cart_id":1,"username":"steve","product_id":1,"product_name":"Bowl","unit_price":5.5,"quantity":2},
                {"cart_id":1,"username":"steve","product_id":2,"product_name":"Catnip","unit_price":4.25,"quantity":1},
            ]
        }

    def get_cart_info_by_user(self, user_id):
        lines = self.cart_by_user.get(user_id, [])
        return [dict(x) for x in lines] if lines else None

    def insert_shopping_cart(self, date_created, user_id):
        # just return a cart id
        return 99

    def insert_cart_items(self, items):
        # append items to user's cart 1 for simplicity
        for it in items:
            self.cart_by_user.setdefault(1, []).append(
                {"cart_id": it.get("cart_id", 99), "username":"steve",
                "product_id":it["product_id"], "product_name": self.products_repo.data[it["product_id"]]["name"],
                "unit_price": self.products_repo.data[it["product_id"]]["unit_price"], "quantity":it["quantity"]}
            )
        return (1,)

    def update_cart_items(self, user_id, product_id, quantity):
        lines = self.cart_by_user.get(user_id, [])
        for ln in lines:
            if ln["product_id"] == product_id:
                ln["quantity"] = int(quantity)
        return SimpleNamespace(rowcount=1)

    def delete_cart_by_user_id(self, user_id):
        self.cart_by_user[user_id] = []
        return SimpleNamespace(rowcount=1)

    def delete_cart_by_id(self, cart_id):
        return SimpleNamespace(rowcount=1)

class FakeInvoiceRepo:
    def __init__(self):
        self.headers = {}
        self.lines = []

    def insert_invoice_headers(self, sale_date, total_amount, invoice_address, payment_method, user_id):
        new_id = (max(self.headers) + 1) if self.headers else 1
        self.headers[new_id] = {"id":new_id,"sale_date":sale_date,"total_amount":total_amount,"invoice_address":invoice_address,"payment_method":payment_method,"user_id":user_id}
        return new_id

    def insert_invoice_lines(self, lines):
        self.lines.extend(lines)
        return (1,)

    def get_invoice_info_by_user(self, user_id):
        # return minimal list
        if not self.headers:
            return None
        out = []
        for h in self.headers.values():
            if h["user_id"] == user_id:
                out.append({"invoice_id":h["id"],"sale_date":h["sale_date"],"username":"steve",
                            "product_name":"Bowl","quantity":1,"subtotal":h["total_amount"],"invoice_total":h["total_amount"]})
        return out or None

class FakeCache:
    def __init__(self):
        self.store = {}

    def check_key(self, key):
        return key in self.store

    def get_data(self, key):
        return self.store[key]

    def store_data(self, key, value):
        self.store[key] = value

    def delete_data_with_pattern(self, pattern):
        # simple wildcard support for demo
        if pattern.endswith("*"):
            prefix = pattern[:-1]
            for k in list(self.store):
                if k.startswith(prefix):
                    del self.store[k]

# ---- Pytest fixtures ----

@pytest.fixture
def app_and_ioc(monkeypatch):
    # build a fake IOC container like main.ioc_container expects
    products = FakeProductsRepo()
    fake_ioc = SimpleNamespace(
        jwt_manager=FakeJWT(),
        users_repository=FakeUsersRepo(),
        product_repository=products,
        payment_method_repository=FakePaymentRepo(),
        cart_repository=FakeCartRepo(products_repo=products),
        invoice_repository=FakeInvoiceRepo(),
        cache_manager=FakeCache(),
    )
    # patch the ioc_container in the running Flask app module
    monkeypatch.setattr(main, "ioc_container", fake_ioc, raising=True)
    return main.app, fake_ioc

@pytest.fixture
def client(app_and_ioc):
    app, _ = app_and_ioc
    app.testing = True
    with app.test_client() as c:
        yield c
