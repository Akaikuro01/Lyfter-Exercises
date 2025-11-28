import pytest
from sales_logic import complete_sale

class IOC:
    def __init__(self):
        self.product_repository = self
        self.payment_method_repository = self
        self.invoice_repository = self
        self.cart_repository = self
        self._products = {1: {"id":1,"stock_qty":5,"unit_price":10.0}}
        self._pm_ok = {1: {"id":1,"user_id":1}}
        self._stock_updates = []

    # product repo
    def get_products_by_id(self, pid):
        return {"id":pid, "stock_qty": self._products.get(pid, {}).get("stock_qty", 0), "unit_price": self._products.get(pid, {}).get("unit_price", 0)} if pid in self._products else None
    def modify_stock_product(self, action, product_id, quantity):
        self._stock_updates.append((action, product_id, quantity))
        if action == 0:
            self._products[product_id]["stock_qty"] -= int(quantity)

    # payment repo
    def get_payment_methods_by_user_id(self, pm_id):
        return self._pm_ok.get(pm_id)

    # invoice repo
    def insert_invoice_headers(self, sale_date, total_amount, invoice_address, payment_method, user_id):
        return 123
    def insert_invoice_lines(self, lines):
        return (1,)

    # cart repo
    def delete_cart_by_user_id(self, user_id):
        return None

def test_complete_sale_success():
    ioc = IOC()
    items = [{"product_id":1,"unit_price":10.0,"quantity":2}]
    complete_sale("2025-10-20","Addr",1,1,items,ioc)
    # stock decreased
    assert ioc._products[1]["stock_qty"] == 3

def test_complete_sale_product_not_exists():
    ioc = IOC()
    items = [{"product_id":99,"unit_price":10.0,"quantity":1}]
    with pytest.raises(ValueError):
        complete_sale("2025-10-20","Addr",1,1,items,ioc)

def test_complete_sale_insufficient_stock():
    ioc = IOC()
    items = [{"product_id":1,"unit_price":10.0,"quantity":99}]
    with pytest.raises(ValueError):
        complete_sale("2025-10-20","Addr",1,1,items,ioc)

def test_complete_sale_invalid_payment_method():
    ioc = IOC()
    ioc._pm_ok = {}  # no valid PM
    items = [{"product_id":1,"unit_price":10.0,"quantity":1}]
    with pytest.raises(ValueError):
        complete_sale("2025-10-20","Addr",999,1,items,ioc)
