from flask import Blueprint, request, jsonify, Response, current_app
from werkzeug.exceptions import Forbidden, Unauthorized
from auth_logic import check_auth, get_logged_in_user_id
import json

bp = Blueprint("products", __name__)

default_page_size = 10

def generate_cache_products_page_key(page, size):
    return f'getProducts-page{page}-size{size}'

def generate_cache_products_id_key(_id):
    return f'getProducts-id{_id}'

@bp.post('/products')
def register_product():
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0:            
            if not request.is_json:
                    return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}

            if "name" not in body:
                raise ValueError("error: name required.")
            if "price" not in body:
                raise ValueError("error: price required.")
            if "entry_date" not in body:
                raise ValueError("error: Entry date required.")
            if "stock_qty" not in body:
                raise ValueError("error: Stock Quantity required.")
            
            ioc_container.product_repository.insert_product(body.get('name'), body.get('price'), body.get('entry_date'), body.get('stock_qty'))
            ioc_container.cache_manager.delete_data_with_pattern("getProducts-page*")
            ioc_container.cache_manager.delete_data_with_pattern("getProducts-id*")
            return jsonify({"message": "Product inserted successfully!"}), 200
        elif status == 1:
            raise Unauthorized("Login required/ Incorrect token.")
        elif status == 2:
            raise Forbidden("Insufficient permissions.")
    except Forbidden as ex:
        return jsonify(message=str(ex)), 403
    except Unauthorized as ex:
        return jsonify(message=str(ex)), 401
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@bp.get('/products/<int:page>')
def get_product(page):
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0: 
            if not request.args.get("id"):
                # We first check if values are cached
                page_key = generate_cache_products_page_key(page, default_page_size)
                if ioc_container.cache_manager.check_key(page_key):
                    results = ioc_container.cache_manager.get_data(page_key)
                    return Response(results, mimetype="application/json")
                else:
                    results = ioc_container.product_repository.get_products(page, default_page_size)
                    ioc_container.cache_manager.store_data(page_key, json.dumps(results, separators=(",", ":")))
                return jsonify(results), 200
            else:
                _id = int(request.args.get("id"))
                id_key = generate_cache_products_id_key(_id)
                if ioc_container.cache_manager.check_key(id_key):
                    results = ioc_container.cache_manager.get_data(id_key)
                    return Response(results, mimetype="application/json")
                else:
                    results = ioc_container.product_repository.get_products(0, 0, _id)
                    ioc_container.cache_manager.store_data(id_key, json.dumps(results, separators=(",", ":")))
                    return jsonify(results), 200
        elif status == 1:
            raise Unauthorized("Login required/ Incorrect token.")
        elif status == 2:
            raise Forbidden("Insufficient permissions.")
    except Forbidden as ex:
        return jsonify(message=str(ex)), 403
    except Unauthorized as ex:
        return jsonify(message=str(ex)), 401
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500



@bp.put('/products/<int:product_id>')
def update_product(product_id):
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0: 
            if not request.is_json:
                    return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}
        
            if "name" not in body:
                raise ValueError("error: name required.")
            if "unit_price" not in body:
                raise ValueError("error: price required.")
            if "entry_date" not in body:
                raise ValueError("error: Entry date required.")
            if "stock_qty" not in body:
                raise ValueError("error: stock_qty required.")
            
            ioc_container.product_repository.update_products_by_id(product_id, body.get('name'), body.get('unit_price'), body.get('entry_date'), body.get('stock_qty'))
            ioc_container.cache_manager.delete_data_with_pattern("getProducts-page*")
            ioc_container.cache_manager.delete_data_with_pattern("getProducts-id*")
            return jsonify({"message": "Product updated successfully!"}), 200
        elif status == 1:
            raise Unauthorized("Login required/ Incorrect token.")
        elif status == 2:
            raise Forbidden("Insufficient permissions.")
    except Forbidden as ex:
        return jsonify(message=str(ex)), 403
    except Unauthorized as ex:
        return jsonify(message=str(ex)), 401
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@bp.delete('/products/<int:product_id>')
def delete_product(product_id):
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0:       
            ioc_container.product_repository.delete_products_by_id(product_id)
            ioc_container.cache_manager.delete_data_with_pattern("getProducts-page*")
            ioc_container.cache_manager.delete_data_with_pattern("getProducts-id*")
            return jsonify({"message": "Product deleted successfully!"}), 200
        elif status == 1:
            raise Unauthorized("Login required/ Incorrect token.")
        elif status == 2:
            raise Forbidden("Insufficient permissions.")
    except Forbidden as ex:
        return jsonify(message=str(ex)), 403
    except Unauthorized as ex:
        return jsonify(message=str(ex)), 401
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500
        
@bp.patch('/returns')
def return_sale():
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1, 2], ioc_container)

        if status == 0:
            body = request.get_json(silent=True) or {}
            
            if "product_id" not in body:
                raise ValueError("error: Product ID required.")
            if "quantity" not in body:
                raise ValueError("error: Quantity required.")
            
            ioc_container.product_repository.modify_stock_product(1, body.get('product_id'), body.get('quantity'))
            ioc_container.cache_manager.delete_data_with_pattern("getProducts-page*")
            return jsonify({"message": "Return completed successfully!"}), 200
        elif status == 1:
            raise Unauthorized("Login required/ Incorrect token.")
        elif status == 2:
            raise Forbidden("Insufficient permissions.")
    except Forbidden as ex:
        return jsonify(message=str(ex)), 403
    except Unauthorized as ex:
        return jsonify(message=str(ex)), 401
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500