from flask import Flask, request, Response, jsonify
from ioc_container import IocContainter
from auth_logic import check_auth, get_logged_in_user_id
from werkzeug.exceptions import Forbidden, Unauthorized
import sales_logic

app = Flask("user-service")
ioc_container = IocContainter()

@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None or data.get('role_id') == None):
        return Response(status=400)
    else:
        result = ioc_container.users_repository.insert_user(data.get('username'), data.get('password'), data.get('role_id'))
        user_id = result[0]

        token = ioc_container.jwt_manager.encode({'id':user_id})
        
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
            token = ioc_container.jwt_manager.encode({'id':user_id})
        
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


@app.route('/products', methods=['GET'])
def get_product():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0: 
            if not request.args.get("id"):
                raise ValueError("Missing ID parameter.")
            results = ioc_container.product_repository.get_products_by_id(int(request.args.get("id")))
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
            if "price" not in body:
                raise ValueError("error: price required.")
            if "entry_date" not in body:
                raise ValueError("error: Entry date required.")
            if "stock_qty" not in body:
                raise ValueError("error: stock_qty required.")
            
            ioc_container.product_repository.update_products_by_id(product_id, body.get('name'), body.get('price'), body.get('entry_date'), body.get('stock_qty'))
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


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0:       
            ioc_container.product_repository.delete_products_by_id(product_id)
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
        

@app.route('/sale', methods=['POST'])
def complete_sale():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1, 2], ioc_container)

        if status == 0:
            if not request.is_json:
                        return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}

            if "sales_date" not in body:
                raise ValueError("error: Sales date required.")
            if "total_amount" not in body:
                raise ValueError("error: Total amount required.")
            if "lines" not in body:
                raise ValueError("error: Lines required.")
            
            lines = body.get("lines")
            required_lines = {
                "product_id",
                "quantity"
            }

            for line in lines:
                missing = required_lines - line.keys()
                if missing:
                    raise ValueError(f"error: Missing lines values: {missing}")
            
            user_id = get_logged_in_user_id(token, ioc_container)
            sales_logic.complete_sale(body.get('sales_date'), body.get('total_amount'), user_id, lines, ioc_container)
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


@app.route('/invoices', methods=['GET'])
def get_invoices_by_user():
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1, 2], ioc_container)

        if status == 0:
            user_id = get_logged_in_user_id(token, ioc_container)
            results = ioc_container.invoice_repository.get_invoice_info_by_user(user_id)

            if results:
                return jsonify(results), 200
            else:
                return None
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