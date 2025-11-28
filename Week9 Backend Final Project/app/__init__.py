from flask import Flask
from ioc_container import IocContainer
from app.product_routes import bp as products_bp
from app.payments_routes import bp as payments_bp
from app.cart_routes import bp as cart_bp
from app.checkout_routes import bp as checkout_bp
from app.invoices_routes import bp as invoices_bp
from app.auth_routes import bp as auth_bp

def create_app():
    app = Flask("petshop-api")
    app.config["JSON_SORT_KEYS"] = False 

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(invoices_bp)

    app.ioc = IocContainer()
    return app
