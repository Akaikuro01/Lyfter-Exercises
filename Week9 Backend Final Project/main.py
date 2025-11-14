from flask import Flask, request, Response, jsonify
from ioc_container import IocContainter
from auth_logic import check_auth, get_logged_in_user_id
from werkzeug.exceptions import Forbidden, Unauthorized
import sales_logic
import json

app = Flask("user-service")
ioc_container = IocContainter()

default_page_size = 10

def generate_cache_products_page_key(page, size):
    return f'getProducts-page{page}-size{size}'

def generate_cache_products_id_key(_id):
    return f'getProducts-id{_id}'

def generate_cache_invoices_page_key(page, size):
    return f'getInvoices-page{page}-size{size}'

@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None or data.get('role_id') == None or data.get("email") == None or data.get('full_name') == None):
        return Response(status=400)
    else:
        result = ioc_container.users_repository.insert_user(data.get('full_name'), data.get('email'), data.get('username'), data.get('password'), data.get('role_id'))
        print(result)
        user_id = result[0]
        role = data.get('role_id')

        token = ioc_container.jwt_manager.encode({'id':user_id, 'role': role})
        
        return jsonify(token=token)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = ioc_container.users_repository.get_user(data.get('username'), data.get('password'))

        if(result == None):
            return Response(status=403)
        else:
            user_id = result[0]
            role = result[3]
            token = ioc_container.jwt_manager.encode({'id':user_id, 'role': role})
        
            return jsonify(token=token)

@app.route('/me')
def me():
    try:
        token = request.headers.get('Authorization')
        # I pass [1, 2] as the supported roles to do this action: 1 - Admin 2 - User
        status = check_auth(token, [1, 2], ioc_container)
        if status == 0:
            token = token.replace("Bearer ","")
            decoded = ioc_container.jwt_manager.decode(token)
            user_id = decoded['id']

            user = ioc_container.users_repository.get_user_by_id(user_id)

            return jsonify(id=user_id, username=user[1], role=user[3])
        elif status == 1:
            raise Unauthorized("Login required/ Incorrect token.")
    except Unauthorized as ex:
        return jsonify(message=str(ex)), 401
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500

@app.route('/products', methods=['POST'])
def register_product():
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


@app.route('/products/<int:page>', methods=['GET'])
def get_product(page):
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



@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
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


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
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
        

#----------------------------------------------------------------------------------------
@app.route('/paymentmethods', methods=['POST'])
def register_payment_method():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0:            
            if not request.is_json:
                    return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}

            if "brand" not in body:
                raise ValueError("error: Brand required.")
            if "last4" not in body:
                raise ValueError("error: Last 4 digits required.")
            if "exp_month" not in body:
                raise ValueError("error: Expiring month required.")
            if "exp_year" not in body:
                raise ValueError("error: Expiring year required.")
            
            user_id = get_logged_in_user_id(token, ioc_container)
            ioc_container.payment_method_repository.insert_payment_method(user_id, body.get('brand'), body.get('last4'), body.get('exp_month'), body.get('exp_year'))
            return jsonify({"message": "Payment method inserted successfully!"}), 200
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


@app.route('/paymentmethods', methods=['GET'])
def get_payment_methods():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0: 
            user_id = get_logged_in_user_id(token, ioc_container)           
            results = ioc_container.payment_method_repository.get_payment_methods_by_user_id(user_id)
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



@app.route('/paymentmethods/<int:pm_id>', methods=['PUT'])
def update_payment_method(pm_id):
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0: 
            if not request.is_json:
                    return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}
        
            if "user_id" not in body:
                raise ValueError("error: User ID required.")
            if "brand" not in body:
                raise ValueError("error: Brand required.")
            if "last4" not in body:
                raise ValueError("error: Last 4 digits required.")
            if "exp_month" not in body:
                raise ValueError("error: Expiring month required.")
            if "exp_year" not in body:
                raise ValueError("error: Expiring year required.")
            
            ioc_container.payment_method_repository.update_payment_methods_by_id(pm_id, body.get('user_id'), body.get('brand'), body.get('last4'), body.get('exp_month'), body.get('exp_year'))

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


