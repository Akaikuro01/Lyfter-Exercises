from flask import Blueprint, request, jsonify, Response, current_app
from werkzeug.exceptions import Forbidden, Unauthorized
from auth_logic import check_auth, get_logged_in_user_id

bp = Blueprint("cart", __name__)


@bp.get('/shoppingcart')
def see_cart_user():
    ioc_container = current_app.ioc
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

@bp.post('/shoppingcart')
def add_to_shopping_cart():
    ioc_container = current_app.ioc
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

@bp.patch('/shoppingcart')
def modify_cart_item_qty():
    ioc_container = current_app.ioc
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


@bp.delete('/shoppingcart')
def delete_shopping_cart():
    ioc_container = current_app.ioc
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