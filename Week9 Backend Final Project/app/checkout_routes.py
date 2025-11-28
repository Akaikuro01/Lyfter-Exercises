from flask import Blueprint, request, jsonify, Response, current_app
from werkzeug.exceptions import Forbidden, Unauthorized
from auth_logic import check_auth, get_logged_in_user_id
from sales_logic import complete_sale

bp = Blueprint("checkout", __name__)

@bp.post('/checkout')
def complete_checkout():
    ioc_container = current_app.ioc
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

            complete_sale(body.get('sales_date'), body.get('invoice_address'), body.get('payment_method'), user_id, shopping_cart_info, ioc_container)
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