@app.route('/paymentmethods/<int:pm_id>', methods=['DELETE'])
def delete_payment_method(pm_id):
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0:       
            ioc_container.payment_method_repository.delete_payment_methods_by_id(pm_id)
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
        
#----------------------------------------------------------------------------------------


@app.route('/shoppingcart', methods=['GET'])
def see_cart_user():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)
        if status == 0:
            user_id = get_logged_in_user_id(token, ioc_container)
            shopping_cart = ioc_container.cart_repository.get_cart_info_by_user(user_id)

            if shopping_cart:
                return jsonify(shopping_cart), 200
            else:
                return jsonify({"message": "Cart is empty"}), 200
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

@app.route('/shoppingcart', methods=['POST'])
def add_to_shopping_cart():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)
        if status == 0:
            if not request.is_json:
                        return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}

            if "date_created" not in body:
                raise ValueError("error: Sales date required.")
            if "items" not in body:
                raise ValueError("error: Items required.")
            
            items = body.get("items")
            required_lines = {
                "product_id",
                "quantity"
            }

            for item in items:
                missing = required_lines - item.keys()
                if missing:
                    raise ValueError(f"error: Missing item values: {missing}")
            
            user_id = get_logged_in_user_id(token, ioc_container)
            cart_id = ioc_container.cart_repository.insert_shopping_cart(body.get('date_created'), user_id)
            for item in items:
                item["cart_id"] = cart_id
            print(items)
            ioc_container.cart_repository.insert_cart_items(items)
            return jsonify({"message": f"Succesfully added to cart: {items}"}), 200
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

@app.route('/shoppingcart', methods=['PATCH'])
def modify_cart_item_qty():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)
        if status == 0:
            if not request.args.get("product_id"):
                raise ValueError("Missing product ID parameter.")
            if not request.args.get("quantity"):
                raise ValueError("Missing quantity parameter.")
            
            product_id = int(request.args.get("product_id"))
            quantity = request.args.get("quantity")

            user_id = get_logged_in_user_id(token, ioc_container)
            ioc_container.cart_repository.update_cart_items(user_id,product_id, quantity)
            return jsonify({"message": "Succesfully updated your cart!"}), 200
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


@app.route('/shoppingcart', methods=['DELETE'])
def delete_shopping_cart():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)
        if status == 0:
            user_id = get_logged_in_user_id(token, ioc_container)
            ioc_container.cart_repository.delete_cart_by_user_id(user_id)
            return jsonify({"message": "Succesfully emptied your cart!"}), 200
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


@app.route('/checkout', methods=['POST'])
def complete_checkout():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1, 2], ioc_container)

        if status == 0:
            if not request.is_json:
                return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}

            if "sales_date" not in body:
                raise ValueError("error: Sales date required.")
            if "invoice_address" not in body:
                raise ValueError("error: Invoice address required.")
            if "payment_method" not in body:
                raise ValueError("error: Payment Method required.")
            
            user_id = get_logged_in_user_id(token, ioc_container)
            shopping_cart_info = ioc_container.cart_repository.get_cart_info_by_user(user_id)

            sales_logic.complete_sale(body.get('sales_date'), body.get('invoice_address'), body.get('payment_method'), user_id, shopping_cart_info, ioc_container)
            ioc_container.cache_manager.delete_data_with_pattern("getInvoices-page*")
            #I am also deleting cache for prdducts as I had to reduce stock
            ioc_container.cache_manager.delete_data_with_pattern("getProducts-page*")
            return jsonify({"message": "Sale completed successfully!"}), 200
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


@app.route('/invoices/<int:page>', methods=['GET'])
def get_invoices_by_user(page):
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1, 2], ioc_container)

        if status == 0:
            page_key = generate_cache_invoices_page_key(page, default_page_size)
            if ioc_container.cache_manager.check_key(page_key):
                    results = ioc_container.cache_manager.get_data(page_key)
                    return Response(results, mimetype="application/json")
            else:
                user_id = get_logged_in_user_id(token, ioc_container)
                results = ioc_container.invoice_repository.get_invoice_info_by_user(user_id)

            if results:
                return jsonify(results), 200
            else:
                return jsonify([]), 200
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

@app.route('/returns', methods=['PATCH'])
def return_sale():
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

if __name__ == "__main__":
    app.run(host="localhost", debug=True)